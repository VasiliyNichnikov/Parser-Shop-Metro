import sys
import typing

from PyQt5 import QtWidgets, uic, QtGui, QtCore
from convertor.convertor_json import sterilization_from_parameters, deserialization_to_parameters
from parameters import Parameters
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog


class Program(QMainWindow):
    def __init__(self, parameters: Parameters) -> None:
        super().__init__()
        self.__parameters = parameters

    def load_interface(self) -> None:
        uic.loadUi(self.__parameters.path_interface, self)

    def connect_buttons(self) -> None:
        self.button_add_url.clicked.connect(self.__add_url)
        self.button_select_path_excel.clicked.connect(self.__select_catalog_for_excel)
        self.button_launch.clicked.connect(self.__launcher)

    def load_values_interface(self) -> None:
        for url in self.__parameters.urls:
            self.list_urls.addItem(url)
        self.number_attempts_in_case_of_error.setValue(self.__parameters.number_attempts_in_case_of_error)
        self.delay_after_error.setValue(self.__parameters.delay_after_error)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_Backspace or event.key() == QtCore.Qt.Key_Delete:
            self.__remove_selected_item()

    def __remove_selected_item(self) -> None:
        selected_items = self.list_urls.selectedItems()
        if selected_items is not None and len(selected_items) > 0:
            selected_item = selected_items[0]
            index_selected_item = self.list_urls.row(selected_item)
            self.list_urls.takeItem(index_selected_item)

    def __add_url(self) -> None:
        url, ok = QInputDialog.getText(self, "Добавление Url",
                                       "Введите url, который вы хотите добавить")
        result = url.replace(' ', '')
        if ok and result != '':
            self.list_urls.addItem(result)

    def __launcher(self) -> None:
        self.__save_parameters()

    def __select_catalog_for_excel(self) -> None:
        path_excel = QFileDialog.getExistingDirectory(self, "Выбрать папку для сохранения excel:",
                                                      self.__parameters.path_excel)
        self.__parameters.path_excel = path_excel

    def __save_parameters(self) -> None:
        self.__parameters.number_attempts_in_case_of_error = self.number_attempts_in_case_of_error.value()
        self.__parameters.delay_after_error = self.delay_after_error.value()
        urls: typing.List[str] = []
        for index in range(self.list_urls.count()):
            url = self.list_urls.item(index).text()
            urls.append(url)
        self.__parameters.urls = urls
        sterilization_from_parameters(path_settings, self.__parameters)

    def __change_enabled_buttons(self, condition: bool):
        self.button_add_url.setEnabled(condition)
        self.button_select_path_excel.setEnabled(condition)
        self.button_launch.setEnabled(condition)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    path_settings = "static/settings.json"
    settings = deserialization_to_parameters(path_settings)

    program = Program(settings)
    program.load_interface()
    program.load_values_interface()
    program.connect_buttons()
    program.show()

    sys.exit(app.exec())
