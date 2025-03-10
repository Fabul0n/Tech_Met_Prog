import sys
from PyQt6.QtWidgets import QApplication
from view.main_window import MainWindow
from controller.file_controller import FileController


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = FileController(None)
    view = MainWindow(controller)
    controller.view = view
    view.show()
    sys.exit(app.exec())