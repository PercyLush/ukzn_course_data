import json
import re

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University Of Western Cape.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
          if "Code" in item:
            if " " in item["Code"]:
                print(item["Code"])

# with open(path, "w", encoding="utf-8") as file2:
#      json.dump(data, file2, indent= 2)
