from flask import Flask, request, jsonify
from flask_cors import CORS
from recommend import get_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_query = data.get("query", "")
    desired_tags = data.get("tags", [])
    max_budget = data.get("max_budget")
    max_time = data.get("max_time")
    preferred_ingredients = data.get("preferred_ingredients", [])

    recommendations = get_recommendations(
        user_query,
        desired_tags,
        max_budget,
        max_time,
        preferred_ingredients
    )
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
