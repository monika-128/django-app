# weather-app
weather-app


import requests
import json
API_KEY = "e7d8ba293c994bb296094927262402"
CITY = "new york"

url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
# url=f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={CITY}&dt=2026-02-24"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:", json.loads(response.text))


# response = requests.get("https://ipinfo.io/json")
# data = response.json()

# print(data)
# print("City:", data.get("city"))
# print("Region:", data.get("region"))
# print("Country:", data.get("country"))


# def get_exchange_rates(base="USD"):
#     url = f"https://open.er-api.com/v6/latest/{base}"
#     response = requests.get(url)
#     data = response.json()
#     if data.get("result") == "success":
#         return data["rates"]
#     return {}

# def convert_currency(amount, from_cc, to_cc):
#     rates = get_exchange_rates(base=from_cc)
#     rate = rates.get(to_cc)
#     if rate:
#         return amount * rate
#     return None

# print(convert_currency(1, "USD", "INR"))