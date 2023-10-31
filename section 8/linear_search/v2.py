def checknames(target, namelist):
    index = -1
    for names in range(len(namelist)):
        if namelist[names] == target:
            index = names
        return index
names = ['Najwa', 'Dimitry', 'Maria', 'Selina', 'Riccardo']
targetname = str(input("Enter a name:"))
position = checknames(targetname,names)
if position >= 0:
    print(names[position], 'found in list')
    print("at position",position)
else:
    print('name not found')