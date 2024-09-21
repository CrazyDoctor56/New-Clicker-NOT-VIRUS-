from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer
from random import randint

app = QApplication([])
win = QWidget()

win.setWindowTitle("Casino")
win.resize(600, 500)

text_1 = QLabel("If you win, you get $1000")
text_num1 = QLabel("?")
text_num2 = QLabel("?")

button = QPushButton("Random 100%")
main_line = QVBoxLayout()

main_line.addWidget(text_1, alignment = Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(text_num1, alignment = Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(text_num2, alignment = Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(button, alignment = Qt.AlignmentFlag.AlignCenter)

win.setLayout(main_line)

def click():
    rand_num1 = randint(1, 10)
    text_num1.setText(str(rand_num1))
    rand_num2 = randint(1, 10)
    text_num2.setText(str(rand_num2))

    if rand_num1 == rand_num2:
        text_1.setText("YOU WON! BUT IM NOT MR BEAST, IM SCAMMER!!!")

        QTimer.singleShot(3000, app.quit)
    else:
        text_1.setText("If you win, you get $1000")

button.clicked.connect(click)

win.show()
app.exec()