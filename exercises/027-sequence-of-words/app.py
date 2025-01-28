# Your code here
def sequence_of_words(words):
    new_list = words.split(",")
    aux = sorted(new_list)
    result = ', '.join(aux)
    return result



print(sequence_of_words("without,hello,bag,world"))