from int_module import add,mul
from str_module import remove_space
from list_module import double_list

import monkeytype

def main():
    print(add(1,3))
    print(remove_space('I am Stranger.'))
    print(double_list([1,2,3]))
    with monkeytype.trace():
        mul(2,2)
    return

if __name__ == '__main__':
    main()
