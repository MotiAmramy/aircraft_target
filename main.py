from functools import partial
from idlelib.pyparse import trans
from api.api_req import get_db_weather, get_db_city
from model.aircraft import Aircraft
from model.data_source import Data_Source
from repository.json_repository import read_json
import service.weather_service as ws
import service.location_service as le
import service.aircraft_service as ais
import service.pilot_service as ps
from toolz import pipe, partial, first, second
import api.api_req as apiW
import service.target_service as ts
from service.aircraft_service import convert_aircraft_to_model
from service.pilot_service import convert_pilot_to_model

if __name__ == '__main__':
    aircraft_data = read_json("repository/aircraft.json")
    list_of_aircraft = convert_aircraft_to_model(aircraft_data)
    pilots_data = read_json("repository/pilots.json")
    list_of_pilots = convert_pilot_to_model(pilots_data)
    target_data = read_json("repository/target.json")
    full_data_weather_location = ts.create_list_targets(target_data)
    all_together = Data_Source(aircraft=list_of_aircraft, pilots=list_of_pilots, targets=full_data_weather_location)


    def create_missions(data_source):
        pipe(
            data_source,

        )
