import os
import sys
import typing
import traceback
import threading
from database import db_session
from parameters import Parameters
from parser_metro.parser import Parser
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from convertor.from_db_to_excel import create_excel
from recipient_from_server.chromewebdriver import IWebDriver, ChromeWebDriver
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog, QMessageBox
from convertor.convertor_json import sterilization_from_parameters, deserialization_to_parameters


class Program(QMainWindow):
    def __init__(self, parameters: Parameters) -> None:
        super().__init__()
        self.__parameters = parameters

    def load_interface(self) -> None:
        uic.loadUi(self.__parameters.path_interface, self)

    def clear_database(self) -> None:
        self.__remove_folder_database(self.__parameters.path_database)

    def connect_buttons(self) -> None:
        self.button_add_url.clicked.connect(self.__add_url)
        # self.button_select_path_excel.clicked.connect(self.__select_catalog_for_excel)
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
        url, ok = QInputDialog.getText(self, "???????????????????? Url",
                                       "?????????????? url, ?????????????? ???? ???????????? ????????????????")
        result = url.replace(' ', '')
        if ok and result != '':
            self.list_urls.addItem(result)

    def __launcher(self) -> None:
        self.__save_parameters()
        if len(self.__parameters.urls) > 0:
            self.__change_enabled_buttons(False)
            thread = threading.Thread(target=self.__run_parser)
            thread.start()
        else:
            QMessageBox.critical(self, "????????????", "?????? ???????????? ?????? ????????????????", QMessageBox.Ok)

    def __run_parser(self) -> None:
        name_file = "result_parser"
        path_database = self.__parameters.path_database
        path_driver = self.__parameters.path_webdriver
        path_excel = self.__parameters.path_excel
        number_attempts_in_case_of_error = self.__parameters.number_attempts_in_case_of_error
        delay_after_error = self.__parameters.delay_after_error

        db_session.global_init(path_database + name_file + ".db")

        for number_url in range(len(self.__parameters.urls)):
            driver: IWebDriver = ChromeWebDriver(path_driver, number_attempts_in_case_of_error, delay_after_error)
            url = self.__parameters.urls[number_url]

            parser = Parser(driver, url, number_attempts_in_case_of_error, delay_after_error)
            parser.run()
            driver.close()
        create_excel(path_excel=path_excel, name=name_file)
        db_session.close_session()
        print("Parser end")

        self.__open_folder_with_excel()
        self.__remove_folder_database(path_database)
        self.__change_enabled_buttons(True)

    def __open_folder_with_excel(self) -> None:
        abspath_excel = os.path.abspath(self.__parameters.path_excel)
        os.system(f"explorer.exe {abspath_excel}")

    @staticmethod
    def __remove_folder_database(path_database: str):
        if os.path.exists(path_database):
            files = os.listdir(path_database)
            for file in files:
                os.remove(path_database + file)

    def __select_catalog_for_excel(self) -> None:
        path_excel = QFileDialog.getExistingDirectory(self, "?????????????? ?????????? ?????? ???????????????????? excel:",
                                                      self.__parameters.path_excel)
        self.__parameters.path_excel = path_excel + "/"

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
        # self.button_select_path_excel.setEnabled(condition)
        self.button_launch.setEnabled(condition)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    path_settings = "static/settings.json"
    settings = deserialization_to_parameters(path_settings)
    try:
        program = Program(settings)
        program.load_interface()
        program.load_values_interface()
        program.clear_database()
        program.connect_buttons()
        program.show()
    except:
        with open("exceptions.log", 'a', encoding='UTF') as log_file:
            traceback.print_exc(file=log_file)

    sys.exit(app.exec())
