from toolz import first
from toolz.curried import partial, pipe

from model.weather import Weather

def convert_to_weather_model(json, location):
    current_weather = pipe(
        json["list"],
        partial(filter, lambda a : a["dt_txt"].endswith("00:00:00")),
        first
    )

    return Weather(
        location,
        current_weather["weather"][0]["main"],
        current_weather["clouds"]["all"],
        current_weather["wind"]["speed"],
        current_weather["dt_txt"]
    )





