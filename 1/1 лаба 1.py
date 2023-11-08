num = int(input("Введите натуральное число: "))
max_digit = 0
reverse_num = 0
if num < 0:
    print("ошибка, число отрицательное")
else:
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        reverse_num = reverse_num * 10 + digit
        num = num // 10
        print("Максимальная цифра:", max_digit)
        print("Число в обратном порядке:", reverse_num)