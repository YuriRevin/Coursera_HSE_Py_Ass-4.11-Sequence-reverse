def print_reversed(seq, pos=0):
    elem = seq[pos]
    if elem != 0:
        print_reversed(seq, pos + 1)
    print(elem)


print_reversed(tuple(map(int, input().split())))
