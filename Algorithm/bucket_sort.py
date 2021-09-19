def bucket_sort(arrToSort):
    lenOfArr = len(arrToSort)
    bucket = []

    # create sub_bucket inside bucket 
    bucket = [[] for _ in range(lenOfArr)]

    # add items in to sub_bucket based on integer part
    for item in arrToSort:
        index = int(item*10)
        bucket[index].append(item) 
    
    # sort all the sub bucket
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])

    k = 0 # track the sorted list index
    # copy all the sorted item from sub bucket to sorted array
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            arrToSort[k] = bucket[i][j]
            k += 1

if __name__ == '__main__':
    array_list = [
        [.42, .32, .33, .52, .37, .47, .51],
        [.22, .11, .2, .112, .45, .11, .34, .19]
    ]

    for array in array_list:
        bucket_sort(array)
        print(array)

