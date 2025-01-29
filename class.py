class Point():
    # Метод визначає, як створювати точку:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(8,3)

print(p.x,p.y)
