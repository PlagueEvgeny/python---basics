lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.18',
    '19.05.19',
    '19.05.22'
]
student_marks = [
    5,
    4,
    3,
    2,
    5
]

student_2_marks = [
    4,
    3,
    5,
    5,
    4
]

for lesson_date, mark, mark_2 in zip(lesson_dates, student_marks, student_2_marks):  # ['19.05.15', 5, 4]
    # print(lesson_date, 'оценка', 'студента 1', mark, ', студента 2', mark_2)
    print(lesson_date)

curren_date = input('введите дату:\n')