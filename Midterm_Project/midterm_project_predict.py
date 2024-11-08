import pickle
from flask import Flask, request, jsonify
import os  # We need this line to use the correct port

# Load the model and the DictVectorizer
model_file = 'Mideterm_model.bin'
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Initialize the Flask app
app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    customer = request.get_json()

    # Transform the customer data using the vectorizer
    X = dv.transform([customer])  # Wrap customer in a list for single prediction
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    # Create the response object
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == "__main__":
    # Use the port that Render provides. If it's not available, use 1911 as a fallback
    port = int(os.environ.get("PORT", 1911))
    app.run(debug=True, host="0.0.0.0", port=port)

 


