def remove_letters(word):
    if 'о' in word:
        word = word.replace('о', '', 1)
    if 'л' in word:
        word = word[::-1].replace('л', '', 1)[::-1]
    return word

word = input("input word: ")
modified_word = remove_letters(word)
print("Changed word:", modified_word)
