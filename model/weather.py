class Weather:

    def __init__(self,location, cloud, cloud_status, wind_speed, hour):
        self.location = location
        self.cloud = cloud
        self.cloud_status = cloud_status
        self.wind_speed = wind_speed
        self.hour = hour

    def __str__(self):
        return f"location: {self.location}, cloud: {self.cloud}, cloud_status: {self.cloud_status}, wind_speed: {self.wind_speed}, hour: {self.hour}"