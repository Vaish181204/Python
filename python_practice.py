#Arithmetic Operators
a=5
b=6
print(a+b)
print(a-b)

#Assignment Operators
a=5 
a+=3
print(a)
b=10
b-=2
print(b)

#Comparison Operators
a=5
b=6 
print(a==b)
print(a!=b)

#Logical Operators
a=5
b=6
print(a>3 and b>5)
print(a>3 or b<5)

#Bitwise Operators
a=5
b=3 
print("Bit1",a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR

#Membership Operators
my_list = [1, 2, 3, 4, 5]       
print(3 in my_list)  # True
print(6 in my_list)  # False

#Identity Operators
a = [1, 2, 3]   
b = a
print(a is b)  # True
c = [1, 2, 3]
print(a is c)  # False

#Ternary Operator
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: Even    