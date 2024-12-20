# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import kagglehub
import numpy as np
from IPython.display import display
from sklearn.metrics import mutual_info_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
import seaborn as sns
from matplotlib import pyplot as plt

import pickle

output = 'Capstone1_Model.bin'

# Download latest version
path = kagglehub.dataset_download("lainguyn123/student-performance-factors")
print("Path to dataset files:", path)

file_path = f"{path}/StudentPerformanceFactors.csv"
df = pd.read_csv(file_path)


# Lower case all column names and replace blanks with _
df.columns = df.columns.str.lower().str.replace(' ','_')

# Delete rows with missing values
df = df.dropna(subset=['teacher_quality'])
df = df.dropna(subset=['parental_education_level'])
df = df.dropna(subset=['distance_from_home'])

# Define high score
df['high_score'] = (df['exam_score'] >= 70).astype(int)

categorical = ['parental_involvement', 'access_to_resources', 'extracurricular_activities', 'motivation_level', 'internet_access','family_income','teacher_quality','school_type','peer_influence','learning_disabilities','parental_education_level','distance_from_home','gender']
numerical = ['hours_studied','attendance','sleep_hours','previous_scores', 'tutoring_sessions','physical_activity']

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=11)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=11)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.high_score.values
y_val = df_val.high_score.values
y_test = df_test.high_score.values

del df_train['high_score']
del df_train['exam_score']
del df_val['high_score']
del df_val['exam_score']
del df_test['high_score']
del df_test['exam_score']

train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)

dicts_val = df_val.to_dict(orient='records')
X_val = dv.transform(dicts_val)

log_reg = LogisticRegression(C=10, max_iter=1000, random_state=1)
log_reg.fit(X_train, y_train)

y_prob_log_reg = log_reg.predict_proba(X_val)[:, 1]  # Probability of positive class
y_pred_log_reg = (y_prob_log_reg >= 0.5).astype(int)

precision_log_reg = precision_score(y_val, y_pred_log_reg)
recall_log_reg = recall_score(y_val, y_pred_log_reg)
f1_log_reg = f1_score(y_val, y_pred_log_reg)
roc_auc_log_reg = roc_auc_score(y_val, y_prob_log_reg)

orig_acc = round((y_val == y_pred_log_reg).mean(),2)

print('Output AUC Score')
print("AUC Score:", roc_auc_log_reg)

print(orig_acc)

"""SAVE MODEL"""
with open(output, 'wb') as f_out:
    pickle.dump((dv, log_reg), f_out)
