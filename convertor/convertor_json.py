import json
from parameters import Parameters


def sterilization_from_parameters(path_json, parameters: Parameters) -> None:
    data: dict = {
        "urls": parameters.urls,
        "number_attempts_in_case_of_error": parameters.number_attempts_in_case_of_error,
        "delay_after_error": parameters.delay_after_error,
        "hide_browser": parameters.hide_browser,
        "path_database": parameters.path_database,
        "path_excel": parameters.path_excel,
        "path_webdriver": parameters.path_webdriver,
        "path_interface": parameters.path_interface
    }
    with open(path_json, 'w', encoding='UTF') as write_file:
        json.dump(data, write_file, ensure_ascii=False)


def deserialization_to_parameters(path_json) -> Parameters:
    with open(path_json, "r", encoding='UTF') as read_file:
        data = json.load(read_file)
        return Parameters(data)
