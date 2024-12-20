import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(dv_file, 'rb') as f1_in:
    dv = pickle.load(f1_in)

with open(model_file, 'rb') as f2_in:
     model = pickle.load(f2_in)

app = Flask('Q4HW')
@app.route('/Q4HW', methods = ['POST'])

def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0,1]
    subscription = y_pred>=0.5
    
    
    result = {
        'probability': float(y_pred), 
        'subscription': bool(subscription)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 9696)