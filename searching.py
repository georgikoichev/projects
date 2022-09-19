from validation import is_int, is_list

def binary_search(numbers, n):
    is_list(numbers)
    is_int(n)

    numbers.sort()
    n_list = numbers.copy()

    while numbers:
        middle_index = len(numbers) // 2
        middle = numbers[middle_index]
        if n > middle:
            numbers = numbers[middle_index:]
        elif n < middle:
            numbers = numbers[:middle_index]
        else:
            return n_list.index(n)
    return
