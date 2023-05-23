class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return ComplexNumber(real_diff, imag_diff)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


# Тест
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

c3 = c1 + c2
print(c3)

c4 = c1 - c2
print(c4)

print(c1 == c2)

print(c1 != c2)
