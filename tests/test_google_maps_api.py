from utils.google_maps_api import GoogleMapsAPI
from utils.checking import Checking

import allure

@allure.epic('Test create place')
class TestCreatePlace:

    @allure.description('Test create, update, delete new place')
    def test_create_new_place(self):
        print("*Метод POST*")
        result_post = GoogleMapsAPI.create_new_place()
        Checking.check_status_code(result_post, 200)
        Checking.check_json_keys(result_post, ["status", "place_id", "scope", "reference", "id"])
        Checking.check_json_value(result_post, 'status', 'OK')

        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("*Метод GET*")
        result_get = GoogleMapsAPI.get_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_keys(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', "29, side layout, cohen 09")

        print("*Метод PUT*")
        result_put = GoogleMapsAPI.update_place_data(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_keys(result_put, ["msg"])
        Checking.check_json_value(result_put, "msg", "Address successfully updated")

        print("*Метод GET PUT*")
        result_get = GoogleMapsAPI.get_place(place_id)
        Checking.check_json_value(result_get, 'address', "Lva Tolstogo ulitsa, dom 16")

        print("*Метод DELETE*")
        result_delete = GoogleMapsAPI.delete_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_keys(result_delete, ["status"])
        Checking.check_json_value(result_delete, "status", "OK")

        print("*Метод GET DELETE*")
        result_get = GoogleMapsAPI.get_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_keys(result_get, ["msg"])
        Checking.check_json_search_word_in_value(result_get, 'msg', "doesn't exist")

        print("Тестирование класса TestCreatePlace успешно завершено!")
