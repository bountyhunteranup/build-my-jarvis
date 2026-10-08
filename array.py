text = input("Please enter a text: ")

common_count = 0
words = []
word = ''
for m in range(len(text)):
    if text[m] != '.' and text[m] != '!' and text[m] != '?' and text[m] != ',':
        word += text[m]
    if text[m] == ' ':
        if word:
            words.append(word)
            word = ''
if word:
    words.append(word)
for n in range(len(words)):
    print(words[n])