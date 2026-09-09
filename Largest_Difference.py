arr = [2,4,3,5,8,5,9,10,45,23,54]
largest = 0
smallest = float('inf')
for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("the largest element is:",largest)
print("the smallest element is:",smallest)
print("the difference between largest and smallest element is:",largest - smallest)