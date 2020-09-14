import sys
#CameCase

myvar = [12, "15", 92.55, 55, True]
print(myvar, type(myvar), id(myvar), sys.getsizeof(myvar))

myvar = 12
print(myvar, type(myvar), id(myvar), sys.getsizeof(myvar))

myvar = 12.5
print(myvar, type(myvar), id(myvar), sys.getsizeof(myvar))

myvar = "12.5"
print(myvar, type(myvar), id(myvar)), sys.getsizeof(myvar)