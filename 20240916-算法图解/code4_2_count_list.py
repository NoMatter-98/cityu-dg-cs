def count_list(arr):
    if arr == []:
        return 0
    arr.pop(0)
    return 1+count_list(arr)

def count_list_tail_recur(arr,count=0):
    if arr == []:
        return count
    arr.pop(0)
    count += 1
    return count_list_tail_recur(arr,count)

print("count_list:",count_list([1,2,3,4]))
print("count_list_tail_recursive:",count_list_tail_recur([1,2,3,4]))
