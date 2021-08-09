while True:
    a = int(input('Введите первое число'))
    b = int(input('Введите второе число'))
    c = input('Введите знак')
    if c == '+':
        print(a + b)
    if c == '-':
        print(a - b)
    if c == '*':
        print(a * b)
    if c == '/':
        if b == 0:
            print('Деление на ноль невозможно')
            continue
        print(a / b)