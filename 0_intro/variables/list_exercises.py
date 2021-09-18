# list_exercises.py

from typing import List


mylist = [1, 2, 3, 3, 4, 4, 4]
hislist = list(range(3, 7))

# 01. Sum all of the elements in the list


def sum_list(list):
    return sum(list)


print(sum_list(mylist))

# 02. Write a program that removes all duplicates from a list


def remove_duplicate(input_list):
    new_list = list(set(input_list))
    return new_list


print(remove_duplicate(mylist))
# 03. Write a program that finds the intersection of two list


def find_intersection(list1, list2):
    new_list = [x for x in list1 if x in list2]

    return list(set(new_list))


print(find_intersection(mylist, hislist))
# 04. Write a program that finds the union of two lists, omitting duplicates
print(find_intersection(mylist, hislist))
# 05. Write a program that finds the differences of two lists (opposite of intersection)


def find_differences(list1, list2):
    new_list = [
        x for x in list1 if x not in list2]
    new_list += ([x for x in list2 if x not in list1])

    return list(set(new_list))


print(find_differences(mylist, hislist))

# 06. Write a program that creates a list containing the frequencies
# [[1, 3]]


def count_freq(list1):
    list2 = list(set(list1))
    newlist = []
    for val in list2:
        newlist += [[val, list1.count(val)]]
    return newlist


print(count_freq(mylist))
