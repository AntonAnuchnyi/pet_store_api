import json
from tools.api_requests import PetStoreAPIPets
from tools.checking import Checking


class TestPetStore:

    def test_pet_1(self):
        print('POST new pet')
        post_result = PetStoreAPIPets.post_new_pet()
        Checking.check_status_code(post_result, 200)
        post_info = post_result.json()
        pet_id = post_info.get('id')
        print('New pet ID =', pet_id)
        print('GET pet info')
        get_result = PetStoreAPIPets.get_pet(pet_id)
        Checking.check_status_code(get_result, 200)
        # result_fields = json.loads(get_result.text)  # get all json keys from the body
        # print(list(result_fields))
        Checking.check_required_fields(get_result, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])
        print('UPDATE pet info')
        put_result = PetStoreAPIPets.update_pet(pet_id)
        Checking.check_status_code(put_result, 200)
        print('GET updated pet info')
        PetStoreAPIPets.get_pet(pet_id)
        print('DELETE pet')
        delete_result = PetStoreAPIPets.delete_pet(pet_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_field_value(delete_result, 'message', str(pet_id))
        print('GET deleted pet info')
        get_result = PetStoreAPIPets.get_pet(pet_id)
        Checking.check_status_code(get_result, 404)
        Checking.check_field_value(get_result, 'message', 'Pet not found')

