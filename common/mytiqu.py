import jsonpath


def excel(excel_extract,respose,classDATA):
    """瓜瓜提醒一定记得先转换为一个字典"""
    excel_extract_dict=eval(excel_extract)

    for key,value in excel_extract_dict.items():

        result=jsonpath.jsonpath(respose,value)

        if result:

            setattr(classDATA,key,str(result[0]))


