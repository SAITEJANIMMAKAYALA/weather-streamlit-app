import requests
from config import API_KEY, BASE_URL

def get_weather(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    try:
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            return {'error': data.get('message', 'Unknown error')}
    except Exception:
        return {'error': 'Invalid response from API'}
