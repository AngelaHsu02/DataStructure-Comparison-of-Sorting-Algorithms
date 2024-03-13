''' Python implementation of QuickSort using Hoare's 
partition scheme. '''

''' This function takes first element as pivot, and places 
	all the elements smaller than the pivot on the left side 
	and all the elements greater than the pivot on 
	the right side. It returns the index of the last element 
	on the smaller side '''

def partition(arr, low, high):
	mid = (low + high) // 2  # use the middle element as pivot
	pivot = arr[mid]
	i = low - 1
	j = high + 1
	while (True):
		i += 1
		while (arr[i] < pivot):
			i += 1
		j -= 1
		while (arr[j] > pivot):
			j -= 1
		# If two pointers met.
		if (i >= j):
			return j
		arr[i], arr[j] = arr[j], arr[i]

def quickSortHoare(arr, low, high):
	''' pi is partitioning index, arr[p] is now at right place '''
	while (low < high):
		pi = partition(arr, low, high)
		if pi - low < high - pi:
			quickSortHoare(arr, low, pi)
			low = pi + 1
		else:	
			quickSortHoare(arr, pi + 1, high)
			high = pi
		

''' Function to print an array '''
def printArray(arr, n):
	for i in range(n):
		print(arr[i], end=" ")
	print()


# Driver code
if __name__ == '__main__':
	arr = [10, 7, 8, 9, 1, 5]
	n = len(arr)
	quickSortHoare(arr, 0, n - 1)
	print("Sorted array:")
	#printArray(arr, n)
	print(arr)