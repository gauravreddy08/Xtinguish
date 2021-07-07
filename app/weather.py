
import requests

def get_weather(API_KEY):
    r = requests.get('https://get.geojs.io/v1/ip.json')
    ip_add = r.json()['ip']

    # Geo Location
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_req = requests.get(url)
    lon, lat = geo_req.json()['longitude'], geo_req.json()['latitude']

    # Weather Conditions
    x = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=' + API_KEY)
    weather_data = x.json()

    loc = weather_data['name']
    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    hum = weather_data['main']['humidity']
    wind_dir = weather_data['wind']['deg']
    wind_speed = weather_data['wind']['speed']
    return loc, weather, temp, hum, wind_dir, wind_speed

def get_time(API_KEY):
    r = requests.get('https://get.geojs.io/v1/ip.json')
    ip_add = r.json()['ip']

    # Geo Location
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_req = requests.get(url)
    lon, lat = geo_req.json()['longitude'], geo_req.json()['latitude']

    # Weather Conditions
    x = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=' + API_KEY)
    weather_data = x.json()

    time = weather_data['dt']
    sunrise = weather_data['sys']['sunrise']
    sunset = weather_data['sys']['sunset']

    if(time>=sunrise and time<=sunset): return "Day"
    return "Night"