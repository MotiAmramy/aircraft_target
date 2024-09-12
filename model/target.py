from imghdr import tests


class Target:
    def __init__(self, target_City, priority, location, weather):
        self.target_City = target_City
        self.priority = priority
        self.location = location
        self.weather = weather


    def __str__(self):
        return f"target_city: {self.target_City}, priority : {self.priority}"
