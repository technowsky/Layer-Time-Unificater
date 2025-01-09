from classes.command import *
import matplotlib.pyplot as plt

class layer:
    def __init__(self, gcode):
        self.gcode = gcode
        self.layer_height = self.get_layer_height()
        self.model_height = self.get_model_height()
        self.layer_time = self.calculate_layer_time()
        self.commands = self.get_commands()
        self.points = self.create_layer_points()
        self.max_x_point = float(max(map(lambda x: x[0], self.points))) if self.points else None
        self.min_x_point = float(min(map(lambda x: x[0], self.points))) if self.points else None
        self.max_y_point = float(max(map(lambda x: x[1], self.points))) if self.points else None
        self.min_y_point = float(min(map(lambda x: x[1], self.points))) if self.points else None
        #print(self.points)

        #print(self.layer_height, self. model_height)

        #print(list(map(lambda c: c.get_full_command_str() ,self.get_commands_by_name("G1")+self.get_commands_by_name("G0"))))
        #print("Max X:",self.max_x_point,"Min X:",self.min_x_point,"Max Y:",self.max_y_point,"Min Y:",self.min_y_point)

    def calculate_layer_time(self):
        #Calculate layer time from layer class. May move to layer class.
        return None

    def get_layer_height(self):
        for l in self.gcode.split("\n"):
            if ";HEIGHT" in l:
                val_name = l.split(":")
                return float(val_name[1]) if val_name else None
        return None
        
    def get_model_height(self):
        for l in self.gcode.split("\n"):
            if ";Z" in l:
                val_name = l.split(":")
                return float(val_name[1]) if val_name else None
        return None

    def get_commands(self):
        return list(map(lambda l: command(l), filter(lambda x: x!="" and x!="\n", self.gcode.split("\n"))))

    def create_layer_points(self):
        points = list(map(self.return_point, self.commands))
        points = list(filter(lambda a: a is not None and a != (None, None), points))
        for i in range(len(points)):
            if points[i][0] is None: points[i][0] = points[i-1][0]
            if points[i][1] is None: points[i][1] = points[i-1][1]
        return points

    def return_point(self, command):
        if command.command == "G1" or command.command == "G0":
            x_coord = command.get_parameter("X")
            y_coord = command.get_parameter("Y")
            point = (
                float(x_coord) if x_coord else None, 
                float(y_coord) if y_coord else None
                )
            return point
        return None

    def get_commands_by_name(self, name):
        return list(filter(lambda p: p.command.lower() == name.lower(), self.commands))

    def display_layer_moves(self):
        fig, ax = plt.subplots()
        ax.plot(list(map(lambda p: float(p[0]), self.points)), list(map(lambda p: float(p[1]), self.points)))
        plt.show()
