from toolz import first
from toolz.curried import partial, get_in, pipe
from operator import itemgetter
from api.api_req import get_db_weather
from api.api_req import get_db_city
from model.target import Target
from repository.json_repository import read_json
from service.location_service import convert_to_location_model
from service.weather_service import convert_to_weather_model




def get_data(json):
    city = itemgetter("Target City")(json)
    location = pipe(
        city,
        get_db_city,
        lambda data: convert_to_location_model(data, city)
    )
    weather = pipe(
        city,
        get_db_weather,
        lambda data: convert_to_weather_model(data, city)
    )
    return Target(city, json["Priority"],weather, location)

def create_list_targets(json_list):
    return pipe(json_list,partial(map, get_data),list)






# def convert_target_to_model(json):
#     list_of_target = []
#     citis = [a["Target City"] for a in json]
#     priority = [a["Priority"] for a in json]
#     for i in range(15):
#         temp_weather = get_db_weather(citis[i])
#         temp_weather_model = convert_to_weather_model(temp_weather, citis[i])
#         temp_location = get_db_city(citis[i])
#         temp_location_model = convert_to_location_model(temp_location, priority[i])
#         list_of_target.append(Target(citis[i], priority[i], temp_weather_model, temp_location_model))
#
#     return list_of_target







