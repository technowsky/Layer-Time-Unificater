import sys
import os
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QGridLayout
from PySide6.QtCore import Qt

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

class main_window(QWidget):
    def __init__(self, text):
        super().__init__()
        self.text = text

        self.resize(100, 100)

        self.text_label = QLabel(text)
        self.layout = QGridLayout(self)

        self.layout.addWidget(self.text_label, 0, 0, Qt.AlignCenter)

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
    
    print(sys.argv[1])
    print(get_file_content(sys.argv[1]))
    sys.exit(app.exec())
