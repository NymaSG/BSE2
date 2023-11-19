def calculator():
    try:
        f = float(input("Введите первое число: "))
        g = float(input("Введите второе число: "))
        
        c = f + g
    
        print("Результат сложения:", c)
        
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа.")

calculator()