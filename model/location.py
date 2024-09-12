class Location:
    def __init__(self, city, lat, lon):
        self.city = city
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"city : {self.city}, let : {self.lat}, lon: {self.lon}"


