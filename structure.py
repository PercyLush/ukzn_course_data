import json
import re

def assessments():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BEd(Output).json"

    with open(path, "r") as file1:
        data = json.load(file1)

        for item in data:
            if "Assessment" in item:
                DATA = []
                pattern = r"([A-Za-z]+\s*\(\d+\%\)|[A-Za-z]+\s*\d+\%[A-Za-z]\:+\s*\d+\%)"
                subjects = re.findall(pattern, item["Assessment"])
                if subjects:
                    for subject in subjects:
                        mark_pattern = r"(\d+)"
                        mark_match = re.search(mark_pattern, subject)
                        mark = mark_match.group() if mark_match else 0

                        # Determine the type based on keywords in the subject
                        if "xam" in subject:
                            course_type = "Exam"
                        elif "ssign" in subject:
                            course_type = "Assignment"
                        elif "ssessment" in subject:
                            course_type = "Assessment"
                        else:
                            course_type = "Coursework"
                    # Append the data to DATA list
                    course = {"Name": subject, "Type": course_type, "Weight": mark}
                    DATA.append(course)
                else:
                    new_Data = item["Assessment"].split(";")

                    for n in new_Data:
                        Text = ""

                        name_pattern = r"([A-Za-z]+)"
                        mark_pattern = r"(\d+\%)"
                        name = re.findall(name_pattern, n)
                        mark2 = re.search(mark_pattern, n)
                        for one in name:
                            Text += f"{one} "
                        if "xam" in n:
                            type = "Exam"
                        elif "ssign" in n:
                            type = "Assignment"
                        elif "ssessment" in n:
                            type = "Assessment"
                        else:
                            type = "Coursework"

                        if mark2:
                            course = {"Name": Text.strip(), "Type": type,"Weight": mark2.group()}
                            DATA.append(course)
                        else:
                            course = {"Name": Text.strip(), "Type": type,"Weight": 0}
                            DATA.append(course)
                item["Assessment"] = DATA

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured(BEd).json", "w") as file2:
        json.dump(data, file2, indent=2)


def prerequisite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured(BEd).json"

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

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Structured(BEd).json", "w") as file:
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
#corequiresite()