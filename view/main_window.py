from PyQt6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
)
from model.file_models import *


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("File Manager")
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Type", "Name", "Creation Date", "Size", "Details"])

        self.add_button = QPushButton("Add Manually")
        self.add_button.clicked.connect(self.controller.add_manually)

        self.add_from_file_button = QPushButton("Add From File")
        self.add_from_file_button.clicked.connect(self.controller.add_from_file)

        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.controller.delete_selected)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.add_from_file_button)
        layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_table(self, files) -> None:
        self.table.setRowCount(len(files))
        for row, file in enumerate(files):
            self.table.setItem(row, 0, QTableWidgetItem(file.__class__.__name__))
            self.table.setItem(row, 1, QTableWidgetItem(file.name))
            self.table.setItem(row, 2, QTableWidgetItem(file.creation_date))
            self.table.setItem(row, 3, QTableWidgetItem(str(file.size)))
            if isinstance(file, TxtFile):
                self.table.setItem(row, 4, QTableWidgetItem(f"Lines: {file.lines_count}, Words: {file.words_count}"))
            elif isinstance(file, MP4File):
                self.table.setItem(row, 4, QTableWidgetItem(f"Duration: {file.duration}, Resolution: {file.resolution}"))
            else:
                self.table.setItem(row, 4, QTableWidgetItem(""))