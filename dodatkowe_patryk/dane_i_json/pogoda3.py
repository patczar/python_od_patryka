import json
import urllib.request
from collections import namedtuple

Weather = namedtuple('Weather', ['location', 'temperature', 'air_pressure', 'humidity', 'state'])


def get_location_id(location_name):
    with urllib.request.urlopen(f'https://www.metaweather.com/api/location/search/?query={location_name}') as f:
        results = json.loads(f.read().decode('utf-8'))
        return results[0]['woeid']


def get_location_weather(location_id):
    with urllib.request.urlopen(f'https://www.metaweather.com/api/location/{location_id}') as f:
        result = json.loads(f.read().decode('utf-8'))
        return Weather(
            location=result['title'],
            temperature=result['consolidated_weather'][0]['the_temp'],
            air_pressure=result['consolidated_weather'][0]['air_pressure'],
            humidity=result['consolidated_weather'][0]['humidity'],
            state=result['consolidated_weather'][0]['weather_state_name']
        )


if __name__ == '__main__':
    # miasto = sys.argv[1]
    miasto = 'Warsaw'
    location_id = get_location_id(miasto)
    weather = get_location_weather(location_id)
    print(f'Pogoda w {weather.location}:')
    print(f'- temperatura: {weather.temperature:.2f}°C')
    print(f'- ciśnienie: {weather.air_pressure} hPa')
    print(f'- wilgotność: {weather.humidity}%')
    print(f'- stan: {weather.state}')
