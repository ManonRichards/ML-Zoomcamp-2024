import pickle
from flask import Flask, request, jsonify
import os  # We need this line to use the correct port

# Load the model and the DictVectorizer
model_file = 'Capstone1_Model.bin'
with open(model_file, 'rb') as f_in:
    dv, log_reg = pickle.load(f_in)

# Initialize the Flask app
app = Flask('score')

@app.route('/predict', methods=['POST'])

def predict():
    # Get JSON data from the request
    student = request.get_json()

    # Transform the customer data using the vectorizer
    X = dv.transform([student])  # Wrap customer in a list for single prediction
    y_pred = log_reg.predict_proba(X)[0, 1]
    score = y_pred >= 0.5

    # Create the response object
    result = {
        'score_probability': float(y_pred),
        'high score': bool(score)
    }

    return jsonify(result)

if __name__ == "__main__":
    # Use the port that Render provides. If it's not available, use 1911 as a fallback
    port = int(os.environ.get("PORT", 1911))
    app.run(debug=True, host="0.0.0.0", port=port)

