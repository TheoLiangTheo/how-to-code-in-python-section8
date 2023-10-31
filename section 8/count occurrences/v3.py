def countocurrences(filename, targetnumber):
    ocurrences = 0
    filename = filename + '.txt'
    with open(filename) as nums:
        for each in nums.readines():
            each = each[0:-1]
            if int(each) == targetnumber:
                ocurrences = ocurrences + 1
    return ocurrences
file = 'numbers'
target = int(input("state the value to count:"))
total = countocurrences(file, target)
print(target,'appeared',ocurrence,'times')