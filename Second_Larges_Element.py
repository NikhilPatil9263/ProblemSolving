arr = [2,4,3,4,10,5,7,9]
largest = 0
second_largest = 0
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("The second largest elements is :", second_largest)
