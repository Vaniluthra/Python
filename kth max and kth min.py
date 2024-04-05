def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

my_array = list(map(int,input('enter space separated list elements:').split()))
sorted_array = quicksort(my_array)
k=int(input('enter k:'))

distinct = [sorted_array[0]]
for i in range(1, len(sorted_array)):
    if sorted_array[i] != sorted_array[i-1]:
        distinct.append(sorted_array[i])

print(distinct[-k], distinct[k-1])
