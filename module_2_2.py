first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == first or third == first or third == second:
    print(2)
elif first != second or first != third or second != first or third != first or third != second:
    print(0)