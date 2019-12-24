import requests
from datetime import datetime

api_url = 'http://api.openweathermap.org/data/2.5/forecast'
params = {
    'q': 'London',
    'appid': 'ab302c76b17a18089e36a1ff13857e52',
    'units': 'metric'
}
res = requests.get(api_url, params=params)
# print(res.json()['list'][0])
print(res.json()['list'][0]['main']['temp'])
print(res.json()['list'][0]['main']['humidity'])
print(res.json()['list'][0]['wind']['speed'])
print(res.json()['list'][0]['wind']['deg'])
print(res.json()['list'][0]['weather'][0]['description'])

now = datetime.now()
print(now.date())
year_then = int(res.json()['list'][0]['dt_txt'][:4])
month_then = int(res.json()['list'][0]['dt_txt'][5:7])
day_then = int(res.json()['list'][0]['dt_txt'][8:10])
then_date = datetime(year_then, month_then, day_then)
print(then_date.day)
print((then_date.date() - now.date()).days)

print(len(res.json()['list']))
print(res.json()['list'])
print(res.json()['list'][0])
print(res.json()['list'][39]['dt_txt'][11:13])
print(res.json()['list'][39]['dt_txt'])

print(res.json()['list'][0])
