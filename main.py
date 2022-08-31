#!/bin/python3
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from src.config import ConfigLoader

class MainWidget(QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.initUI()

  def initUI(self) -> None:
    vbox = QGridLayout()

    title = TitleWidget()
    title.setFixedHeight(70)
    vbox.addWidget(title)

    self.setLayout(vbox)

class TitleWidget(QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.initUI()

  def initUI(self) -> None:
    label_main = QLabel()
    label_main.setFont(QFont('Times font', 20))
    label_main.setText("PassePartout")
    # label_main.setFixedHeight(50)
    label_submain = QLabel('Arial')
    label_submain.setText("Yout multi-tool for managing bootable ISOs")
    # label_submain.setFixedHeight(10)

    vbox = QGridLayout()

    vbox.addWidget(label_main)
    vbox.addWidget(label_submain)

    self.setLayout(vbox)

class MainWindow(QMainWindow):
  def __init__(self) -> None:
    super().__init__()
    self.initUI()

  def initUI(self) -> None:
    self.setWindowTitle("PassePartout")
    self.setCentralWidget(MainWidget())

# Note: arguments can be passed down to Qt with sys.args
app = QApplication([])

window = MainWindow()
window.show()
config_loader = ConfigLoader()

app.exec()