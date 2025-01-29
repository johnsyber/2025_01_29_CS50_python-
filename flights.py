class Flight():
    # Метод створення нового рейсу з визначеною місткістю
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Метод для додавання пасажира на рейс
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # Метод повернення числа наявних вільних місць
    def open_seats(self):
        return self.capacity - len(self.passengers)

# Створити новий рейс з o= до 3 пасажирів
flight = Flight(3)

# Створити список людей
people = ["Гаррі", "Рон", "Герміона", "Джинні"]

# Спробувати додати кожну особу до списку пасажирів
for person in people:
    if flight.add_passenger(person):
        print(f"{person} додано успішно на рейс")
    else:
        print(f"Для {person} вільних місць немає")



