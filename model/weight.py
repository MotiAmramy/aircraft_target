class Weight:
    def __init__(self):
        self.weather = 0
        self.aircraft = 0
        self.pilot = 0
        self.target = 0
        self.execute_time = 0

    def calc_score(self):
        add1 = (self.aircraft + self.pilot) * 0.25
        add2 = (self.target + self.weather) * 0.20
        add3 = self.execute_time *0.10
        return add1 + add2 + add3
