import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://93516964-1c56-45fc-bb66-631928572b4c.eastus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "FW4zMl0mwblO9KIe265ceRNWpymBtheR"

# Two sets of data to score, so we get two results back
data = {
    "data":
    [
         {
            'age': 39,
            'job': "management",
            'marital': "married",
            'education': "university.degree",
            'default': "no",
            'housing': "yes",
            'loan': "no",
            'contact': "telephone",
            'month': "nov",
            'day_of_week': "wed",
            'duration': 204,
            'campaign': 1,
            'pdays': 3,
            'previous': 0,
            'poutcome': "success",
            'emp.var.rate': -0.1,
            'cons.price.idx': 93.2,
            'cons.conf.idx': -42,
            'euribor3m': 4.633,
            'nr.employed': 5195.8
        },
        
        {
            "age": 27,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 400,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },
    ],
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())