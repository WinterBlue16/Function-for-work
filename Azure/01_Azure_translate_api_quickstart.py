"""
microsoft azure translate api를 빠르게 사용, 테스트해볼 수 있는 예시입니다. 
해당 api를 사용하기 위해서는 다음과 같은 조건을 충족해야 합니다. 

1. microsoft azure 계정이 존재한다.
2. azure 리소스가 존재한다. 
3. translate api 리소스가 존재한다.
4. azure translation 라이브러리가 설치되어 있다.
"""

import requests
import uuid
import json

from requests.models import Response

source_lang = 'ko'
target_lang_list = ['en', 'ja']  # 한꺼번에 여러 언어 번역 가능


def translate_text(text, source_text, target_lang_list):
    # Add your subscription key and endpoint
    subscription_key = ""
    endpoint = ""

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Service resource.
    location = "koreancentral"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': source_lang,
        'to': target_lang_list
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more then one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(
        constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True,
          ensure_ascii=False, indent=4, separators=(',', ': ')))
