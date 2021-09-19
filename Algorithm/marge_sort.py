# implementation of marge sort algorithm
def marge(listToSort, left, right):
    lenOfLeft = len(left)
    lenOfRight = len(right)

    i=j=k=0
    # i track index of left list
    # j track index of right list
    # k track index of main list

    while i < lenOfLeft and j < lenOfRight:
        if left[i] > right[j]:
            listToSort[k] = right[j]
            j +=1
        else:
            listToSort[k] = left[i]
            i +=1 
     
        k += 1

    while i < lenOfLeft:
        listToSort[k] = left[i]
        i += 1
        k += 1

    while j < lenOfRight:
        listToSort[k] = right[j]
        j += 1
        k += 1


def marge_sort(listToSort):
    lenOfList = len(listToSort)

    if lenOfList <= 1:
        return lenOfList

    mid = lenOfList // 2
    leftList = listToSort[:mid]
    rightList = listToSort[mid:]

    marge_sort(leftList)
    marge_sort(rightList)
    marge(listToSort, leftList, rightList)


if __name__ == '__main__':
    array_list = [
            [9, 7, 2, 12, 8, 15, 5, 9, 3],
            [4, 9, 11, 2, 0, 3],
            [22, 7, 2, 12, 8, 15, 5, 9, 3, 11],
            [3],
            [5, 22, 9, 1, 5, 0, 3, 5, 1, 0, 4, 11, 2, 3]
        ]
        
    for n in array_list:
        marge_sort(n)
        print(n)

