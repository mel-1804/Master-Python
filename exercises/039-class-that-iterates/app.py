# Your code here
class Iterator:
    def __init__(self, n):
        self.n = n
    
    def divisible_by_seven(self):
        for num in range(0, self.n + 1):
            if num % 7 == 0:
                yield num


obj = Iterator(50)

for num in obj.divisible_by_seven():
    print (num)



