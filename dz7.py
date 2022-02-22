a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + 0.1*a
    day += 1
print(day)