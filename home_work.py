student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if mark:
        student_marks.append(int(mark))
        if int(mark) > 5:
            print("Оценка не подходит под категорию оценивания")
            student_marks.remove(int(mark))
        elif int(mark) < 1:
            print("Оценка не подходит под категорию оценивания")
            student_marks.remove(int(mark))
        elif int(mark) == 0:
            student_marks.remove(int(mark))
    else:
         break

print('ввод завершен')


#mock_student_marks = ['5', '4', '3', '2', '5']  # correct mock
#mock_student_marks = [5, 4, 3, 2, 5]  # wrong mock
#student_marks = mock_student_marks

# data processing
i = 0
avg_mark = 0
while i < len(student_marks):
    avg_mark += (student_marks[i])

    # avg_mark += student_marks[i]
    i += 1
avg_mark /= len(student_marks)
if not student_marks:
    print("Пусто")
else:
    print("Оценки", student_marks)
    print('средний балл', avg_mark)
