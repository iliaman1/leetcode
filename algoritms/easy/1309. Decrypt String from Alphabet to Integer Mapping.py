def freq_alphabets(s: str) -> str:
    alpha_dict = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
        '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r',
        '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'
    }

    res_string = ''
    i = 0

    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':
            res_string += alpha_dict[s[i:i + 3]]
            i += 3
        else:
            res_string += alpha_dict[s[i]]
            i += 1

    return res_string


# short and good solution
def freq_alphabets1(s: str) -> str:
    for i in range(26, 0, -1):
        s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))

    return s
