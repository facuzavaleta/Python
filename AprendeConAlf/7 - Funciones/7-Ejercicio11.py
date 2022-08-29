def func1(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def func2(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = "como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"

print(func1(text))
print(func2(func1(text)))