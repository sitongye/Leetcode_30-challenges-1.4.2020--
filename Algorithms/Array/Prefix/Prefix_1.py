#Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

#For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def Solution(nums, queries, limit):
    prefix = []
    curr_sum = 0
    for num in nums:
        curr_sum += num
        prefix.append(curr_sum)
    result = [prefix[query[0]] - prefix[query[1]] + nums[query[0]] < limit for query in queries]
    return result

