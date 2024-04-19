import json

path1 = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of KwaZulu-Natal.json"
path2 = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\StructuredData.json"

with open(path1, "r", encoding="utf-8") as file1, open(path2, "r", encoding="utf-8") as file2:
    original_data = json.load(file1)
    descriptions = json.load(file2)

    for item in original_data:
        for item2 in descriptions:

            if "Code" in item and "Code" in item2:
                if item["Code"] == item2["Code"]:
                    if "Assessment" in item2:
                        item["Assessment"] = item2["Assessment"]
                    if "Content" in item2:
                        item["Description"] = item2["Content"]
                    if "Prerequisite" in item2:
                        item["Prerequisite"] = item2["Prerequisite"]
                    if "Corequisite" in item2:
                        item["Corequisite"] = item2["Corequisite"]
                    if "DP" in item2:
                        item["DP"] = item2["DP"]

with open(path1, "w", encoding="utf-8") as file:
    json.dump(original_data, file, indent=4)