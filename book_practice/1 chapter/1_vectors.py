from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #метод для показа строки пользователю
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    #Сложение
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    #Вычитание (смотреть в специальных методах для операторов)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __lt__(self, other):
        v1 = self.x + self.y
        v2 = other.x + other.y

        if v1 < v2:
            return True
        else:
            return False

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(1,4)
v2 = Vector(10,1)

print(v1 - v2)
print(v1 > v2)
#print(abs(v1))
#print(abs(v1*3))

#print(repr(v1))

# Замена (Аналог) format()
#print('Vector %r %r' % (5,10))
