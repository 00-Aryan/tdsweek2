from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student marks data
try:
    with open("q-vercel-python.json", "r") as file:
        marks_data = json.load(file)
except Exception as e:
    print(f"Error loading JSON file: {e}")
    marks_data = []

@app.route("/api", methods=["GET"])
def get_marks():
    try:
        # Get the 'name' parameter as a list
        names = request.args.getlist("name")
        
        # Find marks for each name in the list
        marks = []
        for name in names:
            # Search for the student in the list
            student = next((item for item in marks_data if item["name"] == name), None)
            marks.append(student["marks"] if student else None)

        # Return the marks as a JSON response
        return jsonify({"marks": marks})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
