nums = [100, 4, 200, 1, 3, 2]
nums_set = set(nums)
longest = 0
for num in nums_set:
    if num - 1 not in nums_set:
        current_num = num
        length = 1

        while current_num + 1 in nums_set:
            current_num += 1
            length += 1
        longest = max(longest, length)
print(longest)