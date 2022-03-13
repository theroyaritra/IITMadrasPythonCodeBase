class Time:
    def __init__(self, time):
        self.time = time
    def seconds_to_minutes(self):
        self.minutes = self.time // 60
        self.seconds = self.time % 60
        return f'{self.minutes} min {self.seconds} sec'

    def seconds_to_hours(self):
        self.seconds_to_minutes()
        self.hours = self.minutes // 60
        self.minutes = self.minutes % 60
        return f'{self.hours} hrs {self.minutes} min {self.seconds} sec'

    def seconds_to_days(self):
        self.seconds_to_hours()
        self.days = self.hours // 24
        self.hours = self.hours % 24
        return f'{self.days} days {self.hours} hrs {self.minutes} min {self.seconds} sec'        
