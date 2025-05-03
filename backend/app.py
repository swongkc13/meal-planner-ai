from flask import Flask, request, jsonify
from recommend import recommend

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    try:
        data = request.get_json()
        query = data.get("query", "")
        results = recommend(query)
        return jsonify(results)
    except Exception as e:
        print("💥 ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
