from toolz import first
from toolz.curried import partial, get_in, pipe
from model.pilot import Pilot


def convert_pilot_to_model(json):
    return [Pilot(a["name"], a["skill"]) for a in json]

