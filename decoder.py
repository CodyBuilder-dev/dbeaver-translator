
test_str = "presentation.spreadsheet.description = \uC2A4\uD504\uB808\uD2B8\uC2DC\uD2B8 \uD615\uD0DC\uB85C \uCFFC\uB9AC \uACB0\uACFC \uCD9C\uB825"

f = open("property_kor_encode", "r", encoding="utf8")
t_str = f.readline()
f.close()

def decoder_all(text: str) -> str :
    # return text.split("\\u")
    text_list =text.split("\\u")
    # return text_list
    new_text_list =[]
    new_text_list.append(text_list[0]) # 속성명
    for word in text_list[1:]:
        if len(word) == 4 : # 띄어쓰기 미포함
            new_word = "\\u"+word
            new_text_list.append(new_word.encode().decode('unicode-escape'))
        else : # 띄어쓰기 포함
            new_word = "\\u" + word[:-1]
            new_text_list.append(new_word.encode().decode('unicode-escape'))
            new_text_list.append(' ')
    return ''.join(new_text_list)

def extract_utf(text: str) -> str:
    utf_list = text.split('\\u')[1:]
    new_list = []
    for word in utf_list:
        if len(word) == 4 : # 띄어쓰기 미포함
            new_word = "\\u"+word
            new_list.append(new_word.encode().decode('unicode-escape'))
        else : # 띄어쓰기 포함
            new_word = "\\u" + word[:-1]
            new_list.append(new_word.encode().decode('unicode-escape'))
            new_list.append(' ')
    return ''.join(new_list)

print(extract_utf(t_str))
