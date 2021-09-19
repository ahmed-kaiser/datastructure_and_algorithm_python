# Implementation of bubble sort algorithm
def bubble_sort(listToSort):
    lenOfList = len(listToSort)

    for i in range(lenOfList):
        change = False
        for j in range(lenOfList - i - 1):
            if listToSort[j] > listToSort[j+1]:
                listToSort[j] ,listToSort[j+1] = listToSort[j+1], listToSort[j]
                change = True
        
        if change is False:
            # if no swap happen
            break


if __name__ == '__main__':
    array = [
        [22, 7, 2, 12, 8, 15, 5, 9, 3],
        [],
        [4, 9, 11, 2, 0, 3],
        [2, 45, 11, 8, 5, 33, 21, 1],
        [4]
    ]

    for n in array:
        bubble_sort(n)
        print(n)
