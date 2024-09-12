class Pilot:
    def __init__(self, name, skill):
        self.lat = 31.79592425
        self.lon = 35.21198075969497
        self.name = name
        self.skill = skill

    def __str__(self):
        return f"Name: {self.name}, Skill: {self.skill}"