# implementation of radix sort algorithm
def counting_sort(arrToSort, place):
    lenOfArr = len(arrToSort)
    temp_arr = [0] * 10

    # count value from main list
    for i in range(lenOfArr):
        index = arrToSort[i] // place
        temp_arr[index % 10] += 1

    # cumulative addition
    for i in range(1, len(temp_arr)):
        temp_arr[i] = temp_arr[i] + temp_arr[i-1]

    sortedArr = [0] * lenOfArr

    # place the element from main list to sorted list
    i = lenOfArr - 1
    while i >=0:
        index = arrToSort[i] // place
        temp_arr[index % 10] -= 1
        sortedArr[temp_arr[index % 10]] = arrToSort[i]
        i -= 1

    for i in range(lenOfArr):
        arrToSort[i] = sortedArr[i]


def radix_sort(arrToSort):
    max_item = max(arrToSort)

    place = 1
    while max_item // place > 0:
        counting_sort(arrToSort, place)
        place *= 10


if __name__ == '__main__':
    data_list = [
        [121, 432, 564, 23, 13, 45, 788],
        [334, 56, 76, 555, 67, 223, 56, 823, 112],
        [7],
        [678, 44, 2, 34, 678, 212, 44, 2]
    ]
    
    for data in data_list:
        radix_sort(data)
        print(data)
