import datetime
import json
import requests

now = datetime.datetime.now()
print (now.year, now.month, now.day, now.hour, now.minute, now.second)

main_api = "https://api.adviceslip.com/advice"
json_data = requests.get(main_api).json()
message = json_data["slip"]["advice"]
print("Quote of the day: " , message)

kanye_api ="https://api.kanye.rest"
json_data = requests.get(kanye_api).json()
quote = json_data["quote"]
print("Random kanye quote: ", quote)

if