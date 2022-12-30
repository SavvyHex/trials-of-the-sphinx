import requests

def get_questions(number:int, category:str):
    parameters = {
        "amount": number,
        "type": "multiple",
        "category": 9 if category == "gk" else 17 if category == "sci" else 0
    }

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    return response.json()["results"]