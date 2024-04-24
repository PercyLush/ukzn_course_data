import json

path1 = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured(BEd).json"
path2 = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Cleaned.json"

with open(path1, "r", encoding="utf-8") as file1, open(path2, "r", encoding="utf-8") as file2:
    original_data = json.load(file1)
    duration = json.load(file2)

    for item in original_data:
        for item2 in duration:

            if "Code" in item and "Code" in item2:
                if item["Code"] == item2["Code"]:
                    if "Description" in item2:
                        item["Description"] = item2["Description"]

                    # if "Content" in item2:
                    #     item["Content"] = item2["Content"]

                    # if "Prerequisite" in item2:
                    #     item["Prerequisite"] = item2["Prerequisite"]


with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured(BEd).json", "w", encoding="utf-8") as file:
    json.dump(original_data, file, indent=4)