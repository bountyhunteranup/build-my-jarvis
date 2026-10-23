text = input("Please enter a text: ").lower()

common_count = 0
words = []
word = ''
for m in range(len(text)):
    if text[m] != '.' and text[m] != '!' and text[m] != '?' and text[m] != ',' and text[m] != ' ':
        word += text[m]
    if text[m] == ' ':
        if word:
            words.append(word)
            word = ''
if word:
    words.append(word)
# for n in range(len(words)):
#     print(words[n])
    
word = []
for i in range(len(words)):
    current = words[i]
    # Assign each word to current from the list words
    for j in range(len(words)):
        # here j is the count of the total number of words in list 'word'
        if current != words[j]:
            # to check if the word is same as the current 'word' 
            if current not in word:
                # check if the current word is present in the lsit 'word'
                word.append(current)   

frequency = {}

for word in words:
    if word in frequency:
        # What should happen to the existing count?
        frequency[word] += 1
    else:
        # What should the first count be?
        frequency[word] = 1
print(frequency)
    
            
highest_count = 0
most_common = []

for word in frequency:
    if frequency[word] > highest_count:
        # Update highest_count
        highest_count = frequency[word]
        # Reset most_common to contain this word
        most_common = [word]
        
    elif frequency[word] == highest_count:
        # Add this word to most_common    
        most_common.append(word)
            
print(f"Highest count : {highest_count}")
print(f"Most common : {most_common}")