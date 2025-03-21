import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# 1️⃣ Trained Model & Vectorizer Load Karo
model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# 2️⃣ Dataset Load Karo
df = pd.read_csv("dataset.csv")

# 3️⃣ Feature & Label Define Karo
X = df["URL"]  # Features (URLs)
y = df["Label"]  # Labels (0 or 1)

# 4️⃣ URLs Ko Transform Karo (Text to Numbers)
X_transformed = vectorizer.transform(X)

# 5️⃣ Model Se Predictions Lo
y_pred = model.predict(X_transformed)

# 6️⃣ Accuracy & Performance Check Karo
accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y_pred)

print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")
print("🔹 Classification Report:\n", report)
