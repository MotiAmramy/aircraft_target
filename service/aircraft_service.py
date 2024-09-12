from toolz import first
from toolz.curried import partial, get_in, pipe
from model.aircraft import Aircraft

def convert_aircraft_to_model(json):
    return [Aircraft(a["type"], a["speed"], a["fuel_capacity"]) for a in json]

