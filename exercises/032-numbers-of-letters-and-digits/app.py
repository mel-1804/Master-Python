# # Your code here
# def letters_and_digits(sent):
#     string = [x for x in sent]
#     alpha = 0
#     digit = 0
#     for char in string:
#         if char.isdigit():
#             digit = digit + 1
#         elif char.isalpha():
#             alpha = alpha + 1

#     return f"DIGITS: {digit}, LETTERS: {alpha}"

# print(letters_and_digits("hello world! 123"))


def letters_and_digits(sent):
    string = [x for x in sent]
    counts = {"DIGITS" : 0, "LETTERS" : 0}
   
    for char in string:
        if char.isdigit():
            counts["DIGITS"] += 1
        elif char.isalpha():
            counts["LETTERS"] += 1

    return f"DIGITS: {counts["DIGITS"]}, LETTERS: {counts["LETTERS"]}"

print(letters_and_digits("hello world! 123"))