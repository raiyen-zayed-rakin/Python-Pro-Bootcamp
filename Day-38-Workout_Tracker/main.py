import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 167
AGE = 21

APP_ID = os.environ.get("NT_APP_ID")
API_KEY = os.environ.get("NT_APP_KEY")
TOKEN = os.environ.get("TOKEN")

nutrition_endpoint = "https://trackapi.nutritionix.com"

exercise_endpoint = f"{nutrition_endpoint}/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")


exercise_text = input("Tell me which exercise you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
# auth_response = requests.get('https://httpbin.org/basic-auth/rakin/rakin69', auth=('rakin', 'rakin69'))
# print(auth_response.text)
    bearer_headers = {
        "Authorization": f"Basic {TOKEN}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(sheet_response.text)
