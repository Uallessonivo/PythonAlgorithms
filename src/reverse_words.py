def reverse_words_in_string(s: str) -> str:
    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i][::-1]

    reversed_s = " ".join(words)

    return reversed_s


def reverse_words_in_string_v2(s: str) -> str:
    words = s.split(' ')

    reversed_words = map(lambda word: word[::-1], words)

    return " ".join(reversed_words)


if __name__ == "__main__":
    result = reverse_words_in_string("Let's take LeetCode contest")
    print(result)

    result = reverse_words_in_string_v2("Let's take LeetCode contest")
    print(result)
