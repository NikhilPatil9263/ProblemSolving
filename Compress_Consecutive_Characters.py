words = "aaabbccccd"

result = ""
left = 0
right = 0

while right < len(words):
   
    while right < len(words) and words[right] == words[left]:
        right += 1
    count = right - left

    result += words[left] + str(count)

    left = right
    
print(result)