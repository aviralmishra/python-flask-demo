import pytest

from ..weather.weather import get_weather_forecast

def test_get_weather_forecast() -> None:
    assert get_weather_forecast({'lat': 30.2748,'lon': -97.7404}) != None



