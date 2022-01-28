import json
import requests


def request_get_api(api_key, url):
    headers = {
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers).json()
    return response
