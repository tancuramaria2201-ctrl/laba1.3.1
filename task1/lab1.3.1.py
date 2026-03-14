import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        value = p * (p - self.a) * (p - self.b) * (p - self.c)
        if value <= 0:
            return 0
        return math.sqrt(value)
    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"
class Rectangle:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b
    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"
class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        s = (self.a + self.b + self.c + self.d) / 2
        value = (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d)
        if value <= 0:
            return 0
        return math.sqrt(value)
    def __str__(self):
        return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"
class Parallelogram:
    def __init__(self, a, b, h):
        self.a = float(a)
        self.b = float(b)
        self.h = float(h)
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.h
    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.h})"
class Circle:
    def __init__(self, r):
        self.r = float(r)
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r ** 2
    def __str__(self):
        return f"Circle({self.r})"
def read_shapes(filename):
    shapes = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.split()
                if not parts:
                    continue
                name = parts[0]
                params = parts[1:]
                try:
                    if name == "Triangle":
                        shapes.append(Triangle(*params))
                    elif name == "Rectangle":
                        shapes.append(Rectangle(*params))
                    elif name == "Trapeze":
                        shapes.append(Trapeze(*params))
                    elif name == "Parallelogram":
                        shapes.append(Parallelogram(*params))
                    elif name == "Circle":
                        shapes.append(Circle(*params))
                except:
                    print("Помилка у рядку:", line.strip())
    except FileNotFoundError:
        print("Файл не знайдено:", filename)
    return shapes
def process_file(filename):
    shapes = read_shapes(filename)
    if not shapes:
        print("Файл порожній або немає коректних фігур")
        return
    max_area_shape = max(shapes, key=lambda s: s.area())
    max_per_shape = max(shapes, key=lambda s: s.perimeter())
    print("Файл:", filename)
    print("Фігура з найбільшою площею:")
    print(max_area_shape, "Area =", round(max_area_shape.area(), 3))
    print("Фігура з найбільшим периметром:")
    print(max_per_shape, "Perimeter =", round(max_per_shape.perimeter(), 3))
    print()
files = ["input01.txt", "input02.txt", "input03.txt"]
for file in files:
    process_file(file)


