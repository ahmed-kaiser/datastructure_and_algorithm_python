# implementation of quick sort
def partition(listToSort, x, y):
    pivot = x
    start = x
    end = y

    while start < end:
        # search max value from left towards right
        while listToSort[pivot] > listToSort[start]:
            start += 1

        # search min value from right towards left
        while listToSort[pivot] <= listToSort[end]:
            end -= 1

        if start < end:
            listToSort[start], listToSort[end] = listToSort[end], listToSort[start]

    listToSort[pivot], listToSort[end] = listToSort[end], listToSort[pivot]

    return end # return partition index



def quick_sort(listToSort, s, e):
    # s hold start index value
    # e hold end index value
    if s < e:
        p = partition(listToSort, s, e)
        quick_sort(listToSort, s, p-1) # call for left list
        quick_sort(listToSort, p+1, e)  # call for right list



if __name__ == '__main__':
    n = [9, 7, 2, 12, 8, 15, 5, 9, 3]
    lenOfList = len(n)
    quick_sort(n, 0, lenOfList-1)
    print(n)
    # array_list = [
    #     [9, 7, 2, 12, 8, 15, 5, 9, 3],
    #     [4, 9, 11, 2, 0, 3],
    #     [22, 7, 2, 12, 8, 15, 5, 9, 3, 11],
    #     [3],
    #     [5, 22, 9, 1, 5, 0, 3, 5, 1, 0, 4, 11, 2, 3]
    # ]
    
    # for n in array_list:
    #     l = len(n)
    #     quick_sort(n, 0, l-1)
    #     print(n)
