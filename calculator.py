def calculator():
    try:
        k = float(input("Введите первое число: "))
        l = float(input("Введите второе число: "))
        
        c = k + l
    
        print("Результат сложения:", c)
        
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа.")

calculator()