from datetime import datetime
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QDialog, QMainWindow
from pydantic import ValidationError

from model.file_models import CustomFile, TxtFile, MP4File
from model.file_parser import parse_json
from view.add_from_file_dialog import AddFromFileDialog


class FileController:
    def __init__(self, view):
        self.view = view
        self.files = []

    def add_manually(self):
        file_types = ["TxtFile", "MP4File", "CustomFile"]
        file_type, ok = QInputDialog.getItem(self.view, "Select File Type", "Choose file type:", file_types, 0, False)
        if ok and file_type:
            dialog = AddFromFileDialog(file_type, self.view)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                is_valid, error_message = dialog.validate_data()
                if not is_valid:
                    QMessageBox.warning(self.view, "Validation Error", error_message)
                    return

                data = dialog.get_data()
                try:
                    if file_type == "TxtFile":
                        self.files.append(TxtFile(
                            name=data["name"],
                            creation_date=datetime.strptime(data["creation_date"], "%Y-%m-%d"),
                            size=int(data["size"]),
                            lines_count=int(data["lines_count"]),
                            words_count=int(data["words_count"])
                        ))
                    elif file_type == "MP4File":
                        self.files.append(MP4File(
                            name=data["name"],
                            creation_date=datetime.strptime(data["creation_date"], "%Y-%m-%d"),
                            size=int(data["size"]),
                            duration=int(data["duration"]),
                            resolution=data["resolution"]
                        ))
                    else:
                        self.files.append(CustomFile(
                            name=data["name"],
                            creation_date=datetime.strptime(data["creation_date"], "%Y-%m-%d"),
                            size=int(data["size"])
                        ))
                    self.view.update_table(self.files)
                except ValidationError as e:
                    QMessageBox.warning(self.view, "Validation Error", str(e))
                except ValueError as e:
                    QMessageBox.warning(self.view, "Input Error", f"Invalid input format: {e}")

    def add_from_file(self):
        filename, _ = QFileDialog.getOpenFileName(self.view, "Open JSON File", "", "JSON Files (*.json)")
        if filename:
            self.files.extend(parse_json(filename))
            self.view.update_table(self.files)

    def delete_selected(self):
        selected_row = self.view.table.currentRow()
        if selected_row >= 0:
            self.files.pop(selected_row)
            self.view.update_table(self.files)
        else:
            QMessageBox.warning(self.view, "Warning", "No item selected")