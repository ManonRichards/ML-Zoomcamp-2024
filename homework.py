import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(dv_file, 'rb') as f1_in:
    dv = pickle.load(f1_in)

with open(model_file, 'rb') as f2_in:
     model = pickle.load(f2_in)

customer = {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform([customer])

y_pred = model.predict_proba(X)[0,1]

print('input', customer)
print('subscription probablility', y_pred)
