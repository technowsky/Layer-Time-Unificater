from classes.command import *

class layer:
    def __init__(self, gcode):
        self.gcode = gcode
        self.layer_height = self.get_layer_height()
        self.model_height = self.get_model_height()
        self.layer_time = self.calculate_layer_time()
        self.commands = self.get_commands()

        #print(self.layer_height, self. model_height)


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
        ...
