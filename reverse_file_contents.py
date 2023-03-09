import os

# Функція для зчитування та запису даних з файлу у зворотньому порядку

def reverse_file_contents(input_path, output_path):

    # перевірка, чи існує файл

    if not os.path.isfile(input_path):

        print(f"Помилка: Файл {input_path} не знайдено.")

        return

    # зчитування даних з файлу

    with open(input_path, "r") as f:

        lines = f.readlines()

    # перевернення списку з рядків

    lines.reverse()

    # запис даних у новий файл

    with open(output_path, "w") as f:

        f.writelines(lines)

    print(f"Дані з файлу {input_path} успішно записано у зворотньому порядку у файл {output_path}.")

# Приклад виклику функції з вхідним параметром

input_path = "input.txt"

output_path = "output.txt"

reverse_file_contents(input_path, output_path)

