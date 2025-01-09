from classes.parameter import *

class command:
    def __init__(self, gcode_command):
        #print(gcode_command)
        self.gcode_command = gcode_command
        self.command = None
        self.parameters = None
        self.comment = None

        self.compute_gcode_command()  
        #if self.command == "G1" or self.command == "G0":
        #    print(self.command, self.parameters)

    def compute_gcode_command(self):
        command_tab = []
        try: comm_idx = self.gcode_command.index(";")
        except ValueError: comm_idx = None

        if comm_idx and comm_idx != 0:
            self.comment = self.gcode_command[comm_idx:]
            self.command = self.gcode_command[:comm_idx]
            command_tab = self.command.split(" ")
        elif comm_idx and comm_idx == 0:
            self.comment = self.gcode_command
            return
        else:
            command_tab = self.gcode_command.split(" ")
            self.command = command_tab[0]
        
        command_tab = list(filter(lambda a: a != '', command_tab))
        #print(command_tab)
        self.parameters = self.get_parameters(command_tab[1:]) if len(command_tab) > 1 else None
        #print(command_tab)

        #print(self.comment, self.command)

    def get_parameters(self, tab):
        return list(map(lambda p: parameter(p), tab))

    def get_parameter(self, name):
        if self.parameters:
            for p in self.parameters:
                if p.name.lower() == name.lower():
                    return p.value
        else:
            return None

    def __str__(self):
        parameters_str = ""
        for p in self.parameters:
            parameters_str += " "+str(p.name)+str(p.value)
        return str(self.command)+str(parameters_str)


