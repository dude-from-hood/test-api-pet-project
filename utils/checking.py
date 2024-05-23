import json


class Checking:
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Успешно! Статус код =", result.status_code)


    @staticmethod
    def check_json_keys(result, expected_keys):
        json_response = json.loads(result.text)
        assert list(json_response) == expected_keys
        print("Все поля присутствуют")


    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!")


    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'Слово {search_word} присутствует!')
