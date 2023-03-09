from collections import Counter

# Зчитуємо назву файлу з консолі

filename = input("Введіть назву файлу: ")

# Відкриваємо файл і зчитуємо його вміст

with open(filename, 'r') as file:

    data = file.read().lower()

# Видаляємо знаки пунктуації і роздільники

for ch in '.,:;!?"\'()\n':

    data = data.replace(ch, ' ')

# Розбиваємо текст на окремі слова

words = data.split()

# Рахуємо кількість входжень кожного слова

word_counts = Counter(words)

# Сортуємо слова за частотою використання

sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)

# Виводимо результат

for word in sorted_words:

    print(f"{word}: {word_counts[word]}")

