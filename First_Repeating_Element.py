arr = [2,3,4,2,5,6,3]
seen = set()
for num in arr:
    if num in seen:
        print("First repeating element:", num)
        break
    seen.add(num)