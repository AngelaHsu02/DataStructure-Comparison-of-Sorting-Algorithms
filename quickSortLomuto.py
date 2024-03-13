''' Python3 implementation QuickSort using Lomuto's partition 
Scheme.'''

''' This function takes last element as pivot, places 
the pivot element at its correct position in sorted 
	array, and places all smaller (smaller than pivot) 
to left of pivot and all greater elements to right 
of pivot '''


def partition(arr, low, high):
	pivot = arr[high] #pivot is the last element in the array
	i = (low - 1)
	for j in range(low, high):
		# If current element is smaller than or equal to pivot
		if (arr[j] <= pivot):
			# increment index of smaller element
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)


''' The main function that implements QuickSort 
arr --> Array to be sorted, 
low --> Starting index, 
high --> Ending index '''
def quickSortLomuto(arr, low, high):
	while (low < high):
		''' pi is partitioning index, arr[p] is now at right place '''
		pi = partition(arr, low, high)
		if pi - low < high - pi:
			quickSortLomuto(arr, low, pi - 1)
			low = pi + 1
		else:
			quickSortLomuto(arr, pi + 1, high)
			high = pi - 1


''' Function to print an array '''
#def printArray(arr, size):
#	for i in range(size):
#		print(arr[i], end=" ")
#	print()


if __name__ == '__main__':
	arr = [10, 7, 8, 9, 1, 5]
	print('org:',arr)
	n = len(arr)
	quickSortLomuto(arr, 0, n - 1)
	print("Sorted array:",arr)
	#printArray(arr, n)