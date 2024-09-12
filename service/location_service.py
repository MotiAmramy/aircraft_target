from model.location import Location


def convert_to_location_model(json, location):


    return  Location(
        location,
        json[0]["lat"],
        json[0]["lon"]
    )



