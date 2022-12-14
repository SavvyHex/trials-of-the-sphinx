import pip
try:
    import requests
except ModuleNotFoundError:
    pip.main(["install", "requests"])
from tkinter import messagebox
import html

def get_questions_from_net(number:int, category:str):
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

def make_sense(question_raw:str):
    return html.unescape(question_raw)

def make_fair(ini_ans:float) -> float:
    ans = str(ini_ans)
    if(len(ans)>5):
        ans = ans[:5]
    return float(ans)