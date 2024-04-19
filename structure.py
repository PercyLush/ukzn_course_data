import json
import re

def assessments():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BA PPL.json"

    with open(path, "r") as file1:
        data = json.load(file1)

        for item in data:
            if "Assessment" in item:
                DATA = []
                new_data = re.split(",| ;", item["Assessment"].strip())
                pattern_name = r"([A-z]+)"
                pattern_mark = r"(\d+\)%|\d+%)"
                for n in new_data:
                    Text = ""
                    name = re.findall(pattern_name, n)
                    mark = re.search(pattern_mark, n)
                    for i in name:
                        Text += f"{i} "

                    if "Exam" in Text:
                        if mark:
                            assessment = {"Name": Text.strip(), "Type": "Exam","Weight": mark.group()}
                            DATA.append(assessment)
                        else:
                            assessment = {"Name": Text.strip(), "Type": "Exam","Weight": 0}
                            DATA.append(assessment)
                    else:
                        if mark:
                            assessment = {"Name": Text.strip(), "Type": "Coursework","Weight": mark.group(), "Dynamic": True}   
                            DATA.append(assessment)
                        else:
                            assessment = {"Name": Text.strip(), "Type": "Coursework","Weight": 0, "Dynamic": True}   
                            DATA.append(assessment)
                item["Assessment"] = DATA
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured.json", "w") as file2:
        json.dump(data, file2, indent=2)

def prerequisite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured.json"

    with open(path, "r") as file:
        data = json.load(file)

    for item in data:
        if "Prerequisite" in item:
            prerequisites_text = item["Prerequisite"]
            # Split by ',' or ' and ', treated as logical AND
            prerequisites_list = re.split(',| and ', prerequisites_text.strip())
            and_data = []

            for prerequisite in prerequisites_list:
                mark = re.search(r"(\d{2})%", prerequisite)
                mark_value = mark.group() if mark else None
                # Handle 'or' conditions within each 'and' split segment
                if ' or ' in prerequisite:
                    or_split = prerequisite.split(' or ')
                    or_data = []
                    for part in or_split:
                        code_match = re.search(r"([A-Z]+\d+[A-Z]*\d*)", part.strip())
                        if code_match:
                            if mark_value:
                                or_data.append({"Code": code_match.group().strip(), "Mark": mark_value})
                            else:
                                or_data.append({"Code": code_match.group().strip()})
                    if or_data:
                        and_data.append({"$or": or_data})
                else:
                    # Direct code matches without 'or'
                    codes = re.findall(r"([A-Z]+\d+[A-Z]*\d*)", prerequisite)
                    for code in codes:
                        if mark_value:
                            and_data.append({"Code": code, "Mark": mark_value})
                        else:
                            and_data.append({"Code": code})

            # Wrap all conditions into a single "$and" if there are multiple conditions
            if len(and_data) > 1:
                item["Prerequisite"] = {"$and": and_data}
            elif len(and_data) == 1:
                item["Prerequisite"] = and_data[0]  # Only one condition, no need for $and wrapper
            else:
                item["Prerequisite"] = [{"Comment": item["Prerequisite"]}]

    with open("BA(PPL).json", "w") as file:
        json.dump(data, file, indent=4)

def corequiresite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BA(PPL).json"

    with open(path, "r") as file:
        data = json.load(file)

    for item in data:
        if "Corequisite" in item:
            prerequisites_text = item["Corequisite"]
            # Split by ',' or ' and ', treated as logical AND
            prerequisites_list = re.split(',| and ', prerequisites_text.strip())
            and_data = []

            for prerequisite in prerequisites_list:
                mark = re.search(r"(\d{2})%", prerequisite)
                mark_value = mark.group() if mark else None
                # Handle 'or' conditions within each 'and' split segment
                if ' or ' in prerequisite:
                    or_split = prerequisite.split(' or ')
                    or_data = []
                    for part in or_split:
                        code_match = re.search(r"([A-Z]+\d+[A-Z]*\d*)", part.strip())
                        if code_match:
                            if mark_value:
                                or_data.append({"Code": code_match.group().strip(), "Mark": mark_value})
                            else:
                                or_data.append({"Code": code_match.group().strip()})
                    if or_data:
                        and_data.append({"$or": or_data})
                else:
                    # Direct code matches without 'or'
                    codes = re.findall(r"([A-Z]+\d+[A-Z]*\d*)", prerequisite)
                    for code in codes:
                        if mark_value:
                            and_data.append({"Code": code, "Mark": mark_value})
                        else:
                            and_data.append({"Code": code})

            # Wrap all conditions into a single "$and" if there are multiple conditions
            if len(and_data) > 1:
                item["Corequisite"] = {"$and": and_data}
            elif len(and_data) == 1:
                item["Corequisite"] = and_data[0]  # Only one condition, no need for $and wrapper
            else:
                item["Corequisite"] = [{"Comment": item["Corequisite"]}]

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BA(PPL).json", "w") as file:
        json.dump(data, file, indent=4)



assessments()
prerequisite()
corequiresite()