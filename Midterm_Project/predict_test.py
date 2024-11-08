import requests

url = 'http://localhost:1911/predict'

customer_id = 'xyz-123'
customer= {"age": 35.0,
           "balance": 103502.22,
           "creditscore": 852,
           "estimatedsalary": 146191.82,
           "gender": "Female",
           "geography": "France",
           "hascrcard": "Yes",
           "isactivemember": "Yes",
           "numofproducts": 3,
           "rownumber": 252,
           "tenure": 2}

response = requests.post(url, json=customer).json()

print(response)

if response['churn'] ==True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)
