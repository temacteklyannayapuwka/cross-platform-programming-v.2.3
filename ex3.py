import sys

if __name__ == '__main__':
    s = input("Input any sentence: ")
    n = int(input("Input length: "))

    # Check length
    if len(s) >= n:
        print(
            "Specified length must be greater than the length of the sentence",
            file=sys.stderr
        )
        exit(1)

    # Split sentence into words
    words = s.split(' ')
    # Check the number of words in a sentence
    if len(words) < 2:
        print(
            "The sentence must contain several a few",
            file=sys.stderr
        )
        exit(1)

    # Number of spaces to add
    delta = n
    for word in words:
        delta -= len(word)

    # The number of spaces per word
    w, r = delta // (len(words) - 1), delta % (len(words) - 1)

    # Generate a list to store words and spaces
    lst = []

    # Number all the words in the list and iterate over them
    for i, word in enumerate(words):
        lst.append(word)

        # If the word is not the last, add spaces
        if i < len(words) - 1:
            # Determine the number of spaces
            width = w
            if r > 0:
                width += 1
                r -= 1

            # Add the given number of spaces to the list
            if width > 0:
                lst.append(' ' * width)

    # Output a new sentence by concatenating all the elements of the lst
    print(''.join(lst))
    input("Press any button to exit")