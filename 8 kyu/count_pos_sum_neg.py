''' Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''

def count_positives_sum_negatives(arr):
    '''count positives in array and sum negatives'''
    pos = [ x for x in arr if x>0]
    neg = [x for x in arr if x<0]
    count = []
    
    count.append(len(pos))
    count.append(sum(neg))
    if len(arr) !=0:
        return count
    else:
        return []