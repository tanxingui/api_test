import jsonpath


def excel(excel_extract,respose,classDATA):
    excel_extract_dict=eval(excel_extract)

    for key,value in excel_extract_dict.items():

        result=jsonpath.jsonpath(respose,value)

        if result:

            setattr(classDATA,key,str(result[0]))


