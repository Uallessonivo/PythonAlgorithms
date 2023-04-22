def two_sum(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] + nums[right] == target:
            return [left + 1, right + 1]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    variable = [2, 7, 11, 15]
    result = two_sum(variable, 9)
    print(result)
