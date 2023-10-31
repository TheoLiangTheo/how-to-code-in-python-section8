total = 0
items = int(input('enter number of items:'))
for count in range(items):
    temp = int(input('enter value '+str(count+1)+':'))
    total = total + temp
print("the total =",total)