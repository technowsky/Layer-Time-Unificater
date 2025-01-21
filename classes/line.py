import math

class move:
    def __init__(self, p1, p2, speed, accel=None):
        self.distance = math.sqrt( (p2[0] - p1[0]) ** 2 + (p2[1] - p2[1]) ** 2 ) #in milimeters
        self.speed = speed #in milimeters/minute
        self.accel = accel #in milimeters/secounds/secounds
        self.time = calculate_move_time()  #in secounds

    def calculate_move_time(self):
        speed_sec = self.speed/60  #default in gcode speed is in mm/min. Conversion to mm/s
        return self.distance/speed_sec

