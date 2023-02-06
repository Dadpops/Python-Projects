# practicepython.org
# solution 1
"""
name = input("Give me your name: ")
age = int(input("Give me your age: "))
year = 2023 + (100 - age)

print("Your name is " + name + " and you will turn 100 in the year " + str(year))
"""
# solution 2
"""
number = input("Give me a number: ")
divide = input("Give me a divider: ")
evenOdd = int(number) % 2
div4 = int(number) % 4
check = int(number) % int(divide)

if evenOdd == 0:
    if div4 == 0:
        print(number + " is a multiple of 4")
    else:
        print(number + " is Even")
else:
    print(number + " is Odd")

if check == 0:
    print(number + " is divided by " + divide)
else:
    print(number + " is not divided by " + divide)
"""
# solution 3
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
check = int(input("Give me numbers less than: "))

for element in a:
    if element < check:
        b.append(element)

print(b)
"""
# solution 4
"""
number = int(input("Give me a number: "))
numList = range(1,number)
divisors = []

for elem in numList:
    if number % int(elem) == 0:
        divisors.append(elem)
print(divisors)
"""
# solution 5
