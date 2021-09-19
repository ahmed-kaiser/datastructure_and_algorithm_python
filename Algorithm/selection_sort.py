# implementation of selection sort algorithm
def selection_sort(item_list):
    lenOfList = len(item_list)

    for i in range(lenOfList - 1):
        min_index = i # track index of minimum item
        for j in range(i+1, lenOfList):
            if item_list[j] < item_list[min_index]:
                # min value found
                min_index = j

        if min_index != i:
            item_list[i], item_list[min_index] = item_list[min_index], item_list[i]
        
if __name__ == '__main__':
    n = [22, 7, 2, 12, 8, 15, 5, 9, 3]
    selection_sort(n)
    print(n)
