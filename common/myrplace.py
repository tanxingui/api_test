from faker import Faker
import time
import re

from common.phone import get_random_phone


def replace_case_with_re(case_dict, Data):
    case_str = str(case_dict)
    replaced_list = re.findall("#(\w+)#",case_str)

    if replaced_list:
        # 如果有random_str，则要生成一个随机数，然后再替换掉它
        if "random_str" in replaced_list:
            # 生成随机数：今天的日期_20个随机字母
            cur_time = time.strftime("%Y%m%d",time.localtime())
            cur_str = Faker().pystr()
            random_str = cur_time + "_" + cur_str
            case_str = case_str.replace("#random_str#", random_str)
        if "phone" in replaced_list:
            new_phone=get_random_phone()
            case_str=case_str.replace("#phone#",new_phone)

        for mark in replaced_list:

            if hasattr(Data, mark):
                case_str = case_str.replace(f"#{mark}#", getattr(Data, mark))
    new_case_dict = eval(case_str)
    return new_case_dict
