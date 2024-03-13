#def partition3(a, l, r):
#   x, j, t = a[l], l, r
#   i = j

#   while i <= t:
#      if a[i] < x:
#         a[j], a[i] = a[i], a[j]
#         j += 1

#      elif a[i] > x:
#         a[t], a[i] = a[i], a[t]
#         t -= 1
#         i -= 1  # remain in the same i in this case
#      i += 1
#   return j, t


#def randomized_quick_sort(a, l, r):
#    if l >= r:
#        return
#    k = random.randint(l, r)
#    a[l], a[k] = a[k], a[l]
#    m1, m2 = partition3(a, l, r)
#    randomized_quick_sort(a, l, m1 - 1)
#    randomized_quick_sort(a, m2 + 1, r)


#def partition(arr, pivot):
#    less, equal, greater = [], [], []
#    for val in arr:
#        if val < pivot:
#           less.append(val)
#        elif val == pivot:
#           equal.append(val)
#        elif val > pivot:
#           greater.append(val)
#    return less, equal, greater


#def quickSort3way(arr, max_depth=None):
#    # 如果 max_depth 未提供，则将其设为正无穷大
#    if max_depth is None:
#        max_depth = float('inf')

#    # 如果数组长度小于等于 1 或者递归深度达到最大值，直接返回数组
#    if len(arr) <= 1 or max_depth == 0:
#        return arr
#    pivot = arr[0]
#    less, equal, greater = partition(arr, pivot)
#    return quickSort3way(less) + equal + quickSort3way(greater)

#if __name__ == '__main__':
#	arr = [10, 7, 8, 9, 1, 5]
#	n = len(arr)
#	quickSort3way(arr)
#	print("Sorted array:")
#	print(quickSort3way(arr))

def quickSort3way(arr, low, high):
    if low < high:
        pivot = arr[low]
        left, right, i = low, high, low + 1

        while i <= right:
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                i += 1
                left += 1
            elif arr[i] > pivot:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            else:
                i += 1

        quickSort3way(arr, low, left - 1)
        quickSort3way(arr, right + 1, high)


#if __name__ == '__main__':
#	arr = [10, 7, 8, 9, 1, 5]
#	n = len(arr)
#	quickSort3way(arr, 0, n - 1)
#	print("Sorted array:")
