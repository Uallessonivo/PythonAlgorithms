def rotate_array(nums, k):
    n = len(nums)
    k = k % n

    nums.reverse()

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums


if __name__ == "__main__":
    variable = [1, 2, 3, 4, 5, 6, 7]
    result = rotate_array(variable, 3)
    print(result)
