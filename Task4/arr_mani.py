#D:\Task4

def merge_intervals(lst):
    if not lst:
        return []

    lst.sort(key=lambda x: x[0])
    res = [lst[0]]

    for i in lst[1:]:
        last = res[-1]
        if i[0] <= last[1]:
            last[1] = max(last[1], i[1])
        else:
            res.append(i)

    return res

# Test Case 1: Basic overlapping intervals
test1 = [[1,3],[2,6],[8,10],[15,18]]
result1 = merge_intervals(test1)
# Expected: [[1,6],[8,10],[15,18]]
# Test Case 2: Adjacent intervals (touching endpoints)
test2 = [[1,4],[4,5]]
result2 = merge_intervals(test2)
# Expected: [[1,5]]
# Test Case 3: Completely contained intervals
test3 = [[1,4],[2,3]]
result3 = merge_intervals(test3)
# Expected: [[1,4]]
# Test Case 4: No overlapping intervals
test4 = [[1,2],[3,4],[5,6]]
result4 = merge_intervals(test4)
# Expected: [[1,2],[3,4],[5,6]]
# Test Case 5: All intervals overlap
test5 = [[1,4],[2,5],[3,6]]
result5 = merge_intervals(test5)
# Expected: [[1,6]]
# Test Case 6: Unsorted input
test6 = [[6,7],[2,4],[5,9]]
result6 = merge_intervals(test6)
# Expected: [[2,4],[5,9]]
# Test Case 7: Single interval
test7 = [[1,4]]
result7 = merge_intervals(test7)
# Expected: [[1,4]]
# Test Case 8: Complex overlapping case
test8 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
result8 = merge_intervals(test8)
# Expected: [[1,10]]


print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)