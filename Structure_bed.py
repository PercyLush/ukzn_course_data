import json
import re


def code():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BEd.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"([A-Z]+\d+)"
        final_data = re.sub(pattern, r"Code: \1\n", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BEdFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(final_data)


def name():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BEdFinal.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"Code:(.+)\n(.+)"
        final_data = re.sub(pattern, r"Code: \1\nName: \2\n", data)

    with open(path, "w", encoding="utf-8") as file2:
        file2.write(final_data)

code()
name()