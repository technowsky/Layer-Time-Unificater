from classes.command import *
import matplotlib.pyplot as plt

class layer:
    def __init__(self, gcode, l_num):
        self.layer_number = l_num
        self.prev_layer = None
        self.next_layer = None
        self.gcode = gcode
        self.layer_height = self.get_layer_height()
        self.model_height = self.get_model_height()
        self.layer_time = self.calculate_layer_time()
        self.layer_time = self.model_height
        self.commands = self.get_commands()
        self.default_speed = None
        self.points = self.create_layer_points()
        self.moves = self.get_moves()
        self.max_x_point = float(max(map(lambda x: x[0], self.points))) if self.points else None
        self.min_x_point = float(min(map(lambda x: x[0], self.points))) if self.points else None
        self.max_y_point = float(max(map(lambda x: x[1], self.points))) if self.points else None
        self.min_y_point = float(min(map(lambda x: x[1], self.points))) if self.points else None

    def calculate_layer_time(self):
        #Calculate layer time from layer class. May move to layer class.
        ...


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
        commands = list(map(lambda l: command(l), filter(lambda x: x!="" and x!="\n", self.gcode.split("\n"))))
        return commands

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

    def get_moves(self):
        for i in range(len(self.commands)-1):
            p1 = self.return_point(self.commands[i])
            p2 = self.return_point(self.commands[i+1])
