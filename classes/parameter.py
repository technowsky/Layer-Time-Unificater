class parameter:
    def __init__(self, param_str):
        self.type = None
        self.name = None
        self.value = None
        #print(param_str)

        if "=" in param_str:
            self.type = "Klipper"
            self.name = param_str.split("=")[0]
            self.value = param_str.split("=")[1]
        else:
            self.type = "GCode"
            self.name = param_str[0]
            self.value = param_str[1:]

        #print(self.type, self.name, self.value)
    def __str__(self):
        return str(self.name)+str(self.value) if self.type == "GCode" else str(self.name)+"="+str(self.value)

