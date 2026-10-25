words = ["ai", "python", "data"]

squares = [x**2 for x in range(1, 11) if x % 2 == 0]

print(squares)

word_lengths = {word: len(word) for word in words}

print(word_lengths)

unique_letters = sorted({letter for letter in "banana"})

print(unique_letters)