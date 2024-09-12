import  requests


def get_db_weather(location):
    response = requests.request("GET",api_path_for_weather(location))
    return response.json()

def get_db_city(location):
    response = requests.request("GET",api_path_for_location(location))
    return response.json()




def api_path_for_weather(weather):
    return f"https://api.openweathermap.org/data/2.5/forecast?q={weather}&appid=f3ab28e14b746b988f438b8446b1d486"


def api_path_for_location(location):
    return f"https://api.openweathermap.org/geo/1.0/direct?q={location}&appid=f3ab28e14b746b988f438b8446b1d486"



