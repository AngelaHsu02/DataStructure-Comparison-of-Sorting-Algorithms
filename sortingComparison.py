import random
import timeit
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSortLomuto import quickSortLomuto
from quickSortHoare import quickSortHoare
from quickSort3way import quickSort3way
from countingSort import countingSort
import sys
import cProfile

def runSortingAlgorithm(algorithm, arr):
    return timeit.timeit(lambda: algorithm(arr), number=numTrials) / numTrials

def generateArraySize(size):
    return [random.randint(0, size-1) for s in range(size)]

def generateArrayElementRange(k):
    return [random.randint(0, k-1) for s in range(2**13)]

def random_swap(arr, swap):
    for s in range(swap):
        i, j = random.sample(range(len(arr)), 2)
        arr[i], arr[j] = arr[j], arr[i]
        # print(f"Swap {s+1}:", arr)
    return arr

'''To compare algorithms, the following are 3 kinds of output and 
we can use each output to run the main separately.'''

if __name__ == '__main__':
    numTrials = 10    
    # First input
    sizes = [2**i for i in range(10, 31)]
    for size in sizes:
        arr = generateArraySize(size)
    
    #The second input   
    swaps = [2**i for i in range(0, 21)]
    for swap in swaps:
        sortedArray = list(range(2**13))
        arr = random_swap(sortedArray, swap)
        #print(f"Original array (swap times {swap}):", arr)

    # The third input
    ks = [2**i for i in range(0, 21)]
    for k in ks:
        arr = generateArrayElementRange(k)
        #print(f"Original array (element range 0~{k}):", arr)

        averageInsertionSortTime = runSortingAlgorithm(insertionSort, arr.copy())
        averageMergeSortTime = runSortingAlgorithm(mergeSort, arr.copy())
        averageQuickSortLomutoTime = runSortingAlgorithm(lambda arr: quickSortLomuto(arr, 0, len(arr) - 1), arr.copy())
        averageQuickSortHoareTime = runSortingAlgorithm(lambda arr: quickSortHoare(arr, 0, len(arr) - 1), arr.copy())
        averageQuickSort3wayTime = runSortingAlgorithm(lambda arr: quickSort3way(arr, 0, len(arr) - 1), arr.copy())
        averageCountingSortTime = runSortingAlgorithm(countingSort, arr.copy())

        print(f"size{size}, {averageInsertionSortTime}, {averageMergeSortTime}, {averageQuickSortLomutoTime}, {averageQuickSortHoareTime}, {averageQuickSort3wayTime}, {averageCountingSortTime}")
        print(f"swap times {swap}, {averageInsertionSortTime}, {averageMergeSortTime}, {averageQuickSortLomutoTime}, {averageQuickSortHoareTime}, {averageQuickSort3wayTime}, {averageCountingSortTime}")
        print(f"element range 0~{k}, {averageInsertionSortTime}, {averageMergeSortTime}, {averageQuickSortLomutoTime}, {averageQuickSortHoareTime}, {averageQuickSort3wayTime}, {averageCountingSortTime}")