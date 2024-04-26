'''
Description
Program to find union and intersection of 2 arrays
'''
def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end=" ")
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j], end=" ")
            j += 1
        else:
            print(arr2[j], end=" ")
            j += 1
            i += 1
    while i < m:
        print(arr1[i], end=" ")
        i += 1
    while j < n:
        print(arr2[j], end=" ")
        j += 1
def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j], end=" ")
            j += 1
            i += 1
arr1 = list(map(int, input('Enter space separated list elements:').split()))
arr2 = list(map(int, input('Enter space separated list elements:').split()))
m = len(arr1)
n = len(arr2)
printUnion(arr1, arr2, m, n)
printIntersection(arr1, arr2, m, n)
