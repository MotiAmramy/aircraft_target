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



# print(ais.convert_aircraft_to_model(home3)[1])
# print(le.convert_to_location_model(home2, "Damascus"))
# print(ps.convert_pilot_to_model(home4)[1])
# print(ts.convert_target_to_model(home5))
# print(ws.convert_to_weather_model(home["Damascus"], "Damascus"))
# print(ts.create_list_targets(home5))
