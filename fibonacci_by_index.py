# Функція для обчислення чисел Фібоначчі

def fibonacci(index):

    # Якщо індекс менший або рівний 0, повернути 0

    if index <= 0:

        return 0

    # Якщо індекс дорівнює 1, повернути 1

    elif index == 1:

        return 1

    else:

        # обчислення чисел Фібоначчі

        a, b = 0, 1

        for i in range(2, index+1):

            c = a + b

            a, b = b, c

        return b

# Приклад виклику функції з вхідним параметром

index = 10

result = fibonacci(index)

print(f"Число Фібоначчі з індексом {index}: {result}")

