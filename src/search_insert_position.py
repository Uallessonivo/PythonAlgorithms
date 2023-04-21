def insert_position(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


if __name__ == "__main__":
    variable = [1, 3, 5, 6]
    result = insert_position(variable, 2)
    print(result)
