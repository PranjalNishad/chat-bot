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

## 🚀 Setup Instructions

  ### 1️⃣ Clone the Repository
  
  ```bash
  git clone https://github.com/PranjalNishad/chat-bot.git
  cd chat-bot

**## Create a Virtual Environment (Recommended)**

    # On Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    venv\Scripts\activate

**3️⃣ Install Dependencies**

**If you just cloned the repo and don’t have required libraries, install everything from requirements.txt:**

        pip install -r requirements.txt

 **If you don’t have a requirements.txt, you can create one (after installing Flask or other libs) with:**

    pip freeze > requirements.txt

**4️⃣ Run the Backend**

    python backend.py


**By default, this will start the server at:**

    http://127.0.0.1:5000


