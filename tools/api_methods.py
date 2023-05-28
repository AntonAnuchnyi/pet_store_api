import requests
from tools.logger import Logger


class Methods:
    headers = {'Content-Type': 'application/json'}

    @staticmethod
    def get(url):
        Logger.add_request(url, method='GET')
        get_result = requests.get(url, headers=Methods.headers)
        Logger.add_response(get_result)
        return get_result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method='POST')
        post_result = requests.post(url, json=body, headers=Methods.headers)
        Logger.add_response(post_result)
        return post_result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method='PUT')
        put_result = requests.put(url, json=body, headers=Methods.headers)
        Logger.add_response(put_result)
        return put_result

    @staticmethod
    def delete(url):
        Logger.add_request(url, method='DELETE')
        delete_result = requests.delete(url, headers=Methods.headers)
        Logger.add_response(delete_result)
        return delete_result

