# install requests and win10toast packages

import requests
from win10toast import ToastNotifier
import json
import time

def updateNotify():
    source_api = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = source_api.json()
    text = f'Confirmed Cases: {data["cases"]} \nDeaths : {data["deaths"]} \n Recovered :{data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates", text, duration=20)
        time.sleep(60)


updateNotify()
