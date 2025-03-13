from PyQt6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
)
from model.file_models import *


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Тип", "Имя", "Дата создания", "Размер", "Детали"])

        self.add_button = QPushButton("Добавить вручную")
        self.add_button.clicked.connect(self.controller.add_manually)

        self.add_from_file_button = QPushButton("Добавить из файла")
        self.add_from_file_button.clicked.connect(self.controller.add_from_file)

        self.delete_button = QPushButton("Удалить выбранную строку")
        self.delete_button.clicked.connect(self.controller.delete_selected)

        self.save_to_file_button = QPushButton("Сохранить в файл")
        self.save_to_file_button.clicked.connect(self.controller.save_to_file)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.add_from_file_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.save_to_file_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_table(self, files) -> None:
        self.table.setRowCount(len(files))
        for row, file in enumerate(files):
            self.table.setItem(row, 0, QTableWidgetItem(file.__class__.__name__))
            self.table.setItem(row, 1, QTableWidgetItem(file.name))
            self.table.setItem(row, 2, QTableWidgetItem(file.formated_creation_date))
            self.table.setItem(row, 3, QTableWidgetItem(str(file.size)))
            if isinstance(file, TxtFile):
                self.table.setItem(row, 4, QTableWidgetItem(f"Строки: {file.lines_count}, Слова: {file.words_count}"))
            elif isinstance(file, MP4File):
                self.table.setItem(row, 4, QTableWidgetItem(f"Длительность: {file.duration}, Разрешение: {file.resolution}"))
            else:
                self.table.setItem(row, 4, QTableWidgetItem(""))