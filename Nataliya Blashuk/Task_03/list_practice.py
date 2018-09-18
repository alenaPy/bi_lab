"""Completed task 1.List practice from labwork3."""

# 1.1
xList = ["a", "b"]
yList = ["b", "c", "d"]
list1 = [x + y for x in xList for y in yList]
print(list1)

# 1.2
list2 = list1[::2]
print(list2)

# 1.3
nList = [str(i) for i in range(1, 5)]
aList = ["a"]
list3 = [n + a for n in nList for a in aList]
print(list3)

# the second variant of the 1.3
nList = [str(i) for i in range(1, 5)]
list3 = [n + "a" for n in nList]
print(list3)

# the third variant of the 1.3
nList = ",".join([str(i) for i in range(1, 5)])
list3 = [n + "a" for n in nList[::2]]
print(list3)

# 1.4
print(list3.pop(1))

# 1.5
list4 = list3.copy()
print(list4)
list4.insert(1, "2a")
print(list4)
