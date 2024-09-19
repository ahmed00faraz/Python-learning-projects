import requests

AMOUNT = 10
TYPE = "boolean"
parameters = {
    "amount": AMOUNT,
    "type": TYPE
}
# https://opentdb.com/api.php?amount=10&type=boolean
URL = "https://opentdb.com/api.php"
response = requests.get(URL, params=parameters)
response.raise_for_status()
question_data = response.json()['results']
