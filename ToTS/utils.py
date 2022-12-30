import requests
from tkinter import messagebox

def get_questions(number:int, category:str):
    parameters = {
        "amount": number,
        "type": "multiple",
        "category": 9 if category == "gk" else 17 if category == "sci" else 0
    }

    try:
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    except:
        messagebox.showinfo("ERROR", "Please check your internet connection")
        exit()

    return response.json()["results"]