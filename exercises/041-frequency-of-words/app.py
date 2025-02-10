# Your code here
def compute_word_frequency(string):
    aux = string.split(' ')
    aux1 = sorted(aux)
    aux2 = {}

    for x in aux1:
        if x in aux2:
            aux2[x] += 1
        else:
            aux2[x] = 1
    
    return aux2



print(compute_word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))