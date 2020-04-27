largestOddNumber = 0
count = 10
while count > 0:
    number = int(input('Enter Number: '))
    if number%2 !=0:
        if number>largestOddNumber:
            largestOddNumber = number
    count -= 1

if largestOddNumber == 0:
    print('No Odd Numbers')
else:
    print(largestOddNumber, 'is the largest Odd Number')


