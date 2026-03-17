My_set={1,2,3,"Seema"}
print(My_set)
print(My_set) #order is not preserved in set
My_set1={1,2,2,3}
print(My_set1) #duplicate values are not allowed in set

#Define set and add one element
newSet={1,2,5}
print(newSet)
newSet.add(6)
print(newSet)
#newSet.append(7) #append is not used for set
newSet.add(7)
print(newSet)

#perform operations: remove pop discard clear
newSet.pop()
print(newSet)
newSet.remove(5)
print(newSet) 
newSet.discard(6)
print(newSet)
newSet.clear()
print(newSet)


#check the element is exist in set or not
newSet={1,2,5}
a=input("Enter any element:")
if a in newSet: 
  print("It is present")
else:
  print("It is not present")

#define 2 sets and tell difference between 2 sets
A={2,6,9,7}
B={5,10,66}
print(A.difference(B))

#find common elements in 2 sets
print(A.intersection(B))
print(A&B) #using and operator
print(A and B) #and is logical=> used for string, char
                      # bitwise => used for int, float

#check if one set is subset of another 
A={5,8,6,9,1,2}
B={5,1,2}
print(B.issubset(A))
print(A.issubset(B))
#another method without subset
print(B<=A)

s1={10,20,30,40}
s2={20}
print(s2.issubset(s1))
print(s2<=s1)
