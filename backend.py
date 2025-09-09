from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  

# Load data from JSON

with open("admissions_data.json", "r", encoding="utf-8") as f:
    college_data = json.load(f)

# Chat endpoint

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    response = "I'm not sure about that. Please ask about admissions, fees, eligibility, seats, or process."

    # Greetings
    if any(word in user_message for word in ["hi", "hello", "hey"]):
        response = f"Hello! I am the {college_data['college']['short_name']} admissions assistant. How can I help you today?"

    # College name
    elif "name" in user_message or "college" in user_message:
        response = f"Our college is {college_data['college']['name']} ({college_data['college']['short_name']})."


    # Location / Address
    elif "location" in user_message or "address" in user_message:
        response = f"We are located at {college_data['college']['address']}. Affiliation: {college_data['college']['affiliation']}."

    # Contact info
    elif "contact" in user_message or "email" in user_message or "phone" in user_message:
        c = college_data["college"]["contacts"]
        response = f"You can contact us at {c['admissions_email']} or call {c['phone']}. Website: {c['website']}"

    # Eligibility
    elif "eligibility" in user_message:
        response = college_data["admissions"]["general_eligibility"]

    # Scholarships\
    elif any(word in user_message for word in ["grant", "scholarship", "scholarships", "financial aid", "fee waiver"]):
        scholarships = college_data["admissions"].get("scholarships") or college_data["admissions"].get("grant")
        if scholarships:
            response = "Available Scholarships:\n- " + "\n- ".join(scholarships)
        else:
            response = "No scholarship information is available at the moment."


    # Documents
    elif "document" in user_message or "certificate" in user_message:
        response = "Documents required:\n- " + "\n- ".join(college_data["admissions"]["documents_required"])


    # Seats
    elif "seat" in user_message:
        cse = college_data["programs"]["B.Tech"]["branches"]["CSE"]["seats"]
        aiml = college_data["programs"]["B.Tech"]["branches"]["AI/ML"]["seats"]
        response = f"Seat matrix:\n- CSE: {cse}\n- AI/ML: {aiml}"

    # Fees
    elif "fee" in user_message or "fees" in user_message:
        btech = college_data["programs"]["B.Tech"]
        mba = college_data["programs"]["MBA"]
        response = (
            f"B.Tech fees: ₹{btech['base_fees_per_year']}/year "
            f"(JEE quota: ₹{btech['jee_subsidized_fees_per_year']}/year).\n"
            f"MBA fees: ₹{mba['base_fees_per_year']}/year."
        )

    # Admission process
    elif "apply" in user_message or "admission" in user_message or "process" in user_message:
        steps = "\n".join([f"{i+1}. {s}" for i, s in enumerate(college_data["admissions"]["process"])])
        response = f"Admission process:\n{steps}\nFor more details visit: {college_data['college']['contacts']['website']}"

    # FAQ fallback
    else:
        for faq in college_data["faqs"]:
            if any(word in user_message for word in faq["q"].lower().split()):
                response = faq["a"]
                break

    return jsonify({"response": response})



if __name__ == "__main__":
    app.run(debug=True, port=5000)
