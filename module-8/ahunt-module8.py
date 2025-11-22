import json

#The purpose of this code is to demonstrate how to read from and write to a JSON file
#by loading a list of student records, adding a new student, and updating the JSON file

def print_students(students):
    """Loop through the list and print each student."""
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")


def main():
    # Load json file into a list
    with open("student.json", "r") as f:
        students = json.load(f)

    # Notifify user and print original list
    print("Printing original student list:")
    print_students(students)
    print()

    # Add new student using append()
    new_student = {
        "F_Name": "Alexander",
        "L_Name": "Hunt",
        "Student_ID": 27584,
        "Email": "ahunt@example.com"
    }
    students.append(new_student)

    # Notifify user and print updated list
    print("Updated student list:")
    print_students(students)
    print()

    # Append the new data to the json using json.dump()
    with open("student.json", "w") as f:
        json.dump(students, f, indent=4)

    # Notify user that the JSON file was updated
    print("The JSON file has been updated with the new student.")


if __name__ == "__main__":
    main()
