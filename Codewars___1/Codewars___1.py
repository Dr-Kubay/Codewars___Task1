# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def getCount(inputStr):
    sum = 0
    for el in inputStr:
        if el in 'aeiou':
            sum += 1
        else:
            pass
    return sum