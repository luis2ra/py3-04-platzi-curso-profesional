# class 18: removing duplicates from a list

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 2, 2, 2, 3, "Platzi", "Platzi", True, 4.6, False]
    print("original list: ", random_list)

    print("removing with a function: ", remove_duplicates(random_list))
    print("removing appling sets: ", remove_duplicates_with_sets(random_list))


if __name__ == '__main__':
    run()
