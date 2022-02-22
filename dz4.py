n = int(input("Enter any positive integer"))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    elif n > 9:
        pass
print("Максимальное цифра в числе ", max)
