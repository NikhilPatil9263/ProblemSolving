arr = [0,2,1,3,0,2,0,0,4,5,0]
left = 0
right = len(arr)-1
while left < right:
    if arr[left] == 0 and arr[right]!= 0:
        arr[left], arr[right] = arr[right],arr[left]
    elif arr[left] == 0 and arr[right] == 0:
        right -= 1
    else:
        left += 1
print(arr)

        

