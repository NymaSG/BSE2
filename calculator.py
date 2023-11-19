def calculator():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        c = a + b
    
        print("Результат сложения:", c)
        
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа.")

calculator()