import os
from flask import Flask, request, jsonify
import pickle

# Load model
model_file = 'Mideterm_model.bin'
try:
    with open(model_file, 'rb') as f_in:
        dv, model = pickle.load(f_in)
    print("Model and DictVectorizer loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    return jsonify(result)

if __name__ == "__main__":
    # Get the port number from the environment variable for Render
    port = int(os.environ.get("PORT", 9696))  # Default to 9696 if not set by Render
    app.run(debug=False, host="0.0.0.0", port=port)  # Bind to the dynamic port
