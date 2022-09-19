from projects.validation import is_list


def sorting(numbers):
    is_list(numbers)
    for i in range(len(numbers)):
        smallest = min(numbers[i:])
        smallest_index = numbers[i:].index(smallest) + i
        numbers[smallest_index], numbers[i] = numbers[i], numbers[smallest_index]
    return numbers