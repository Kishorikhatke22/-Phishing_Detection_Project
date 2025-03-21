from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ✅ Home Page (Frontend Render Karega)
@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' is inside the 'templates' folder

# ✅ Block Site API (POST Request)
@app.route('/block', methods=['POST'])
def block_site():
    try:
        data = request.get_json()
        url = data.get('url')

        if not url:
            return jsonify({"error": "Invalid URL"}), 400

        # 📝 Blocked URLs ko file me save karo
        with open("blocked_sites.txt", "a") as file:
            file.write(url + "\n")

        return jsonify({"message": "Site blocked successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
