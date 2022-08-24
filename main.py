print("Hello World!")

print(7 - 2) # 5
print(7 - 20) # -13
print(1.5 - 2) # -0.5
print(0.1 - 0.2) # -0.1
print(10 / 3) # 3.3333333333333335
print(10 / 2) # 5.0
print(5 * 3) # 15
print(1.5 * 3) # 4.5

if 5 > 2:
    print("5 is greater than 2")
# prints `5 is greater than 2`
if 7 > 9:
    print("7 is greater than 9")
else:
    print("7 is lower than 9 (or equal to)")
# prints `7 is lower than 9 (or equal to)`
if 3 > 3:
    print("3 is greater than 3")
elif 3 == 3:
    print("3 equals 3")
else:
    print("something else")
# prints `3 equals 3`

my_str = "Hello world!"
print(my_str)
# Hello world!
print(type(my_str))
# <class 'str'>
new_value = 2 + 5
print(new_value)
# 7
print(type(new_value))
# <class 'int'>
some_rate = 123 / 45
print("some rate", some_rate)
# some rate 2.7333333333333334
print(type(some_rate))
# <class 'float'>
