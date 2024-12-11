class parameter:
    def __init__(self, param_str):
        self.type = None
        self.name = None
        self.value = None

        if "=" in param_str:
            self.type = "Klipper"
            self.name = param_str.split("=")[0]
            self.value = param_str.split("=")[1]
        else:
            self.type = "GCode"
            self.name = param_str[0]
            self.value = param_str[1:]

        #print(self.type, self.name, self.value)

