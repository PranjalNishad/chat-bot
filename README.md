# 🤖 Chat-Bot

A simple chatbot project with a Python backend and a web-based frontend.  
The chatbot interacts with users and can fetch information from `admissions_data.json`.

---

## 📂 Project Structure

    ├── backend.py # Python backend server
    ├── admissions_data.json # Data used by the chatbot
    ├── index.html # Frontend UI
    ├── script.js # Chatbot logic (frontend)
    ├── style.css # Styling
    ├── requirements.txt # Python dependencies
    └── image/ # (Optional) images used in UI


---


---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PranjalNishad/chat-bot.git
cd chat-bot

---

2️⃣ Create a Virtual Environment (Recommended)

    # On Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    venv\Scripts\activate

---

3️⃣ Install Dependencies

If you just cloned the repo and don’t have required libraries, install everything from requirements.txt:

    pip install -r requirements.txt

---

4️⃣ Run the Backend

    python backend.py

-------

📦 Libraries Used
1. Flask

Used to create the backend server and APIs.
👉 Installation:

        pip install flask

2. Flask-Cors (optional but recommended)

If your frontend (index.html) makes requests from another port (like file:// or http://127.0.0.1:5500), you’ll need CORS support.
👉 Installation:

        pip install flask-cors

3. JSON (built-in)

Python’s json library is used to load and parse admissions_data.json.
👉 No installation needed (it comes with Python).

4. Requests (optional)

If your chatbot fetches data from external APIs.
👉 Installation:

        pip install requests








