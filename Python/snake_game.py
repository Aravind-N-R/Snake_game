import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #setting window names and icons
        self.setWindowTitle("Snake Game")
        self.setGeometry(300, 200, 1280, 720)
        self.setWindowIcon(QIcon('Python\oimateitsasnake.jpg'))
        self.button = QPushButton("Start", self)
        #Name and styling
        label = QLabel("SNAKE GAME", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 1280, 80)
        label.setStyleSheet('color: #24fc03;' 'background-color: #000000;' 'font-weight: bold;')
        label.setAlignment(Qt.AlignCenter)
        self.initUI()

#button definitions and functionality   
    def initUI(self):
        self.button.setGeometry(600, 80, 100, 40)
        self.button.setFont(QFont("Times New Roman",20))
        self.button.setStyleSheet('background-color: #00fc43')
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.button.setGeometry(550, 80, 200, 40)
        self.button.setText("Game Start!")
        self.button.setEnabled(False)
        startgame()
    
        
        
def startgame():
    pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet('background-color: #000000')
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




