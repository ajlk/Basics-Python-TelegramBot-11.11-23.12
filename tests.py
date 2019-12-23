import requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'London',
    'appid': 'ab302c76b17a18089e36a1ff13857e52'
}
res = requests.get(api_url, params=params)
print(res.json())
