import random
testSet = set()
while len(testSet) < 999999:
    testSet.add(random.randint(1, 999999))
print(testSet)
