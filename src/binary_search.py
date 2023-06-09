def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1


if __name__ == "__main__":
    variable = [-1, 0, 3, 5, 9, 12]
    result = binary_search(variable, 9)
    print(result)
