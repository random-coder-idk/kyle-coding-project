text = input("Enter a word or sentence: ")
letters_only = text.replace(" ", "")
if len(letters_only) % 2 == 0:
    print("The input has an even number of letters.")
else:
    print("The input has an odd number of letters.")
    
