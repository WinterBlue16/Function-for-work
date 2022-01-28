import json
import requests

# GET


def request_get_api(api_key, url):
    """get api를 호출합니다.

    Args:
        api_key ([string]): [request 호출에 필요한 api key입니다. api key가 없을 경우 401 에러가 발생합니다.]
        url ([string]): [request를 보낼 api의 주소입니다.]

    Returns:
        [dictionary]: [api 호출 결과로 response된 json 데이터입니다.]
    """
    headers = {
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers).json()
    return response

# POST


def request_post_api(api_key, raw_data, url):
    """post api를 호출합니다. 

    Args:
        api_key ([string]): [request 호출에 필요한 api key입니다. api key가 없을 경우 401 에러가 발생합니다.]
        raw_data ([dictionary]): [post로 생성할 데이터입니다.]
        url ([string]): [request를 보낼 api의 주소입니다.]

    Returns:
        [dictionary]: [api 호출 결과로 response된 json 데이터입니다.]
    """
    headers = {
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=raw_data).json()
    return response
