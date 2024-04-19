import json 
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BAData.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        pattern = r"(\s*\d+\s*Humanities)"

        if "Assessment" in item:
            item["Assessment"] = re.sub(pattern, r"", item["Assessment"])
        if "Code" in item:
            item["Code"] = re.sub(pattern, r"", item["Code"])
        if "Name" in item:
            item["Name"] = re.sub(pattern, r"", item["Name"])
        if "Content" in item:
            item["Content"] = re.sub(pattern, r"", item["Content"])
        if "Prerequisite" in item:
            item["Prerequisite"] = re.sub(pattern, r"", item["Prerequisite"])
        if "Corequisite" in item:
            item["Corequisite"] = re.sub(pattern, r"", item["Corequisite"])

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Cleaned.json", "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)