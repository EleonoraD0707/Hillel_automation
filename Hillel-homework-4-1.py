while True:
    word = input("Enter a word with letter 'o':")
    if 'o' in word.lower():
        print("Thank you")
        break
    else:
        print("Enter another word")