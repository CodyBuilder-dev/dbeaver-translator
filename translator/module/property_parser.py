# 개선안 : input이 str type으로 들어올 때만 동작함
# input이 byte stream일때 동작하게 하려면 아키텍처 개선 필요
from django.core.files.uploadedfile import InMemoryUploadedFile

def file_to_strlines(file: InMemoryUploadedFile)-> list:
    return str(file.read()).split('\\r\\n')

def parse(full_text : list) -> dict:
    if (isinstance(full_text, InMemoryUploadedFile)):
        full_text = file_to_strlines(full_text)
    print(full_text)
    selected_text = {}
    for i, line in enumerate(full_text):
        print(line)
        if line[0] == '#' or line[0] == '\n': continue  # 주석되거나 비어이있는 줄은 생략
        property_name, property_value = line.split('=')[0].rstrip(), line.split('=')[1:]

        if len(property_value) != 1:
            raise Exception("속성값에 =이 들어가거나, 속성값이 존재하지 않습니다")
        else:
            property_value = property_value[0].lstrip().replace('\n', '')

        # 기존 line no 표기 제거
        # selected_text[property_name] = (i + 1, property_value)
        selected_text[property_name] = property_value

    return selected_text