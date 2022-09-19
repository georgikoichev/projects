def is_int(n):
    if type(n) != int:
        raise TypeError("integer required")


def is_list(n):
    if type(n) != list:
        raise TypeError("list required")