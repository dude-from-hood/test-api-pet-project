from utils.http_methods import HttpMethods

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class GoogleMapsAPI:

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "https://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        return result_post

    @staticmethod
    def get_place(place_id):
        get_resourse = "/maps/api/place/get/json"
        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        result_get = HttpMethods.get(get_url)
        return result_get

    @staticmethod
    def update_place_data(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        json_for_update_place = {
                "place_id": place_id,
                "address": "Lva Tolstogo ulitsa, dom 16",
                "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_update_place)
        return result_put

    @staticmethod
    def delete_place(place_id):
        del_resource = "/maps/api/place/delete/json"
        del_url = base_url + del_resource + key
        json_for_delete_place = {
            "place_id": place_id
        }
        result_delete = HttpMethods.delete(del_url, json_for_delete_place)
        return result_delete
