def findmaxposition(maxlist):
    maximum = maxlist[0]
    position = 0
    for counter in range(1,len(maxlist)):
        if maxlist[counter] > maximum:
            maximum = maxlist[counter]
            position = counter
    return position
names = ['Agattha','Elsebe','Ranneigh','Kolka','Magga']
ages = [22,33,51,49,18]
print('oldest person is', names[findmaxposition(ages)])