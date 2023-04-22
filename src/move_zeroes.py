def move_zeroes(nums: list[int]) -> list[int]:
    n = len(nums)
    zero_index = 0

    for i in range(0, n):
        if nums[i] != 0:
            (nums[i], nums[zero_index]) = (nums[zero_index], nums[i])
            zero_index += 1

    return nums


if __name__ == "__main__":
    variable = [0, 1, 0, 3, 12]
    result = move_zeroes(variable)
    print(result)
