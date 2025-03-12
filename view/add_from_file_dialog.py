from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
from enum import Enum

class Fields(Enum):
    name = 'Название файла'
    creation_date = 'Дата создания'
    size = 'Размер'
    words_count = 'Количество слов'
    lines_count = 'Количество строк'
    duration = 'Длительность'
    resolution = 'Разрешение'


class AddFromFileDialog(QDialog):
    def __init__(self, file_type, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Добавить {file_type}")
        self.file_type = file_type

        self.name_input = QLineEdit()
        self.creation_date_input = QLineEdit()
        self.size_input = QLineEdit()

        self.lines_count_input = QLineEdit()
        self.words_count_input = QLineEdit()

        self.duration_input = QLineEdit()
        self.resolution_input = QLineEdit()

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow("Название файла:", self.name_input)
        layout.addRow("Дата создания (гггг.мм.дд):", self.creation_date_input)
        layout.addRow("Размер:", self.size_input)

        if file_type == "TxtFile":
            layout.addRow("Количество строк:", self.lines_count_input)
            layout.addRow("Количество слов:", self.words_count_input)
        elif file_type == "MP4File":
            layout.addRow("Длительность:", self.duration_input)
            layout.addRow("Разрешение (н-р, 1920x1080):", self.resolution_input)

        layout.addWidget(self.button_box)
        self.setLayout(layout)

    def get_data(self):
        data = {
            "name": self.name_input.text(),
            "creation_date": self.creation_date_input.text(),
            "size": self.size_input.text(),
        }
        if self.file_type == "TxtFile":
            data["lines_count"] = self.lines_count_input.text()
            data["words_count"] = self.words_count_input.text()
        elif self.file_type == "MP4File":
            data["duration"] = self.duration_input.text()
            data["resolution"] = self.resolution_input.text()
        return data

    def validate_data(self):
        data = self.get_data()
        for key, value in data.items():
            if not value:
                return False, f"Поле '{Fields[key].value}' не может быть пустым."
        return True, ""