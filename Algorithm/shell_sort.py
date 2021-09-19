# implementation of shell sort
def shell_sort(arrToSort):
    lenOfArr = len(arrToSort)
    n = lenOfArr // 2 # n is for interval 

    while n > 0:
        for i in range(n, lenOfArr):
            temp = arrToSort[i]
            j = i
            while j >= n and arrToSort[j - n] > temp:
                arrToSort[j] = arrToSort[j - n]
                j -= n

            arrToSort[j] = temp

        n = n // 2


if __name__ == '__main__':
    array = [
        [22, 7, 2, 12, 8, 15, 5, 9, 3],
        [],
        [4, 9, 11, 2, 0, 3],
        [2, 45, 11, 8, 5, 33, 21, 1],
        [3]
    ]
    for n in array:
        shell_sort(n)
        print(n)

