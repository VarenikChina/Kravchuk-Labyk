def remove_duplicates(input_list):

    return list(set(input_list))

def sort_elements(unique_list):
    numbers = [x for x in unique_list if isinstance(x, (int, float))]
    strings = [x for x in unique_list if isinstance(x, str)]

    numbers.sort(reverse=True)
    strings.sort()

    return numbers + strings

input_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Hello']
unique_list = remove_duplicates(input_list)
result = sort_elements(unique_list)
print(result)
