input_string = input("Введіть рядок: ")
unique_characters = set(input_string)
unique_count = len(unique_characters)

if unique_count > 10:
    print(True)
else:
    print(False)