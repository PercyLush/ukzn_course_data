import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured(BEd).json"

with open(path, "r") as file1:
    data = json.load(file1)

    for item in data:
        item["Institution"] = "University of KwaZulu-Natal"
        if "Credits" in item:
            item["Credits"] = int(item["Credits"])

with open(path, "w") as file2:
    json.dump(data, file2, indent=4)

