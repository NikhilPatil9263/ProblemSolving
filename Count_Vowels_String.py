s = "artificial intelligence"

a = "aeiou"
freq = 0

for i in s:
    if i in a:
        freq += 1

print("The number of vowels in the string is:", freq)