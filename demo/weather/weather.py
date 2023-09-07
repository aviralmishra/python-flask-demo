import datetime
import json
from urllib import request

from ..config import config

class InvalidCoordinatesError(RuntimeError):
    """Error generated if invalid Coordinates input is provided."""

def get_weather_forecast(coords):
    try:
        key = config.config['dev']['key'] 
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={key}&units=metric'
        data = json.load(request.urlopen(url))

        forecast = {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'periods': list(),
        }

        for period in data['list'][0:9]:
            forecast['periods'].append(
                {
                    'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                    'temp': round(period['main']['temp']),
                    'description': period['weather'][0]['description'].title(),
                    'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png',
                }
            )

        return forecast
    except Exception as e:
        raise InvalidCoordinatesError('Weather forecast for invalid coordinates not supported') 

