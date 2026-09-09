arr = [1,3,3,2,4,1,2,3,4,6,4,7,6,7,2]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)