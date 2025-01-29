# Це коментар у Python
names = ["Гаррі", "Рон", "Герміона"]
# Вивести весь список:
print(names)
# Print the second element of the list:
print(names[1])
# Додати нове ім’я до списку:
names.append("Драко")
# Відсотрувати список:
names.sort()
# Вивести новий список:
print(names)


point = (12.5, 10.6)

# Створити пусту множину:
s = set()

# Додати якісь елементи:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Видалити 2 з множини
s.remove(2)

# Вивести множину:
print(s)

# Знайти розмір множини:
print(f"У множині три {len(s)} елементи.")


# Визначення словника
houses = {"Гаррі": "Гриффиндор", "Драко": "Слизерин"}
# Вивести будинок Гаррі
print(houses["Гаррі"])
# Додати значення до словника:
houses["Герміона"] = "Гриффиндор"
# Вивести будинок Герміони:
print(houses["Герміона"])

for i in [0, 1, 2, 3, 4, 5]:
    print(i)

# Створити список:
names = ["Гаррі", "Рон", "Герміона"]

# Вивести кожне ім’я:
for name in names:
    print(name)

name = "Harry"
for char in name:
    print(char)

def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")

