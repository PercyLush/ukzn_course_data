import json

def make_prerequisite_same():
    path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\Stellenbosch University.json"

    with open(path, "r") as file1:
        data = json.load(file1)

        for item in data:
            # Ensure Prerequisite exists and is not None
            if "Prerequisite" in item and item["Prerequisite"]:
                # If there is more than one prerequisite, wrap them in a $and condition
                if len(item["Prerequisite"]) > 1:
                    item["Prerequisite"] = [{"$and": item["Prerequisite"]}]

    with open(path, "w") as file2:
        json.dump(data, file2, indent=2)

def standardize():
    path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\Stellenbosch University.json"
    
    with open(path, "r") as file1:
        data = json.load(file1)

        for item in data:
            if "Prerequisite" in item and item["Prerequisite"]:
                # If there is exactly one prerequisite, extract it from the list
                if len(item["Prerequisite"]) == 1:
                    item["Prerequisite"] = item["Prerequisite"][0]

    with open(path, "w") as file2:
        json.dump(data, file2, indent=2)

make_prerequisite_same()
standardize()
