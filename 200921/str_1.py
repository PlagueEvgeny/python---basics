a = 'Привет всем'
#print(type(a))
#print(dir(a))

print(a.isdigit())

b = "15.7"
print(b.isdigit())

c = "157"
print(c.isdigit())

d = "15e6"
print(d.isdigit())

r = "1500000"
print(r.isdigit())


avg_mark = input("Введите средний балл студента\n")

try:
    avg_mark = float(avg_mark)
    print("Ввод корректен", type(avg_mark), avg_mark)
except ValueError:
    print("Ввод некорректен", avg_mark)
