arr = [2,4,3,5,2,1,4,6,9]
seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates found:", duplicates)