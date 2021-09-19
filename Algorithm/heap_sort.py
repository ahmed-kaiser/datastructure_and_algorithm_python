# implementation of heap sort algorithm
# max heap

def heapify(arrToSort, lenOfArr, root):
    leftChild = 2*root + 1
    rightChild = 2*root + 2

    if leftChild < lenOfArr and arrToSort[leftChild] > arrToSort[root]:
        arrToSort[root], arrToSort[leftChild] = arrToSort[leftChild], arrToSort[root]
        heapify(arrToSort, lenOfArr, leftChild)

    if rightChild < lenOfArr and arrToSort[rightChild] > arrToSort[root]:
        arrToSort[root], arrToSort[rightChild] = arrToSort[rightChild], arrToSort[root]
        heapify(arrToSort, lenOfArr, rightChild)


def max_heap(arrToSort, lenOfArr):
    root_index = lenOfArr//2 - 1

    while root_index >= 0:
        heapify(arrToSort, lenOfArr, root_index)
        root_index -= 1


def heap_sort(arrToSort, lenOfArr):
    max_heap(arrToSort, lenOfArr)

    while lenOfArr > 1:
        arrToSort[0], arrToSort[lenOfArr-1] = arrToSort[lenOfArr-1], arrToSort[0]
        lenOfArr -= 1
        heapify(arrToSort, lenOfArr, 0)


if __name__ == '__main__':
    array_list = [
            [9, 7, 2, 12, 8, 15, 5, 9, 3],
            [4, 9, 11, 2, 0, 3],
            [22, 7, 2, 12, 8, 15, 5, 9, 3, 11],
            [3],
            [5, 22, 9, 1, 5, 0, 3, 5, 1, 0, 4, 11, 2, 3]
        ]
        
    for n in array_list:
        l = len(n)
        heap_sort(n, l)
        print(n)

