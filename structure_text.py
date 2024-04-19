import re


def code():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\Descriptions(BA).txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"([A-Z]+\d+(.+))"
        final_data = re.sub(pattern, r"Code: \1", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BADescriptions.txt", "w", encoding="utf-8") as file2:
        file2.write(final_data)


def name():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BADescriptions.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(.+)\nCode:(.+)"
        final_data = re.sub(pattern, r"Name: \1\nCode: \2", data)

    with open(path, "w", encoding="utf-8") as file2:
        file2.write(final_data)


def description():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BADescriptions.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(Aim:)"
        final_data = re.sub(pattern, r"Description:", data)

    with open(path, "w", encoding="utf-8") as file2:
        file2.write(final_data)


def Content():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BADescriptions.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(Content:)"
        final_data = re.sub(pattern, r"Content:", data)

    with open(path, "w", encoding="utf-8") as file2:
        file2.write(final_data)


def Prerequisite():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BADescriptions.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(Prerequisite Requirement:)"
        final_data = re.sub(pattern, r"Prerequisite: ", data)

    with open(path, "w", encoding="utf-8") as file2:
        file2.write(final_data)


def DP():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\ukzn_course_data\\BADescriptions.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(DP Requirement:|DP requirement:)"
        final_data = re.sub(pattern, r"DP: ", data)

    with open(path, "w", encoding="utf-8") as file2:
        file2.write(final_data)


code()
name()
description()
Content()
Prerequisite()
DP()