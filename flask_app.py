from flask import Flask, render_template, request, jsonify
import pickle
from flask_sqlalchemy import SQLAlchemy
import datetime
import os  # Importing OS module for file handling

app = Flask(__name__)

# ✅ Ensure 'safe_sites.txt' exists
SAFE_SITES_FILE = "safe_sites.txt"
if not os.path.exists(SAFE_SITES_FILE):
    with open(SAFE_SITES_FILE, "w") as file:
        file.write("")  # Create an empty file

# ✅ Load Trained ML Model & Vectorizer
try:
    model = pickle.load(open("phishing_model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    print("✅ Model & Vectorizer Loaded Successfully!")
except Exception as e:
    print(f"❌ Error Loading Model: {e}")

# ✅ SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phishing_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ✅ Database Model for Reported Phishing Sites
class PhishingReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# ✅ Create Database Tables
with app.app_context():
    db.create_all()

# ✅ Route to Suggest Safe Site
@app.route("/suggest_safe_site", methods=["POST"])
def suggest_safe_site():
    url = request.form.get("url")  # Getting URL from frontend
    print(f"📥 Received Safe Site Suggestion: {url}")  # Debugging Print

    if not url:
        print("❌ No URL Provided!")  # Debugging Print
        return jsonify({"error": "No URL provided"}), 400

    try:
        # ✅ Save the suggested safe site in safe_sites.txt
        with open(SAFE_SITES_FILE, "a") as file:
            file.write(url + "\n")

        print("✅ Safe Site Saved Successfully!")  # Debugging Print
        return jsonify({"message": "Safe site suggested successfully!"}), 200

    except Exception as e:
        print(f"❌ Error Saving Safe Site: {e}")  # Debugging Print
        return jsonify({"error": str(e)}), 500

# ✅ Home Route (Renders Frontend)
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        print(f"🔍 Checking URL: {url}")  # Debugging print
        url_transformed = vectorizer.transform([url])
        prediction = model.predict(url_transformed)[0]
        result = "Phishing" if prediction == 1 else "Legitimate"
        print(f"✅ Prediction: {result}")  # Debugging print
        return render_template("index.html", url=url, result=result)

    return render_template("index.html", result=result)

# ✅ API Route for Blocking Sites
@app.route("/block", methods=["POST"])
def block_site():
    try:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"error": "Invalid URL"}), 400

        # 📝 Blocked URLs ko file me save karo
        with open("blocked_sites.txt", "a") as file:
            file.write(url + "\n")

        return jsonify({"message": "Site blocked successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ API Route for Phishing Detection
@app.route("/predict", methods=["POST"])
def predict():
    print("🚀 Predict Route Hit!")  # Debugging print
    try:
        url = request.form.get("url", "")  # Get URL safely
        print(f"🔍 Checking URL: {url}")  

        if not url:
            return jsonify({"error": "No URL provided"}), 400

        url_transformed = vectorizer.transform([url])
        prediction = model.predict(url_transformed)[0]
        result = "Phishing" if prediction == 1 else "Legitimate"

        print(f"✅ Prediction: {result}")  
        return jsonify({"result": result})
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ Route to Handle Phishing Reporting
@app.route("/report", methods=["POST"])
def report_phishing():
    try:
        data = request.get_json()
        url = data.get("url")

        if url:
            new_report = PhishingReport(url=url)
            db.session.add(new_report)
            db.session.commit()
            return jsonify({"message": "Phishing site reported successfully!"}), 201
        else:
            return jsonify({"error": "Invalid URL"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
