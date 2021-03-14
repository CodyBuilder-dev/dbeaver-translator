def collect(file_obj) -> dict:
    full_text = file_obj.readlines()
    selected_text = {}
    for i, line in enumerate(full_text):
        if line[0] == '#' or line[0] == '\n' : continue # 주석되거나 비어이있는 줄은 생략
        property_name, property_value =  line.split('=')[0].rstrip(), line.split('=')[1:]

        if len(property_value) != 1:
            raise Exception("속성값에 =이 들어가거나, 속성값이 존재하지 않습니다")
        else :
            property_value = property_value[0].lstrip().replace('\n','')

        selected_text[property_name] = (i+1,property_value)
    return selected_text


def compare(en:dict, ko:dict) -> dict :
    missing_prop ={}
    for prop_en in en:
        if prop_en not in ko:
            missing_prop[prop_en] = en[prop_en]
    return missing_prop

f =open("bundle_ko.properties","r")
with open("bundle.properties","r") as f_en,open("bundle_ko.properties","r") as f_ko :
    en,ko = collect(f_en), collect(f_ko)

def make_tempfile(missing_prop:dict) :
    f = open("bundle_temp_ko.properties","w")
    for key,value in missing_prop.items():
        str = f"{value[0]} {key}={value[1]}\n"
        f.write(str)

    f.close()

missing_prop =compare(en,ko)
print(missing_prop)
make_tempfile(missing_prop)