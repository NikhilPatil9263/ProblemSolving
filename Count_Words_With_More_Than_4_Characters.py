sentence = "Python makes coding very interesting"
words = sentence.split()
total = 0
for ch in words:
    if len(ch) > 4:
        total += 1
print("The number of words with more than 4 characters is:", total)