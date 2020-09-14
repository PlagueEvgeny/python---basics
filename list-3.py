lesson_dates = [
    "19.05.15"
    "19.05.17"
    "19.05.18"
    "19.05.19"
    "19.05.22"
]
student_marks = [5, 4, 3, 2, 5]
i = 0
while i < len(student_marks):
    print(lesson_dates[i], "оценка", student_marks[i])
    i += 1

for mark in student_marks:
    print("оценка", mark)

for item in enumerate(student_marks): # pairs -> (num, item)
    print("оценка", item,)

for mark in enumerate(student_marks): # pairs -> (num, item)
    print("оценка",i,  mark)

#user_full_name = ["Иван", "Иванов"]
#first_name = user_full_name[0]
#second_name = user_full_name [1]
#first_name, second_name = user_full_name
