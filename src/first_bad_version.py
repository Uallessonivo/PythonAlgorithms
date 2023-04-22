# Fake func
def bad_version(version: int):
    if version <= 5:
        return True

    return False


def first_bad_version(version: int) -> int:
    left = 0
    right = version

    while left <= right:
        mid = left + (right - left) // 2

        if bad_version(mid):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    variable = 5
    result = first_bad_version(variable)
    print(result)
