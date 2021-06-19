# how many matches do you have from the list

mylist = [2, 4, 43, 17, 21, 7]
mylist2 = [13, 21, 17, 30, 3, 5]

mylist.sort()
mylist.sort()

result = set(mylist).intersection(set(mylist2))
print(result)


list1 = [1, 3, 5, 23, 21, 11]
list2 = [32, 21, 12, 34, 41, 2]

list1.sort()
list2.sort()

newlist = []

for x in list1:
    if x in list2:
        newlist.append(x)
print(newlist)
