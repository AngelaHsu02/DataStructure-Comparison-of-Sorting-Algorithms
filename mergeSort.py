# Python program for implementation of MergeSort # 沒有開新array?
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)  # 切到LR都只剩一個元素

        i = j = k = 0
        # Copy data to new arrays #從L[0]R[0]開始比，小的放進arr，index++
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):  # Checking if any element was left #比完剩下的放進arr
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



# Code to print the list
#def printList(arr):
    #for i in range(len(arr)):
    #    print(arr[i], end=" ")
    #print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    #printList(arr)
    print(arr)


    mergeSort(arr)
    print(arr)
    # print("\nSorted array is ")
    #printList(arr)
