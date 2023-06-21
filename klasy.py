import math


class Uczen:
    # właściwości
    def __init__(self, name, surname, level):
        self.name = name
        self.surname = surname
        self.level = level

    # metody
    def show_full_name(self):
        return self.name + " " + self.surname


uczen1 = Uczen("Ania", "Kek", 8)
uczen2 = Uczen("Kamil", "Macionk", 7)

print(uczen1.show_full_name())


class Liczby:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def wyswietl(self):
        return self.x, self.y


print(Liczby(1, 2).wyswietl())


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_coordinates(self):
        return self.x, self.y

    def __str__(self) -> str:
        return f"Wektor o współrzędnych {self.x}. {self.y}"

    def __repr__(self) -> str:
        return f"Wektor o współrzędnych {self.x}. {self.y}"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False

    def __neg__(self):
        if self.x > 0 or self.y > 0:
            return self.x - (2 * self.x), self.y - (2 * self.y)
        else:
            return self.x, self.y

        # można było też zrobić tylko return -self.x, -self.y

    @staticmethod
    def mnozenie(a, b):
        return a * b

    @classmethod
    def foo(cls):
        return cls


vec1 = Vector2D(1, 2)
print(vec1.mnozenie(9, 2))

vec1 = Vector2D(3, 2)
vec2 = Vector2D(3, 4)
print(vec1.show_coordinates())
print(vec1)
print(Vector2D.__add__(vec1, vec2))
print(Vector2D.__sub__(vec1, vec2))
print(Vector2D.__eq__(vec1, vec2))

print(Vector2D.__neg__(vec1))


# dziedziczenie i kompozycja

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def honk(self):
        print("Honk!")


class Car(Vehicle):
    def drive(self):
        print(f"Driving the {self.color} {self.brand} car")


class Bicycle(Vehicle):
    def ride(self):
        print(f"Riding the {self.color} {self.brand} bicycle")


car = Car("Maluch", "blue")

car.honk()

bicycle = Bicycle("romet", "czerwony")

bicycle.honk()


class Ferry(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)

    def foo(self):
        return 1


class Unit_Vector(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)

    def dlugosc_wektora(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


V3 = Unit_Vector(1, 2)

print(Unit_Vector.dlugosc_wektora(V3))


class Figure:
    def __init__(self, sides):
        if not all(side > 0 for side in sides):
            print("Boki muszą mieć dodatnią długość")
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides)


class InvalidSideLengthError:
    pass


class Trojkat(Figure):
    def __init__(self, side1, side2, side3):
        try:
            self.figure = Figure([side1, side2, side3])
        except InvalidSideLengthError as e:
            raise ValueError("Niewłaściwe długości boków") from e

    def get_perimeter(self):
        return self.figure.get_perimeter()


#     def get_area(self):
#
# class Czworokat(Figure):

class MyClass:
    def __init__(self, x):
        self.x = x

    def lubie_placki(self):
        return "lubie placki"


C = MyClass(1)
print(hasattr(C, "lubie_placki"))

#wyjątki
def kelvin_to_cel(x):
    """
    0K = -273*C
    273K = 0*C
    
    returns temperature in celcius degree
    """

    if x < 0:
        raise AssertionError("Temperatura musi być dodatnia na skali Kelvina")

    return x-273

print(kelvin_to_cel(0))

# help(kelvin_to_cel)

# dir(kelvin_to_cel)

a='ant'
b="bat"
c='camel'
print(a,b,c, sep='"')