from int_module import add,mul
from str_module import remove_space
from list_module import double_list
from pandas_module import convert_dict_to_df
import monkeytype

def main():
    print(add(1,3))
    print(remove_space('I am Stranger.'))
    print(double_list([1,2,3]))
    d={'key1': [1,2,3], 'key2': [4,5,6], 'key3': [7,8,9]}
    convert_dict_to_df(d)

    with monkeytype.trace():
        mul(2,2)
    return

if __name__ == '__main__':
    main()
