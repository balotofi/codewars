'''Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz
'''




def longest(a1, a2):
    listA1 = [x for x in a1]
    listA2 = [n for n in a2]
    fullList = listA1 + listA2 
    newList = []
    for letter in fullList:
        if letter not in newList:
            newList.append(letter)
        
    return ''.join(sorted(newList))
