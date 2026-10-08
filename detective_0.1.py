text = input("Enter the text to analyze: ")

char_count = 0

for i in range(len(text)):
    char_count += 1

word_count = 0
# for j in range(len(text)):
#     if text[j] == ' ':
#         word_count += 1

sentence_count = 0
for k in range(len(text)):
    if text[k] == '.' or text[k] == '!' or text[k] == '?':
        sentence_count += 1
        
digit_count = 0 
for l in range(len(text)):
    if text[l].isdigit():
        digit_count += 1
    
common_count = 0
words = []
word = ''
dilimiters = ['.', '!', '?', ',', ' ']
for m in range(len(text)):
    if text[m] not in dilimiters:
        word += text[m]
    else: 
        if word != '':
            words.append(word)
            word = ''
        
if word:
    words.append(word)
# for n in range(len(words)):
#     print(words[n])     

for texts in words:
    word_count += 1
    
unique = []

for i in range(len(words)):
    current = words[i]
    found = False
    
    for item in unique:
        if item == current:
            found = True
            break
    if not found:
        unique.append(current)

highest_count = 0 
most_common = []

for word in unique:
    count = 0
    
    for item in words:
        if item == word:
            count += 1
    # print(f"{word}: {count}")
    
    if count > highest_count:
        most_common = [word]
        highest_count = count
    elif count == highest_count:
        most_common.append(word)
    else:
        continue

print("\nThe total number of characters in the text is: ", char_count)
print("The total number of words in the text is: ", word_count + 1)
print("The total number of sentences in the text is: ", sentence_count)
print("The total number of digits in the text is: ", digit_count)
print(f"The most common word is '{most_common}' with a count of {highest_count}.")