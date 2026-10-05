# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.append("Sara")
students.append("Miko")

# function to print 'Hi name' for each student in the list and show the total count
def greet_students(student_list):
    print(f"Total students: {len(student_list)}")
    for name in student_list:
        print(f"Hi {name}")

# call the function
greet_students(students)

# change Jon to John
students[0] = 'John'

