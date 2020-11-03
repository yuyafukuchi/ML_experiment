from module import add,mul
import monkeytype

def main():
    print(add(1,3))

    with monkeytype.trace():
        mul(2,2)
    return

if __name__ == '__main__':
    main()
