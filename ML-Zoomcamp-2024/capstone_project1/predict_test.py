import requests

url = 'http://localhost:1911/predict'

student_id = 'MMK-191'
customer= {
            "hours_studied": 30,
          "attendance": 61,
          "parental_involvement": "High",
          "access_to_resources": "High",
          "extracurricular_activities": "No",
          "sleep_hours": 10,
          "previous_scores": 64,
          "motivation_level": "Low",
          "internet_access": "Yes",
          "tutoring_sessions": 4,
          "family_income": "Medium",
          "teacher_quality": "Medium",
          "school_type": "Public",
          "peer_influence": "Positive",
          "physical_activity": 2,
          "learning_disabilities": "No",
          "parental_education_level": "Postgraduate",
          "distance_from_home": "Moderate",
          "gender": "Male"
          }

response = requests.post(url, json=customer).json()

print(response)

if response['high score'] ==True:
    print('High Score Predicted for%s' % student_id)
else:
    print('High Score not Predicted for %s' % student_id)