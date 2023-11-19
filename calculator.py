def calculator():
    try:
        a = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        result = a + num2
    
        print("Результат сложения:", result)
        
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа.")

calculator()