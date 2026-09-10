nums = [2, 1, 5, 1, 3, 2]
k = 3

left = 0
right = k

current_sum = sum(nums[left:right])
max_sum = current_sum

while right < len(nums):
    current_sum -= nums[left]
    current_sum += nums[right]

    left += 1
    right += 1

    max_sum = max(max_sum, current_sum)

print(max_sum)