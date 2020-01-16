if __name__ == '__main__':
    a=()
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    a = tuple(integer_list)
    print(hash(a))
