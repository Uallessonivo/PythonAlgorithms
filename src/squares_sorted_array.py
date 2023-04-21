def squares_sorted_array(nums):
    squares = []

    for num in nums:
        squares.append(num * num)

    squares.sort()

    return squares


def squares_sorted_array2(nums):
    return sorted(map(lambda x: x * x, nums))


if __name__ == "__main__":
    variable = [-4, -1, 0, 3, 10]
    
    result = squares_sorted_array(variable)
    print(result)
    
    result = squares_sorted_array2(variable)
    print(result)
