# Задача No27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
# 15 минут
input = "She sells sea shells on the sea shore The shells that she sells are sea "\
    "shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
    # lst - создание списка, при помощи методов lower и split
lst = input.lower().split(' ') # Метод lower() — это строковый метод, который возвращает новую строку полностью в нижнем регистре.Метод split()разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов.
print(lst)
print(f"количество различных слов в тексте: {len(set(lst))}")

# 2  способ
# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# words = text.upper().replace('.', ' ').replace("'", ' ').split()
# uni_words = set(words)
# print(uni_words)
# print(f"Количество различных слов: {len(uni_words)}")