# Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, 
# наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, 
# коли розділювачі симетричні, несиметричні, наприклад ( ( ( ) , 
# або коли розділювачі різних видів стоять у парі, як-от ( }.


def check_brackets(line: str):
    br = {'{': '}', '[': ']', '(': ')'}
    stack = []

    last_ind = None
    for ind, ch in enumerate(line):
        last_ind = ind
        if ch in br.keys():
            stack.append(ch)
        if ch in br.values():
            if br.get(stack.pop()) != ch:
                return False, ind
    return len(stack) == 0, last_ind + 1 if last_ind is not None else -1


def check_brackets_result(line: str):
    print(line)
    res, ind = check_brackets(line)
    if not res:
        print(f"{' ' * ind}^-error" )
    else:
        print('no errors')


check_brackets_result('( ){[ 1 ]( 1 + 3 )( ){ }}')
check_brackets_result('( 23 ( 2 - 3)')
check_brackets_result('( 11 }')
check_brackets_result('')
