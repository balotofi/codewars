''' Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
348597 => [7,9,5,8,4,3]
0 => [0]
'''

def digitize(number):
    digits = [int(n) for n in str(number)]
    arr = digits[::-1]
    print(arr)

# digitize(2384394)
# digitize(2384)
# digitize(4394)
# digitize(234564654694)
# digitize(2000587314)