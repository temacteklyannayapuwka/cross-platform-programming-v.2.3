def get_odd_letters(word):
    odd_letters = ""
    for i in range(len(word)):
        if i % 2 == 0:
            odd_letters += word[i]
    return odd_letters

S1 = input("Input word S1: ")
S2 = get_odd_letters(S1)
print("word S2, odd-letter word S1:", S2)