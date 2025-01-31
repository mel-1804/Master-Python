# Your code here
def square_odd_numbers(string):
    num = string.split(',')
    result = []
    for n in num:
        if not int(n) % 2 == 0:
            result.append((int(n))**2)
    return result

print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))