def calculate_grade(line):
    line = line[:-1]
    list = line.split(':')
    student_name = list[0]
    grades = list[1].split(',')

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])
    average = (grade1 + grade2 + grade3)/3

    if (average >= 90) and (average <= 100):
        letter_grade = 'AA'
    elif (average >= 85) and (average < 90):
        letter_grade = 'BA'
    elif (average >= 80) and (average < 84):
        letter_grade = 'BB'
    elif (average >= 75) and (average < 79):
        letter_grade = 'CB'
    elif (average >= 70) and (average < 74):
        letter_grade = 'CC'
    elif (average >= 65) and (average < 69):
        letter_grade = 'DC'
    elif (average >= 60) and (average < 64):
        letter_grade = 'DD'
    elif (average >= 50) and (average < 59):
        letter_grade = 'FD'
    elif (average >= 0) and (average <= 49):
        letter_grade = 'FF'
    return student_name + ":"+ letter_grade +  "\n"


def read_averages():
    with open("Exam_Notes.txt","r", encoding= "utf-8") as file:
        for line in file:
            print(calculate_grade(line))


def enter_a_note():
    name = input('Student Name: ')
    surname = input('Student surname: ')
    not1 = input('Not 1: ')
    not2 = input('Not 2: ')
    not3 = input('Not 3: ')

    with open("Exam_Notes.txt", "a", encoding= "utf-8") as file:
        file.write(name+' '+surname+':'+not1+', '+not2+', '+not3+'\n')


def save_notes():
    with open("Exam_Notes.txt", "r", encoding= "utf-8") as file:
        list = []

        for i in file:
            list.append(calculate_grade(i))
        with open("results.txt", "w", encoding= "utf-8") as file2:
            for i in list:
                file2.write(i)


while True:
    print('MENU'.center(50,'*'))
    process = input('1- Read Notes\n2- Make a Not\n3- Save Notes\n4- Exit\n')

    if process == '1':
        read_averages()
    elif process == '2':
        enter_a_note()
    elif process == '3':
        save_notes()
    else:
        break
