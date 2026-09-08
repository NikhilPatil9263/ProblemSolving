arr = [2,3,4,2,5,4,6,7]
freq_count = {}
for num in arr:
    if num in freq_count:
        freq_count[num] += 1
    else:
        freq_count[num] = 1
print("frequency count of elements:", freq_count)


