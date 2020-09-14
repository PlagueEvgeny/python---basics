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

mylist = ["Огурец", "Яблоко", "Помидорка"]

print("Я должен сделать ", len(mylist), "покупок." )

print('Покупки:', end=' ')
for item in mylist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
mylist.append('рис')
print('Теперь мой список покупок таков:', mylist)

print('Отсортирую-ка я свой список')
mylist.sort()
print('Отсортированный список покупок выглядит так:', mylist)

print('Первое, что мне нужно купить, это', mylist[0])
olditem = mylist[0]
del mylist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', mylist)