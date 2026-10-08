a = ['hello','damn','what','hello','hello','what']
# b = ['what','why','hello']

# for i in range(len(a)):
#     for j in range(len(a) + 1):
#         if a[i] == a[j]:
#             print(a[i])
common = []           
def compare(x):
    global common
    global count
    count = 0
    for i in range(len(a)):
        if i != x:
            if a[x] == a[i]:
                count += 1
    if count > 0:
        common.append(a[x])
    if x < len(a) - 1:
        x += 1
        compare(x)

# common.append(compare(0))
compare(0)
print(common)

# for i in range(len(common)):
#     temp  = []
#     temp.append(common[i])
#     count = 0
#     for j in range(len(common)):
#         if temp[0] == common[j]:
#             count += 1
#     if temp[0] == common[i]:
#         common.pop(i)
        
unique = []

for i in range(len(common)):

    # current word
    current = common[i]

    # determine whether current is already in unique
    found = False

    for j in range(len(unique)):
        if unique[j] == current:
            found = True

    if not found:
        unique.append(current)

print(f"Unique elements: {unique}")