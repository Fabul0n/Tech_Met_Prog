from datetime import datetime
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QDialog, QMainWindow
from pydantic import ValidationError
from enum import Enum

from model.file_models import CustomFile, TxtFile, MP4File
from model.file_parser import parse_json
from model.form_validator import validate_data
from view.add_from_file_dialog import AddFromFileDialog
from view.main_window import MainWindow



class FileController:
    def __init__(self, view):
        self.view: MainWindow = view
        self.files: list[CustomFile] = []

    def add_manually(self):
        file_types = ["TxtFile", "MP4File", "CustomFile"]
        file_type, ok = QInputDialog.getItem(self.view, "Выберите тип файла", "Тип файла:", file_types, 0, False)
        if ok and file_type:
            dialog = AddFromFileDialog(file_type, self.view)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                data = dialog.get_data()
                is_valid, error_message = validate_data(data)
                if not is_valid:
                    QMessageBox.warning(self.view, "Ошибка валидации", error_message)
                    return

                try:
                    if file_type == "TxtFile":
                        self.files.append(TxtFile(
                            name=data["name"],
                            creation_date=datetime.strptime(data["creation_date"], "%Y.%m.%d"),
                            size=int(data["size"]),
                            lines_count=int(data["lines_count"]),
                            words_count=int(data["words_count"])
                        ))
                    elif file_type == "MP4File":
                        self.files.append(MP4File(
                            name=data["name"],
                            creation_date=datetime.strptime(data["creation_date"], "%Y.%m.%d"),
                            size=int(data["size"]),
                            duration=int(data["duration"]),
                            resolution=data["resolution"]
                        ))
                    else:
                        self.files.append(CustomFile(
                            name=data["name"],
                            creation_date=datetime.strptime(data["creation_date"], "%Y.%m.%d"),
                            size=int(data["size"])
                        ))
                    self.view.update_table(self.files)
                except ValidationError as e:
                    QMessageBox.warning(self.view, "Ошибка валидации", str(e))
                except ValueError as e:
                    QMessageBox.warning(self.view, "Ошибка ввода", f"Недопустимый формат: {e}")

    def add_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self.view, "Открыть JSON файл", "", "(*.json)")
        if filename:
            self.files.extend(parse_json(filename))
            self.view.update_table(self.files)

    def delete_selected(self):
        selected_row = self.view.table.currentRow()
        if selected_row >= 0:
            self.files.pop(selected_row)
            self.view.update_table(self.files)
        else:
            QMessageBox.warning(self.view, "Внимание", "Поле не выбрано")