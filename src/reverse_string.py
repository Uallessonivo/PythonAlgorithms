def reverse_string(s: list[str]) -> list[str]:
    s.reverse()
    return s


if __name__ == "__main__":
    result = reverse_string(['h', 'e', 'l', 'l', 'o'])
    print(result)
