def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print("iterate_sum:",sum([1,2,3,4]))


def sum_recur(arr):
    if arr ==[]:
        return 0
    return arr.pop(0)+sum_recur(arr)
print("recursive_sum:",sum_recur([1,2,3,4]))

def sum_tail_recur(total,arr):
    if arr == []:
        return total
    return sum_tail_recur(total+arr.pop(0),arr)
print("recursive_sum:",sum_tail_recur(0,[1,2,3,4]))