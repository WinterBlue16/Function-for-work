"""
aws translate api를 간단히 사용하는 방법이다.
아래의 코드가 동작하기 위해서는 다음의 두 가지 조건을 만족해야 한다.

1. aws 계정이 존재한다.
2. aws cli를 통한 configure를 완료했다.

"""
import boto3


def aws_translate_text(source_text, source_language, target_language):
    translation = boto3.client(
        service_name='translate', region_name='계정에 등록된 리전', use_ssl=True)
    result = translation.translate_text(
        Text=source_text, SourceLanguage=source_language, TargetLanguage=target_language)
    translated_text = result.get('TranslatedText')

    return translated_text
