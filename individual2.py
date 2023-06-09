def count_letters_in_first_sentence(text):
    sentences = text.split('.')
    if len(sentences) > 0:
        first_sentence = sentences[0].strip()
        if first_sentence:
            return sum(char.isalpha() for char in first_sentence)
    return 0

text = input("Input any text: ")
letter_count = count_letters_in_first_sentence(text)
print("Number of letters in the first sentence:", letter_count)
