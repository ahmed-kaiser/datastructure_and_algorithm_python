# implementation of insertion sort
def insertion_sort(listToSort):
    lenOfList = len(listToSort)
    
    for i in range(1, lenOfList):
        temp = listToSort[i]
        j = i # j help to track previous index in the while loop

        while j > 0 and temp < listToSort[j-1]:
            listToSort[j] = listToSort[j-1]
            j -= 1

        listToSort[j] = temp


if __name__ == '__main__':
    array = [
        [22, 7, 2, 12, 8, 15, 5, 9, 3],
        [],
        [4, 9, 11, 2, 0, 3],
        [2, 45, 11, 8, 5, 33, 21, 1],
        [4]
    ]

    for n in array:
        insertion_sort(n)
        print(n)
