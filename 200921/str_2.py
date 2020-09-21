#class_pupils = input("введите имена учеников через запятую: \n")

class_pupils = "Полина, Антон, Арсений, Евгений, Алексей, Тимур"
correct_result = ["Полина", "Антон", "Арсений", "Евгений", "Алексей", "Тимур"]

#print("Ученики класса:", class_pupils)

result = class_pupils.split(", ")

assert result == correct_result, 'Алгоритм реализован неверно'

print(result)