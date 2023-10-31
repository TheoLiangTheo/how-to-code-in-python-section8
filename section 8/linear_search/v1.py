def checknames(target, nameList):
    found = False
    for names in nameList:
        if names  == target:
            found = True
    return found

names = ['Najwa', 'Dimitry', 'Maria', 'Selina', 'Riccardo']
targetname = str(input("Enter a name:"))
result = checknames(targetname,names)
if result:
    print('Name found in list')
else:
    print('name not found')