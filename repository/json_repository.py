from logging import exception

from model.aircraft import Aircraft
from model.pilot import Pilot
import json
from logging import exception

def read_json(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except exception as e:
        print(e)
        return []

def convert_from_json_to_aircraft(json):
    return Aircraft(type= json["type"],
                    speed=json["speed"],
                    fuel_capacity=json["fuel_capacity"])


def convert_from_json_to_pilot(json):
    return Pilot(name=json["name"],
                    skill=json["skill"])



