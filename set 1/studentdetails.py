N = int(input("Enter the number of students: "))
student_dict = {}

for i in range(N):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    total_mark = float(input("Enter total marks: "))
    student_dict[roll_no] = {'Name': name, 'Total Marks': total_mark}

highest_marks = 0
highest_marks_student = None

for roll_no, details in student_dict.items():
    if details['Total Marks'] > highest_marks:
        highest_marks = details['Total Marks']
        highest_marks_student = details

print("\nStudent with the highest total marks:")
print("Name:", highest_marks_student['Name'])
print("Roll No:", list(student_dict.keys())[list(student_dict.values()).index(highest_marks_student)])
print("Total Marks:", highest_marks)
