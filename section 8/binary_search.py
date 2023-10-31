def binarysearch(namelist,target):
    lower = 0
    upper = len(namelist)-1
    while lower<=upper:
        mid = int((lower+upper)/2)
        if namelist[mid] == target:
            return mid
        elif namelist[mid] < target:
            lower = mid+1
        else:
            upper = mid-1
    return -1
names = ['Aaron','Beth','Clive','Dennis','Edgbert','Francis','Gillian','Hugh','Icarus','Jeremy','Kyle','Lachina']
ages = [33,56,34,56,75,34,24,87,34,44,50,40]
tofind = str(input('enter name of person you want to find:'))
position = binarysearch(names,tofind)
if position >= 0:
    print(names[position],'is',ages[position],'years old')
else:
    print('name not found')