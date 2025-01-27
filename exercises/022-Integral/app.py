# Your code here
def squares_dictionary(n):
    dictionary = {}
    for i in range(1, n+1):
        dictionary[i]= i*i
    return dictionary

print(squares_dictionary(8))
