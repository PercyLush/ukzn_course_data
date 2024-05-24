import json

def replace_key_in_dict(obj, old_key, new_key):
    """ Recursively replace all occurrences of old_key with new_key in a dictionary or list. """
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            new_obj_key = new_key if key == old_key else key
            obj[new_obj_key] = replace_key_in_dict(obj.pop(key), old_key, new_key)
    elif isinstance(obj, list):
        obj = [replace_key_in_dict(item, old_key, new_key) for item in obj]
    return obj

def update_course_prerequisites(courses, old_key, new_key):
    """ Process a list of course dictionaries to replace old_key with new_key in 'Prerequisite' """
    for course in courses:
        if 'Corequisite' in course:
            course['Corequisite'] = replace_key_in_dict(course['Corequisite'], old_key, new_key)
    return courses

# Example data, some courses may not have 'Prerequisite'
with open("C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of the Witwatersrand.json", "r", encoding="utf-8") as file1:
    courses_data = json.load(file1)


    # Key to be replaced and the new key
    old_key = "Course"
    new_key = "Code"

    # Updating course prerequisites
    updated_courses = update_course_prerequisites(courses_data, old_key, new_key)

    # Print the updated course list
with open("C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of the Witwatersrand.json", "w", encoding="utf-8") as file2:
    json.dump(courses_data, file2, indent=2)
