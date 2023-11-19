def calculator():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        result = a + b
    
        print("Результат сложения:", result)
        
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа.")

calculator()