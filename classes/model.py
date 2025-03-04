from classes.layer import *

class model:
    def __init__(self, gcode):
        self.info = self.get_info_from_gcode(gcode)
        #print(self.info)
        self.x_min = 100000000
        self.x_max = -100000000
        self.y_min = 100000000
        self.y_max = -100000000

        self.layers = self.get_layers_from_gcode(gcode)
        self.no_layers = len(self.layers)

        #print(self.layers[1].points)
        #print(self.layers[1].max_x_point, self.layers[1].min_x_point, self.layers[1].max_y_point, self.layers[1].min_y_point)

        #print("Max X:",self.x_max,"Min X:",self.x_min,"Max Y:",self.y_max,"Min Y:",self.y_min)

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
        prev_layer = None
        next_layer = None
        layer_tab = []
        exec_block = gcode.split("; EXECUTABLE_BLOCK_START")[1].split("; EXECUTABLE_BLOCK_END")[0]
        layer_gcode = exec_block.split(";LAYER_CHANGE")
        for index, l in enumerate(layer_gcode):
            new_layer = layer(l, index)
            if new_layer:
                new_layer.prev_layer = prev_layer
                if prev_layer: prev_layer.next_layer = new_layer
                prev_layer = new_layer
            layer_tab.append(new_layer)
            
            if new_layer and new_layer.points:
                if new_layer.max_x_point > self.x_max: self.x_max = new_layer.max_x_point
                if new_layer.min_x_point < self.x_min: self.x_min = new_layer.min_x_point
                if new_layer.max_y_point > self.y_max: self.y_max = new_layer.max_y_point
                if new_layer.min_y_point < self.y_min: self.y_min = new_layer.min_y_point
        return layer_tab
