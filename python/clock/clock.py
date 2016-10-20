class Clock:

    def __init__(self, decimal_hours,decimal_minutes):
        self.minutes = decimal_hours*60 + decimal_minutes


    def _to_dec(self):
        decimal_hours = (self.minutes//60) % 24
        decimal_minutes = (self.minutes - (decimal_hours*60)) % 60
        return (decimal_hours, decimal_minutes)


    def add(self, y):
        self.minutes += y
        return self

    def __repr__(self):
        return("%02s:%02s" % self._to_dec())




