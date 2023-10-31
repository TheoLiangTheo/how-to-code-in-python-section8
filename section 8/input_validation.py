number = int(input('please input a number between 0 and 10:'))
while number < 0 or number > 10:
    print('invalid number')
    number = int(input('please input a number between 0 and 10:'))
print('number is',number)