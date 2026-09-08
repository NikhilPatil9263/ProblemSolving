arr = [2,3,4,5,2,3,4,5,6,5,7]
freq_count = {}
for num in arr:
    if num in freq_count:
        freq_count[num] += 1
    else:
        freq_count[num]  = 1
max_freq = 0
for key, value in freq_count.items():
    if value > max_freq:
        max_freq = value
        max_freq_element = key
print("Element with highest frequency:", max_freq_element, "with frequency:", max_freq)