def mergeAlternately(word1: str, word2: str) -> str:
    pointer_char = 0
    new_sring = ''
    while pointer_char < min(len(word1), len(word2)):
        new_sring += word1[pointer_char] + word2[pointer_char]
        pointer_char += 1

    if len(word1) == len(word2):
        return new_sring

    if len(word1) > len(word2):
        new_sring += word1[pointer_char:]
    else:
        new_sring += word2[pointer_char:]

    return new_sring


# short solution
def mergeAlternately1(word1: str, word2: str) -> str:
    answer = ""

    for i in range(min(len(word1), len(word2))):
        answer = answer + word1[i] + word2[i]
    return answer + word1[min(len(word1), len(word2)):] + word2[min(len(word1), len(word2)):]
