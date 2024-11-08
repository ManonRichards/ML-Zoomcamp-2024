# Commented out IPython magic to ensure Python compatibility.
import pickle
import kagglehub
import pandas as pd
import numpy as np
from IPython.display import display
from sklearn.metrics import mutual_info_score
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import auc
from sklearn.metrics import roc_auc_score
import seaborn as sns
from matplotlib import pyplot as plt

output = 'Mideterm_model.bin'



# Download latest version
path = kagglehub.dataset_download("shubhammeshram579/bank-customer-churn-prediction")
print("Path to dataset files:", path)

file_path = f"{path}/Churn_Modelling.csv"
df = pd.read_csv(file_path)

print('Cleaning Data')
# Don't need to keep customerid or surname
del df['CustomerId']
del df['Surname']

# Delete rows where Geography and Age has missing values
df = df.dropna(subset=['Age'])
df = df.dropna(subset=['Geography'])

df['HasCrCard'] = df['HasCrCard'].fillna(0)
df['IsActiveMember'] = df['IsActiveMember'].fillna(0)

# Lower case all column names and replace blanks with _
df.columns = df.columns.str.lower().str.replace(' ','_')

translate_values = {0: 'No', 1: 'Yes'}
df['isactivemember'] = df['isactivemember'].map(translate_values)
df['hascrcard'] = df['hascrcard'].map(translate_values)

categorical = ['geography', 'gender', 'isactivemember', 'hascrcard']
numerical = ['creditscore', 'age', 'tenure', 'balance', 'numofproducts', 'estimatedsalary']

print ('Prep Train/Val/Test')
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=11)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=11)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.exited.values
y_val = df_val.exited.values
y_test = df_test.exited.values

del df_train['exited']
del df_val['exited']
del df_test['exited']

print ('Train Model')
# Training
train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)

dicts_val = df_val.to_dict(orient='records')
X_val = dv.transform(dicts_val)

# Need a special data structure, that is specialised for XGBoost
features = list(dv.get_feature_names_out())

xgb_model = xgb.XGBClassifier(max_depth=4, learning_rate=0.05,  eval_metric='logloss')
xgb_model.fit(X_train, y_train)

y_prob_xgb = xgb_model.predict_proba(X_val)[:, 1]  # Probability of positive class
y_pred_xgb = (y_prob_xgb >= 0.5).astype(int)

roc_auc_xgb = roc_auc_score(y_val, y_prob_xgb)

print('Output AUC Score')
print("AUC Score:", roc_auc_xgb)

"""Save Model"""
with open(output, 'wb') as f_out:
    pickle.dump((dv, xgb_model), f_out)

print(f'the model is saved to {output}')
