import random

def get_crazy_word(word):
    if len(word) < 3:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]

def get_crazy_words(text):
    lines = text.split('\n')
    crazy_lines = []
    for line in lines:
        words = line.split()
        crazy_words = [get_crazy_word(word) for word in words]
        crazy_lines.append(' '.join(crazy_words))
    return '\n'.join(crazy_lines)
