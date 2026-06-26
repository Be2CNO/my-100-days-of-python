# List
countings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(countings[0])
print(countings[3])
print(countings[-1])
print(countings[-5])
countings[2] = 33
print(countings[2])

countings.extend([22,44443,5435,535,2,2,35,75,67,6,768,76,96,765,45,654,453,344,4,3,23,23,321,4,5,6465,76,56,7,657,767,665,7])
print(countings)
length = len(countings)
print(length)
C = countings.clear()
print(C)


#List Inside List
list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11,12,13,14]
list = [list1 , list2]
print(list)