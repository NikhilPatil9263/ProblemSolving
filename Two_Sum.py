arr = [2,7,11,15,16,18,22,23,24,28]
target = 30
left = 0
right = len(arr)-1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        print("the two numbers are:", arr[left], "and", arr[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1