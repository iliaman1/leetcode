def interpret(command: str) -> str:
    pointer = 0
    res = ''
    while pointer < len(command):
        if command[pointer] == '(' and command[pointer+1] == ')':
            res += 'o'
            pointer += 1
        if command[pointer] == '(' and command[pointer+1] == 'a':
            res += 'al'
            pointer += 3
        if command[pointer] == 'G':
            res += 'G'
        pointer += 1
    return res


# good solution
def interpret1(command: str) -> str:
    if '()' in command:
        command = command.replace('()', 'o')
    if '(al' in command:
        command = command.replace('(', '')
    if 'al)' in command:
        command = command.replace(')', '')
    return command
