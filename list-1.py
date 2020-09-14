import sys
#CameCase

#myvar = [12, "15", 92.55, 55, True]
#print(myvar, type(myvar), id(myvar), sys.getsizeof(myvar))

#myvar = 12
#print(myvar, type(myvar), id(myvar), sys.getsizeof(myvar))

#myvar = 12.5
#print(myvar, type(myvar), id(myvar), sys.getsizeof(myvar))

#myvar = "12.5"
#print(myvar, type(myvar), id(myvar)), sys.getsizeof(myvar)


marks_studet = []
while True:
    mark = input("Введите оценку студента:\n")
    if mark:
        marks_studet.append(mark)
    else:
        break

print("ввод завершен")
print(marks_studet)

mock_marks_student = ["5", "4", "3", "2", "5"]
marks_studet = mock_marks_student

i = 0
avg_mark = 0
while i < len(marks_studet):
    avg_mark += int(marks_studet[i])
    i += 1
avg_mark /= int(marks_studet)
print("Средний балл", avg_mark)
print(avg_mark)
