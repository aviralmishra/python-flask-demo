import pytest

from ..weather.weather import get_weather_forecast, InvalidCoordinatesError

def test_get_weather_forecast() -> None:
    assert len(get_weather_forecast({'lat': 30.2748,'lon': -97.7404})['periods']) == 9

def test_get_weather_forecast_invalid() -> None:
    with pytest.raises(InvalidCoordinatesError):
        assert get_weather_forecast({'lat': 123,'lon': 987})

