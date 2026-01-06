
def bookends(list: list):
    """
    Given a list of numbers remove the first and last elements from the list and
    return a new list of those two elements.
    You can assume any list given is at least 2 elements long.
    Example list of [1,5,7,3,2] the original list would become [5,7,3] and the new
    list would be [1,2]
    :param list:
    :return:
    """
    ListNew = [list[0], list[-1]]
    list.pop(0)
    list.pop(-1)
    return ListNew



def inOrder(list : list):
    """
    Given a list of numbers return true if the list is in ascending order.
    :param list:
    :return:
    """
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

def find(list: list, target : int):
    """
    Given a list of numbers and a target value return the index location of the
    target value within the list.
    If the target value is not in the list return -1
    If multiple of the target value exist within the list you may return either
    index.
    You are not alowed to use the built-in index method from python.
    Example list [1,3,5,7,9] target = 3 returned value would be 1 because 3 can be
    found at the first index.
    Example list [3, 7, 8, 1, 0, 1, 12] target = 1 a return of either 3 or 5 would
    be valid.
    Example list [1,3,5,6,9] target 7 returns -1 because 7 is not within the list.
    :param list:
    :param target:
    :return:
    """
    for i in range(len(list)):
        if list[i] == target:
            return(i)
    return(-1)


def removeLowest(list):
    """
    Given a list of numbers remove the lowest element from the list. You may assume the list is at least 1 element long.
    If there are multiple of the lowest number you just need to remove 1.
    Example list [3,6,7,2,12] would become [3,6,7,12]
    :param list:
    :return:
    """
    x = 0
    for i in range(len(list)):
        if list[i] < list[x]:
            x = i
    list.pop(x)
    return(list)


def keepOrder(list: list, value):
    """
    Given a list of numbers that is in order and a value. Place the value into the
    list such that the list is still in order.
    Example list=[1,3,5,6] value =4 the resulting list would be [1,3,4,5,6]
    :param list:
    :param value:
    :return:
    """
    for i in range (len(list)):
        if value > list[-1]:
            list.append(value)
        elif value < list[0]:
            list.insert(0,value)
        elif list[i] < value and value < list[i+1]:
            list.insert(i+1,value)
    return(list)

import itertools
def merge(list1:list, list2:list):
    """
    Given two lists that are in order. produce a new list that is the two lists merged together and in order.
    Make sure to now modify either of the original lists.
    Example l1 = [1,3,5] l2 = [2,4,6,8] -> [1,2,3,4,5,6,8]
    :param l1:
    :param l2:
    :return:
    """
    listMerge = list1.copy()
    i = 0
    i2 = 0
    while len(listMerge) < len(list1) + len(list2):
        if list2[i2] > list1[-1]:
            listMerge.append(list2[i2])
            i2 += 1
        elif listMerge[i] < list2[i2] and list2[i2] < listMerge[i + 1]:
            listMerge.insert(i+1,list2[i2])
            i2 += 1
        else:
            i += 1
    return(listMerge)
