from projects.validation import is_int


def permutations(n):
    is_int(n)
    def perm(a, k):
        if k == len(a):
            print(a)
        else:
            for i in range(k, len(a)):
                a[k], a[i] = a[i], a[k]
                perm(a, k + 1)
                a[k], a[i] = a[i], a[k]

    numbers = [x+1 for x in range(n)]
    return perm(numbers, 0)

permutations(3)