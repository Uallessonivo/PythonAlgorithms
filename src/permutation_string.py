from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    # Cria uma lista de contagem de caracteres para s1
    s1_count = Counter(s1)
    # Cria uma lista de contagem de caracteres para janela de s2
    s2_count = Counter(s2[:len(s1)])
    # Verifica se a janela inicial de s2 é uma permutação de s1
    if s2_count == s1_count:
        return True

    # Desliza a janela de s2 e atualiza a contagem de caracteres
    for i in range(len(s1), len(s2)):
        # Remove o caractere mais antigo da janela
        if s2_count[s2[i - len(s1)]] == 1:
            del s2_count[s2[i - len(s1)]]
        else:
            s2_count[s2[i - len(s1)]] -= 1

        # Adiciona o novo caractere à janela
        s2_count[s2[i]] += 1
        # Verifica se a janela atual é uma permutação de s1
        if s2_count == s1_count:
            return True

    return False


if __name__ == "__main__":
    variable = "ab"
    result = check_inclusion(variable, "eidbaooo")
    print(result)
