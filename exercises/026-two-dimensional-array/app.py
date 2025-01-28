# Your code here
def two_dimensional_list(x,y):
    matrix = [[i * j for j in range(y)] for i in range(x)]
    return matrix

print(two_dimensional_list(3,5))