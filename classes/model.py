class model:
    def __init__(self, gcode):
        self.info = self.get_info_from_gcode(gcode)


    def get_info_from_gcode(self, gcode):
        #Get info about printing file from orca slicer gcode file
        #
        return None

    def get_layers_from_gcode(self, gcode):
        #Convert gcode to individual layers of print. Must write special layer class
        pass

    def calculate_layer_time(self, layer):
        #Calculate layer time from layer class. May move to layer class.
        pass