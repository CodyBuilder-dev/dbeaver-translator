f = open("property_kor", "r", encoding="utf8")
t_str = f.readline()
f.close()

def encoder(text: str) -> str:
    # 메뉴명에 = 가 들어가지 않는다는 가정 하에
    property_name, value = text.split("=")[0],text.split("=")[1:]
    if len(value) > 1:
        raise Exception("메뉴명 텍스트에 =가 들어가 있습니다")
    if len(value) == 0 :
        raise Exception("속성값이 없습니다")

    value = ''.join(value).split()
    new_text = []
    for word in value:
        new_text.append(word.encode('unicode-escape').decode())

    return property_name + '= ' + ' '.join(new_text)

print(encoder(t_str))