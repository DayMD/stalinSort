import random
unsortedList = []
sortedList = []

for i in range (0, 100):
    rand = random.randint(0,1000)
    unsortedList.append(rand)

print("Unsorted list")
print(unsortedList)

sortedList.append(unsortedList[0])
x = 1
                  
while x < len(unsortedList):
    print(unsortedList[x])
    if unsortedList[x] > sortedList[-1]:
        sortedList.append(unsortedList[x])
    x += 1
    
print("Sorted List")
print(sortedList)
