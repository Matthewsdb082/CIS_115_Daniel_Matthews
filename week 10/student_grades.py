def calculate_average_grade(grades_dict):

    total = 0
    count = 0
    for grade in grades_dict.values():
        total += grade
        count += 1
        
    average = total / count
    return average

student_grades = {
"a":88,
"b":98,
"c":0

}

class_average = calculate_average_grade(student_grades)

print("class average score:", class_average)