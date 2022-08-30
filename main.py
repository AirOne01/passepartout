#!/bin/python3
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

from src.config import ConfigLoader

class MainWindow(QMainWindow):
  label_main: QLabel

  def __init__(self) -> None:
    super().__init__()

    self.setWindowTitle("PassePartout")
    self.label_main = QLabel()
    self.label_main.setText("Hello world")

    self.setCentralWidget(self.label_main)
  
# Note: arguments can be passed down to Qt with sys.args
app = QApplication([])

window = MainWindow()
window.show()
config_loader = ConfigLoader()

if (config_loader.has_created_config):
  window.label_main.setText("HAS CREATED CONFIG")
else:
  window.label_main.setText("CONFIG ALREADY LOADED:\n{}".format(config_loader.config.get("DEFAULT", "Version")))

app.exec()