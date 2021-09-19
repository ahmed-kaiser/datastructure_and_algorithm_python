# implementation of counting sort
# take 2 parameter array and max value of the array

def counting_sort(arrToSort, max_value):
    lenOfArr = len(arrToSort)
    temp_arr = [0] * (max_value + 1)

    # count value from main list
    for i in range(lenOfArr):
        temp_arr[arrToSort[i]] = temp_arr[arrToSort[i]] + 1

    # cumulative addition
    for i in range(1, len(temp_arr)):
        temp_arr[i] = temp_arr[i] + temp_arr[i-1]

    sortedArr = [0] * lenOfArr # sortedArr keep the sorted value

    # place the element from main list to sorted list
    i = lenOfArr - 1
    while i >=0:
        temp_arr[arrToSort[i]] -= 1
        sortedArr[temp_arr[arrToSort[i]]] = arrToSort[i]
        i -= 1

    return sortedArr


if __name__ == '__main__':
    array = [
        [9, 7, 2, 12, 8, 15, 5, 9, 3],
        [4, 9, 11, 2, 0, 3],
        [2, 45, 11, 8, 5, 33, 21, 1],
        [3],
        [5, 22, 9, 1, 5, 0, 3, 5, 1, 0, 4, 11, 2, 3]
    ]
    for n in array:
        m = max(n)
        print(counting_sort(n, m))
