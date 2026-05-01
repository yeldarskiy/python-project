students = {}

def add_student(name, grades):
    students[name] = grades
    print(f"{name} қосылды!")

def average_grade(name):
    grades = students[name]
    avg = sum(grades) / len(grades)
    print(f"{name} орташа балы: {avg:.2f}")

def show_all():
    print("\n--- Барлық студенттер ---")
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        print(f"{name}: {grades} | Орташа: {avg:.2f}")

add_student("Асель", [85, 90, 78, 92])
add_student("Берік", [70, 65, 80, 75])
add_student("Дана", [95, 88, 91, 97])

average_grade("Асель")
average_grade("Берік")
show_all()