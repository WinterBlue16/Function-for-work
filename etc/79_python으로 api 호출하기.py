import json
import requests

# GET


def request_get_api(api_key, url):
    headers = {
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers).json()
    return response

# POST


def request_post_api(api_key, raw_data, url):
    headers = {
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=raw_data).json()
    return response
