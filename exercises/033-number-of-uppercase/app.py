# Your cod here
def number_of_uppercase(sent):
    counts = {"UPPER": 0, "LOWER": 0}
    for char in sent:
        if char.isupper():
            counts["UPPER"] += 1
        elif char.islower():
            counts["LOWER"] += 1
        else:
            pass
    return f"UPPERCASE: {counts["UPPER"]}, LOWERCASE: {counts["LOWER"]}"

print(number_of_uppercase("Hello world!"))
