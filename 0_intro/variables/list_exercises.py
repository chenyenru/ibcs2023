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

    # another way to do this from tr.brent


def brent1_remove_duplicate(input_list):
    for val in input_list:
        while input_list.count(val) > 1:
            mylist.remove(val)
    # third way


def brent2_remove_duplicate(input_list):
    # enumerates over the list and find the first one (so that it does not have duplicates)
    newlist = [x for i, x in enumerate(mylist) if mylist.index(x) == i]
    return newlist


def brent3_remove_duplicate(input_list):
    # put it in my list if it does not occurr anywhere else in the list (anywhere after me)
    newlist = [x for i, x in enumerate(mylist) if x not in mylist[i+1:]]


print(remove_duplicate(mylist))


# 03. Write a program that finds the intersection of two list


def find_intersection(list1, list2):
    new_list = [x for x in list1 if x in list2]

    return list(set(new_list))


print(find_intersection(mylist, hislist))
# 04. Write a program that finds the union of two lists, omitting duplicates


def find_union(list1, list2):
    result = list(set(list1+list2))
    return result


print(find_intersection(mylist, hislist))


def brent1_find_intersection(mylist):
    result2 = [x for i, x in enumerate(
        lista) if x in listb and lista.index(x) == 1]


# 05. Write a program that finds the differences of two lists (opposite of intersection)


def find_differences(list1, list2):
    new_list = [
        x for x in list1 if x not in list2]
    new_list += ([x for x in list2 if x not in list1])

    return list(set(new_list))


print(find_differences(mylist, hislist))


def brent1_find_differences(list1, list2):
    result = [x for x in (list1 + list2)
              if ((x not in list1) != (x not in listb))]
    return list(set(result))


# 06. Write a program that creates a list containing the frequencies
# [[1, 3]]


def count_freq(list1):
    list2 = list(set(list1))
    newlist = []
    for val in list2:
        newlist += [[val, list1.count(val)]]
    return newlist


def brent_freq(list1):
    freq = [(x, list1.count(x))
            for i, x in enumerate(list1) if i == list1.index(x)]

    print("Solution 2: ", freq)


print(count_freq(mylist))

print("hello world")
