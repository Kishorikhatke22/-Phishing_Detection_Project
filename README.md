<h1>Phishing Detection and Response System</h1>


A Flask-based Machine Learning project that detects phishing websites and provides a response mechanism.

 <h1>Table of Contents</h1>
 
 ✅About the Project
 
 ✅Features
 
 ✅Tech Stack
 
 ✅Project Architecture
 
 ✅Installation
 
 ✅Usage Guide
 
 ✅API Endpoints
 
 ✅Deployment Guide

<h1>About the Project</h1>

This Phishing Detection and Response System is designed to detect phishing websites using machine learning techniques. It classifies URLs as safe or phishing based on extracted features. Additionally, it includes a response mechanism that allows users to block malicious websites.

 <h1>Key Information</h1>
 
 Project Type: Machine Learning + Cybersecurity
 
 Backend: Flask (Python)
 
 Frontend: HTML, CSS, JavaScript
 
 Database: SQLite

 <h1>Features</h1>
 
✅ Detect phishing websites using a trained ML model

✅ Maintain a blocklist and safe list of websites

✅ Web-based UI for easy interaction

✅ API-based approach for third-party integration

✅ Logs phishing detection attempts for future reference

✅ Automatic updates of phishing URLs

✅ Ready for deployment on Render

<h1>Tech Stack</h1>

Technology	                -             Purpose

Python	                    -             Backend logic & ML model

Flask                	     -              Web framework for API & UI

Scikit-learn	              -             Machine learning for phishing detection

Pandas & NumPy       	     -              Data processing

HTML, CSS, JavaScript	     -             Frontend

SQLite                     -              Database to store blocked & safe sites

Render                     -           	 Deployment

 <h1>Project Architecture</h1>
 
 Phishing-Detection-and-Response/
 
│── static/                  # CSS & JavaScript files

│── templates/               # HTML files

│   ├── index.html           # Main UI

│   ├── result.html          # Result page

│── app.py                   # Flask application

│── phishing_model.pkl       # Machine Learning Model

│── blocked_sites.txt        # Blocked phishing websites

│── safe_sites.txt           # Safe websites list

│── requirements.txt         # Required Python libraries

│── README.md                # Documentation

 <h1>Installation</h1>
 
1️⃣  Clone the Repository
git clone https://github.com/Kishorikhatke22/Phishing-Detection-and-Response.git
cd Phishing-Detection-and-Response

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
python app.py
Then open: http://127.0.0.1:5000/ in your browser.


 <h1>Usage Guide</h1>
🔹 Detect Phishing URL

1️⃣ Open the website (http://127.0.0.1:5000/)

2️⃣ Enter a URL in the input box

3️⃣ Click "Check URL"

4️⃣ The system will classify it as Phishing or Legitimate

🔹 Block a Website

1️⃣ Go to http://127.0.0.1:5000/block

2️⃣ Enter the URL to be blocked

3️⃣ Click "Block"

🔹 View Blocked and Safe Sites
Open blocked_sites.txt to see blocked phishing sites
Open safe_sites.txt to see trusted websites


<h1>API Endpoints</h1>
Endpoint	             Method	                  Description
/	                     GET	                    Loads the main UI
/check-url   	         POST                   	Checks if a URL is phishing or safe
/block	               POST	                    Blocks a phishing website
/safe-sites  	         GET	                    Returns the list of safe sites

<h1>Deployment Guide</h1>

This project can be hosted on:

✅ Render









