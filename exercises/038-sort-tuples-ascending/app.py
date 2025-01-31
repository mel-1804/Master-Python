from operator import itemgetter

# Your code here
def sort_tuples_ascending(input):
    result = sorted(input, key=itemgetter(0,1,2))
    return result


print(sort_tuples_ascending(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85']))