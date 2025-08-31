student_name = input("Enter student name: ")

subjects = input("Enter subjects to enroll (separated by commas): ")

subject_list = [subject.strip() for subject in subjects.split(",")]

print(f"{student_name} enrolled in the following subjects:")
for subject in subject_list:
    print(f"- {subject}")
