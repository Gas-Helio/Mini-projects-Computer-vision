import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog
from angle import Angle


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Angle Finder")
        btn = QPushButton("Abrir imagem")
        layout = QVBoxLayout()
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        btn.clicked.connect(self.open)
        self.show()

    def open(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            Angle(path[0]).run()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
