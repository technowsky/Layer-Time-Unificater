from classes.layer import *

class model:
    def __init__(self, gcode):
        self.info = self.get_info_from_gcode(gcode)
        #print(self.info)
        self.layers = self.get_layers_from_gcode(gcode)


    def get_info_from_gcode(self, gcode):
        #Get info about printing file from orca slicer gcode file
        #
        info_dict = {}
        info_gcode_block = gcode.split("; EXECUTABLE_BLOCK_END")[1].split("; CONFIG_BLOCK_START")[0]
        info_tab = info_gcode_block.replace("\n", "").split("; ")
        for l in info_tab:
            if " = " in l:
                l = l.replace("; ", "")
                splited = l.split(" = ")
                name = splited[0].replace(" ", "_")
                value = splited[1].replace(" ", "_")
                info_dict |= {name: value}

        return info_dict

    def get_layers_from_gcode(self, gcode):
        #Convert gcode to individual layers of print. Must write special layer class
        layer_tab = []
        exec_block = gcode.split("; EXECUTABLE_BLOCK_START")[1].split("; EXECUTABLE_BLOCK_END")[0]
        layer_gcode = exec_block.split(";LAYER_CHANGE")
        for l in layer_gcode: layer_tab.append(layer(l))
        print(len(layer_tab))
