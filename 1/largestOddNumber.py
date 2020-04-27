x, y, z  = 1, 11, 9 

largestOddNumber = None

if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print('No odd Numbers')
else:
    if x%2 != 0:
        if y%2 != 0:
            if x>y:
                largestOddNumber = x
            else:
                largestOddNumber = y
        else:
            largestOddNumber = x
    else:
        if y%2 != 0:
            largestOddNumber = y
    if z%2 !=0:
        if z > largestOddNumber:
            largestOddNumber = z
if largestOddNumber != None:
    print(largestOddNumber, 'is the largest odd number')

