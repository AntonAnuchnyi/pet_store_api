from tools.api_methods import Methods
base_url = 'https://petstore.swagger.io/v2'


class PetStoreAPIPets:

    @staticmethod
    def post_new_pet():
        post_path = '/pet'
        post_url = base_url + post_path
        post_body = {
            "id": 0,
            "category": {
                "id": 1,
                "name": "dogs"
            },
            "name": "bobik",
            "photoUrls": [
                "empty"
            ],
            "tags": [
                {
                    "id": 2,
                    "name": "big"
                }
            ],
            "status": "available"
        }
        post_result = Methods.post(post_url, post_body)
        print(post_url)
        print(post_result.text)
        return post_result

    @staticmethod
    def get_pet(pet_id):
        get_path = '/pet/'
        get_url = base_url + get_path + str(pet_id)
        get_result = Methods.get(get_url)
        print(get_url)
        print(get_result.text)
        return get_result

    @staticmethod
    def update_pet(pet_id):
        put_path = '/pet'
        put_url = base_url + put_path
        put_body = {
            "id": pet_id,
            "category": {
                "id": 2,
                "name": "cats"
            },
            "name": "barsik",
            "photoUrls": [
                "empty"
            ],
            "tags": [
                {
                    "id": 3,
                    "name": "small"
                }
            ],
            "status": "available"
        }
        put_result = Methods.put(put_url, put_body)
        print(put_url)
        print(put_result.text)
        return put_result

    @staticmethod
    def delete_pet(pet_id):
        delete_path = '/pet/'
        delete_url = base_url + delete_path + str(pet_id)
        delete_result = Methods.delete(delete_url)
        print(delete_url)
        print(delete_result.text)
        return delete_result
