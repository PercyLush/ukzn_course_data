import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BEd SNR & FET.json"

def clean1():
    with open(path, "r") as file1:
        data = json.load(file1)

        for item in data:
            if "Name" in item:
                pattern = r"\((\d+)"
                credit = re.search(pattern, item["Name"])
                item["Credits"] = credit.group()

    with open(path, "w") as file2:
        json.dump(data, file2, indent=4)

def clean2():
    with open(path, "r") as file1:
        data = json.load(file1)

        for item in data:
            if "Name" in item:
                pattern = r"(\s*\((.+)\))"
                item["Name"] = re.sub(pattern,r"", item["Name"])
            if "Credits" in item:
                pat_cred = r"\("
                item["Credits"] = re.sub(pat_cred, r"", item["Credits"])


    with open(path, "w") as file2:
        json.dump(data, file2, indent=4)

clean1()
clean2()

