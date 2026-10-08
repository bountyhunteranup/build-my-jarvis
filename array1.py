common = ['hello', 'what', 'hello', 'hello', 'what']

unique = []

count = 0

for i in range(len(common)):
    current = common[i]
    found = False

    for item in unique:
        if item == current:
            found = True
            break
            
    if not found:
        unique.append(current)

print(unique)
# print(count)

highest_count = 0
most_common = ""

for word in unique:
    count = 0
    
    for item in common:
        if item == word:
            count += 1
    print(f"{word}: {count}")
    
    if count > highest_count:
        highest_count = count
        most_common = word

print(f"The most common word is '{most_common}' with a count of {highest_count}.")