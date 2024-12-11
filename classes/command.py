from classes.parameter import *

class command:
    def __init__(self, gcode_command):
        self.gcode_command = gcode_command
        self.command = None
        self.parameters = None

        self.compute_gcode_command()       

    def compute_gcode_command(self):
        if self.gcode_command[0] == ";":
            self.command = "Commet"
            self.parameters = self.gcode_command[1:]
        else:
            command_tab = self.gcode_command.split(" ")
            self.command = command_tab[0]
            self.parameters = self.get_parameters(command_tab[1:])

    def get_parameters(self, tab):
        return list(map(lambda p: parameter(p), tab))
