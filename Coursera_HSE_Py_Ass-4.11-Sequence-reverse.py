def reverse(l):
    if len(l) > 1:
        print(l[len(l)-1])
        del l[len(l)-1]
        return reverse(l)
    else:
        return l[0]


def ss(n):
    if n != 0:
        l.append(n)
        return ss(int(input()))
    elif n == 0 and len(l) == 0:
        return n
    elif n == 0 and len(l) != 0:
        l.append(n)
        return reverse(l)


l = []
print(ss(int(input())))
