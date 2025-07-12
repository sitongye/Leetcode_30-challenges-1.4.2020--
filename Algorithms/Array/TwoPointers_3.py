# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

def combine_arry(sorted_arr1, sorted_arr2):
    i = j = 0
    ouput_arr = []
    while i < len(sorted_arr1) and j < len(sorted_arr2):
        if sorted_arr1[i] <= sorted_arr2[j]:
            output_arr.append(sorted_arr1)
            i += 1
        else:
            output_arr.append[j]
            j += 1
    # if any of the array is not till the end, then append them till the end
    while i < len(sorted_arr1):
        ans.append(arr1[i])
        i += 1
    while j < len(sorted_arr2):
        ans.append(arr1[j])
        j += 1
    
    return output_arr


# Time complexity O(n)
# Space Complexity O(1)
    

        