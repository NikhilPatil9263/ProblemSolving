s = ["listen"]
t = ["silent"]
freq_s= {}
freq_t= {}

for ch in s[0]:
    if ch in freq_s:
        freq_s[ch] += 1
    else:
        freq_s[ch] = 1
for ch in t[0]:
    if ch in freq_t:
        freq_t[ch] += 1
    else:
        freq_t[ch] = 1
if freq_s == freq_t:
    print("the two strings are anagrams")
else:
    print("the two strings are not anagrams")