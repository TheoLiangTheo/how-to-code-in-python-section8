numbers  = [[12,3,5,4],[67,7,5,3],[5,7,3,2],[4,6,5,8],[5,3,2,4],[5,7,8,9],[0,9,2,3],[6,4,6,2],[4,5,7,86],[7,4,4,6]]
ocurrence = 0
target = int(input('state the value to count:'))
for outerloop in range(len(numbers)):
    for innerloop in range(len(numbers[outerloop])):
        if numbers[outerloop][innerloop] == target:
            ocurrence = ocurrence + 1
print(target,'appeared',ocurrence,'times')