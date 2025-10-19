def remove_odds(nums):
    return [num for num in nums if num % 2 == 0]

original_list = [117, 200, 302, 405, 509, 684]
filtered_list = remove_odds(original_list)
print(f"Original list: {original_list}")
print(f"Filtered list (even numbers): {filtered_list}")