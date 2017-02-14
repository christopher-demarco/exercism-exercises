#!/usr/bin/env python

class Clock:

    def __init__(self, decimal_hours, decimal_minutes):
        self.minutes = decimal_hours*60 + decimal_minutes

    def _to_dec(self):
        decimal_hours = (self.minutes//60) % 24
        decimal_minutes = (self.minutes - (decimal_hours*60)) % 60
        return (decimal_hours, decimal_minutes)

    def add(self, y):
        self.minutes += y
        return self

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return "%02d:%02d" % (self._to_dec())


if __name__ == '__main__':
    import sys, time
    c = Clock(0,0)
    if len(sys.argv) == 2:
        i = float(sys.argv[1])
    else:
        i = 1
    while True:
        c.add(1); print c
        time.sleep(i)

