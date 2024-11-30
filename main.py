import sys
import os
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QGridLayout
from PySide6.QtCore import Qt


class main_window(QWidget):
    def __init__(self, text):
        super().__init__()
        self.text = text

        self.resize(100, 100)

        self.text_label = QLabel(text)
        self.layout = QGridLayout(self)

        self.layout.addWidget(self.text_label, 0, 0, Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication()
    widget = main_window(sys.argv[1])
    widget.show()
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))
    sys.exit(app.exec())
