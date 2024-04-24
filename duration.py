import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured(BEd).json"

with open(path, "r") as file1:
    data1 = json.load(file1)
    data = [
        {
            "Code": "EDNS202"
        },
        {
            "Code": "EDZU201"
        },
        {
            "Code": "EDCM410"
        },
        {
            "Code": "EDCM320"
        }
    ]
    for item in data:
        if "Code" in item:

            pattern_num = r"(\d+)"
            number = re.search(pattern_num, item["Code"])

