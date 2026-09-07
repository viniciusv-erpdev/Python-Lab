# Encontrar qual estudante tirou nota 100 dentro de uma lista de listas

student_info = [['Charles', 90], ['Tony', 80], ['Alex', 75], ['Jorge', 100]]

def perfect_score(student_info):

    perfect_student = []

    for student in student_info:

        if student[1] == 100:
            perfect_student.append(student)
            return perfect_student

    return perfect_student


print(perfect_score(student_info))