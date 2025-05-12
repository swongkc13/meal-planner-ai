from flask import Flask, request, jsonify
from flask_cors import CORS
from recommend import get_recommendations

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query", "")
    tags = data.get("tags", [])
    max_budget = data.get("max_budget")
    max_time = data.get("max_time")
    preferred_ingredients = data.get("preferred_ingredients", [])

    results = get_recommendations(query, tags, max_budget, max_time, preferred_ingredients)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
