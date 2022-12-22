# assignment2


#soln 1
a="python is a case sensitive language"
print("length of string=",len(a))
print(a[::-1])
b=a[10:26:1]
print(b)
replaced=a.replace("a case sensitive","object oriented")
print(replaced)
print(a.index("a"))
print(a.replace(" ",""))
     

#soln 2
name = "ABC"
SID = "2210XXXX"
department = "XYZ"
CGPA = 9.9
print("Hey,", name, "Here!\nMy SID is", SID, "\nI am from", department, "department and my CGPA is", CGPA)

     

#soln 3
a = 56
b = 10
print("a. a & b =", a&b)
print("b. a | b =", a|b)
print("c. a ^ b =", a^b)
print("d. Left shifting a and b with 2 bits =",a<<2,"and",b<<2)
print("e. Right shifting a with 2 bits and b with 4 bits=",a>>2,"and",b>>4)

     

#soln 4
 a=int(input("enter the first number:"))
 b=int(input("enter the second number:"))
 c=int(input("enter the third number:"))

 if (a>b and a>c):
     print(a,"is greatest")
 elif (b>a and b>c):
      print(b,"is greatest")
 else :
      print(c,"is greatest")         
     

#soln 5
str = input("Enter the string: ")
if "name" in str:
    print("Yes")
else:
    print("No")
     

#soln 6
a = int(input("enter the first side length of triangle:"))
b = int(input("enter the second side length of triangle:"))
c = int(input("enter the third side length of triangle:"))

if (a+b>c and a+c>b and b+c>a):
    print("yes")

else :         
      print("no")           
