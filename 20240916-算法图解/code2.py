# Chapter 2  P28 O(n_square)

# 先前置一个函数
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i]< smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))    #array.pop头回见。  list.pop(index) 输出那个值，同时让list删掉了那个值，一个函数达成两个动作，也就是pop！
    return newArr


print(selectionSort([5,3,6,2,10]))