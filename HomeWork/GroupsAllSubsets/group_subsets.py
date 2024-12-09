from itertools import chain, combinations


def subsets_of_list(lst):
    """
    You are expected to write a Python function that is passed
    a list of integers and returns a dictionary with keys all possible sums
    of subsets of the list, with a respective value for each key the list
    of all subsets (as lists) that have the same sum.

    Within individual subsets, items must appear in the order they appear in the original list.

    Repeated elements in the input list can appear in subsets up to the number of their ocurrence.
    :param lst:
    :return:
    """
    my_dict = dict()
    s = list(lst)
    subsets = list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
    for s in subsets:
        sub_sum = sum(s)
        if sub_sum not in my_dict:
            my_dict[sub_sum] = []
        my_dict.get(sub_sum).append(list(s))

    return my_dict






print(subsets_of_list([1, 2]))