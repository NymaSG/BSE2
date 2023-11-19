def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        result = num1 + num2
    
        print("Результат сложения:", result)
        
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа.")

calculator()