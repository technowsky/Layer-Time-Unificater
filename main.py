import sys
import os
import time
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QPushButton, QVBoxLayout, QLineEdit, QLayoutItem
from PySide6.QtCore import Qt
from classes.model import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import random

# pyinstaller -y -F -p ./classes/ -w ./main.py

#Class hierarchy:
#   model 1--->* layer
#   layer 1--->* move
#   layer 1--->* command
#   move  1--->2 command
#
#
#
#
#

class mpl_widget(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)


class main_window(QWidget):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.gcode_model = None

        #self.resize(100, 100)

        self.text_label = QLabel(text)
        self.exec_path = QLabel(str(sys.executable)+" "+str(sys.argv))
        self.close_button = QPushButton("Close")
        self.layout = QGridLayout(self)
        self.plot = mpl_widget(self, width=10, height=10, dpi=100)
        self.change_button = QPushButton("Randomize plot")
        
        self.add_button = QPushButton("/\\")
        self.down_button = QPushButton("\\/")
        self.layer_number_text_box = QLineEdit()
        self.layer_time_display = QLabel("Layer time: -")

        self.box_layout = QVBoxLayout()
        self.box_layout.addWidget(self.add_button)
        self.box_layout.addWidget(self.layer_number_text_box)
        self.box_layout.addWidget(self.down_button)

        #self.layout.addWidget(self.text_label, 0, 0, Qt.AlignCenter)

        self.layout.addWidget(self.layer_time_display, 1,0, Qt.AlignCenter)
        self.layout.addWidget(self.exec_path, 0, 0, Qt.AlignCenter)
        self.layout.addWidget(self.close_button, 3, 0)
        self.layout.addWidget(self.change_button, 3, 1)
        self.layout.addWidget(self.plot, 2, 0)
        self.layout.addLayout(self.box_layout, 2,1)
        
        #self.close_button.clicked.connect(self.restart)
        self.change_button.clicked.connect(self.display_plot)
        self.add_button.clicked.connect(self.layer_up)
        self.down_button.clicked.connect(self.layer_down)


    def layer_up(self):
        curr_layer_no = int(self.layer_number_text_box.text())
        if curr_layer_no < self.gcode_model.no_layers:
            new_layer_no = curr_layer_no + 1
            self.layer_number_text_box.setText(str(new_layer_no))
            self.display_layer(new_layer_no)

    def layer_down(self):
        curr_layer_no = int(self.layer_number_text_box.text())
        if curr_layer_no > 1:
            new_layer_no = curr_layer_no - 1
            self.layer_number_text_box.setText(str(new_layer_no))
            self.display_layer(new_layer_no)

    def closeEvent(self, event):
        sys.exit(0)

    def load_gcode(self, gcode):
        self.gcode_model = model(gcode)
        if self.gcode_model:
            #self.plot.axes([self.gcode_model.x_min, self.gcode_model.x_max, self.gcode_model.y_min, self.gcode_model.y_max])
            self.display_layer(1)
            self.layer_number_text_box.setText("1")
            
            

    def display_layer(self, layer_no):
        if self.gcode_model and len(self.gcode_model.layers) > layer_no and 0 < layer_no:
            layer = self.gcode_model.layers[layer_no]
            self.layer_time_display.setText("Layer time: "+str(layer.layer_time))

            self.plot.axes.cla()
            self.plot.axes.set_xlim(self.gcode_model.x_min-2, self.gcode_model.x_max+2)
            self.plot.axes.set_ylim(self.gcode_model.y_min-2, self.gcode_model.y_max+2)
            self.plot.axes.plot(list(map(lambda x: float(x[0]), layer.points)), list(map(lambda y: float(y[1]), layer.points)))
            self.plot.axes.set_aspect(1)
            self.plot.draw()


    def display_plot(self):
        #array_x = []
        #array_y = []
        #for i in range(5):
        #    array_x.append(random.randint(1, 100))
        #    array_y.append(random.randint(1, 100))
        #print(array_x)
        #print(array_y)
#
        #self.plot.axes.cla()
        #self.plot.axes.plot(array_x, array_y)
        #self.plot.axes.set_aspect(1)
        #self.plot.draw()

        layer = random.randint(0, len(self.gcode_model.layers))
        self.layer_number_text_box.setText(str(layer))
        self.display_layer(layer)


def get_file_content(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except: return None




if __name__ == "__main__":
    app = QApplication()
    widget = main_window(sys.argv[1])
    widget.show()
    #for name, value in os.environ.items():
    #    print("{0}: {1}".format(name, value))
    
    #print(sys.argv[1])
    widget.load_gcode(get_file_content(sys.argv[1]))
    sys.exit(app.exec())
