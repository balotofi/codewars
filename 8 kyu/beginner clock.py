''' Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000

Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
'''

def past(h, m, s):
    while 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        hour = h*3600000
        minute = m*60000
        seconds = s*1000
        result = hour+minute+seconds
        return result
    return "value not in range"