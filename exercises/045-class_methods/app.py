# Your code here
class MathOperations:
    pi = 3.14159

    @classmethod
    def calculate_circle_area(cls, radius):
        return cls.pi * radius ** 2


circle_area = MathOperations.calculate_circle_area(5)
print(circle_area)