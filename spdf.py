class Shape:
    def draw(self):
        print("Рисую фигуру...")

class Circle(Shape):
    def draw(self):
        print("Рисую круг 🟢")

class Square(Shape):
    def draw(self):
        print("Рисую квадрат 🟦")

class Triangle(Shape):
    def draw(self):
        print("Рисую треугольник 🔺")

shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.draw()
