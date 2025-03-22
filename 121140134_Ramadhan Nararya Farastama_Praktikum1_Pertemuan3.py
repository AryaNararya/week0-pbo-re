import math

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Cannot divide by zero!")
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)

    def log(self, base):
        if base.value <= 0 or self.value <= 0:
            raise ValueError("Logarithm is only defined for positive numbers!")
        return Calculator(math.log(self.value, base.value))

    def __repr__(self):
        return str(self.value)

# Contoh penggunaan
a = Calculator(10)
b = Calculator(2)

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ^ b =", a ** b)
print("log base b of a =", a.log(b))

import random

class Father:
    def __init__(self, blood_type):

        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child(Father, Mother):
    def __init__(self, father, mother):
        # Memilih satu alel dari setiap orang tua
        self.father_allele = random.choice(list(father.blood_type))
        self.mother_allele = random.choice(list(mother.blood_type))
        self.blood_type = self.father_allele + self.mother_allele

    def get_blood_type(self):
        return self.blood_type

# Contoh penggunaan
father = Father("AO")  # Ayah dengan alel A dan O
mother = Mother("BO")  # Ibu dengan alel B dan O

child = Child(father, mother)
print("Golongan darah anak:", child.get_blood_type())