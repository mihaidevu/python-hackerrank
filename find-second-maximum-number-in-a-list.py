my_list = [3, 5, 1, 8, 7, 2, 8, 4]
def find_second_maximum(numbers):
    ordered_numbers = sorted(set(numbers), reverse=True)
    if len(ordered_numbers) < 2:
        return None  # Not enough unique numbers to find the second maximum
    return ordered_numbers[1]

second_max = find_second_maximum(my_list)
print("The second maximum number is:", second_max)
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/