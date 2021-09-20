"""
IBM Watson translate api를 빠르게 사용, 테스트해볼 수 있는 예시입니다. 
해당 api를 사용하기 위해서는 다음과 같은 조건을 충족해야 합니다. 

1. IBM 계정이 존재한다.
2. translation api를 사용할 수 있는 SDK 라이브러리가 설치되어 있다. 
3. translate api key, service url이 존재한다.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url("")


def translate_text(text, model_id):
    translation = language_translator.translate(
        text=text,
        model_id=model_id
    ).get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
