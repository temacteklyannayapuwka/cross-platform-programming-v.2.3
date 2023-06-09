if __name__ == '__main__':
    word = input("Input word: ")

    idx = len(word) // 2
    if len(word) % 2 == 1:
        # Word length is odd
        r = word[:idx] + word[idx+1:]
    else:
        # Word length is even
        r = word[:idx-1] + word[idx+1:]
    print(r)
    input("Press any button to exit")