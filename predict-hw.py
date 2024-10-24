import requests

url = 'https://upgraded-fishstick-q7g64x96jjq344gp-9696.app.github.dev/Q4HW'

customer_id = 'xyz-123'
client = {"job": "management", "duration": 400, "poutcome": "success"}

response = requests.post(url, json=client)

# Check if the request was successful
if response.status_code == 200:
    try:
        data = response.json()
        print(data)
        
        if data.get('subscription') == True:
            print('sending promo email to %s' % customer_id)
        else:
            print('not sending promo email to %s' % customer_id)
    except ValueError:
        print("Response content is not valid JSON:", response.text)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
