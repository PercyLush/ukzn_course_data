import json 
import re

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\Stellenbosch University.json"
path2 = "C:\\Users\\Bheki Lushaba\\course-data\\sun\\descriptions24\\FMHS.json"

with open(path, "r", encoding="utf-8") as file1, open(path2, "r") as file2:
    data = json.load(file1)
    duration = json.load(file2)
    
    for item in data:
        for item2 in duration:
            if item["Code"] == item2["Code"]:
                if "Duration" in item2:
                    item["Duration"] = item2["Duration"]
                if "Period" in item2:
                    item["Period"] = item2["Period"]
        

with open(path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)