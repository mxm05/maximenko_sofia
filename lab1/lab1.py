# Лабораторная работа 1.
# Базовый калькулятор

# Получение операции от пользователя

operation = input("Введите операцию (+ для сложния): ")

# Получение двух чисел от пользователя

num1 = ""
num2 = ""

while not num1.isdigit():
    num1 = input("Введите первое число: ")


while not num2.isdigit():
    num2 = input("Введите второе число: ")

num1 = int(num1)
num2 = int(num2)

# Выполнение операции
if operation == "+":
  result = num1 + num2
  print(f"Результат сложения: {result}")
elif operation == "-":
  result = num1 - num2
  print(f"Результат вычитания: {result}")
elif operation == "*":
  result = num1 * num2
  print(f"Результат умножение: {result}")
elif operation == ":":
  result = num1 / num2
  print(f"Результат частное7: {result}")
else:
  print("Операция не поддерживается")