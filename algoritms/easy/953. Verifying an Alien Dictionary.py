def isAlienSorted(words: list[str], order: str) -> bool:
    alp = {v: k for k, v in enumerate(order)}

    def word_to_num(word: str) -> list:
        res = []
        for char in word:
            res.append(alp[char])
        return res

    return sorted(words, key=word_to_num) == words
