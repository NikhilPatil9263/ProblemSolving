arr = [1,2,3,5,6,7,8,9,10]
left =0
right = 1
for i in range(len(arr)-1):
    if arr[right] - arr[left] != 1:
        print("the missing number is :",arr[left]+1)
        break
    else:
        left += 1
        right += 1



