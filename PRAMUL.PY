'''# print ("kxak")
# # for i in range(0,100):
# #     print ("gaurab\n")
# print("k xa???")
# x = complex(9,2)
# z = 9;
# q = "pri"
# w="nt"
# d = None
# print("the tye of z: ", x, type(x))
# print("the tye of q: ", type(d))

# print(q+w)
# print(5)
# print("joy", 5 , 6, sep ="-", end = "007")
# # """ = comment
# # # cmd + / = ekaichoti comment
# # # option  + down key to move line''''''
# # \"escape character "\
# # """


# # print(5*2)
# # print(5/2) #2.5
# # print(5//2) #2
# # print(5**3)#5*5*5 
# # # a = int(input("enter a number"))
# # b = int(input("enter another num"))
# # if b == 1:
# #     print("samar")
# # elif b ==2:
# #     print("sudip")
# # else:
# #     print("pramul")

# # c = int(input("Enter a number: "))
# # f = str(input("enter the operatij: "))
# # g = int(input("Enter another number: "))
# # match f:
# #     case '+':
# #         print(c + g)
# #     case '*':
# #         print(c * g)
# #     case '-':
# #         print(c - g)
# #     case '/':
# #         print(c / g)
# #     case _:
# #         print("invalid")
# # appple = jhdsbfkjhbdshjkfbhjkwe flu iufh
# # fjguwe bhfiouhiuf
# #  hnoiuyhfiuer
# #   hfiuerhgi
# # for s in appple:
# #     print(s)
    
# # m = "harrycode123213"
# # print(len(m))
# # print(m[-4:-2])

# # print(m.upper())
# # print(m.lower())
# # print(m.rstrip("!"))
# # print(m.replace("harry", "jhon"))
# # print(m.split(" "))
# # heading = "intro to python"
# # print(heading.capitalize())
# # print(heading.center(50))
# # print(m.count("r"))
# # print(m.endswith("to" ,2,9))
# # print(m.find("to"))
# # print(m.isalnum())

# # for k in range(3,15,2):
# #     print(k)
    
# # x = int(input("enter a num"))

# # while True:
# #     x = int(input("enter a num"))
# #     if(x>3):
#         # break
# # for i in range(1,11):
# #     print(i)
# #     if(i==6):
# #        continue
# #     print("5 * ",i,"=",i*5)

# # def name(**name):
# #     print("hello" ,name["a"], name["b"], name["c"])
    
# # name(b="bahadur",a="amul",c="poudel")
    
# # we always see the first return and we dont accept any returns after that
# # tup1 = (1,2,3,4,5,5,6,7,8,9,5)
# # tup2=("d","e","f")
# # print(tup1.index(5,7,))
# # p=tup1+tup2
# # print(p)
# # print(len(tup1))
# # import time
# # timestamp=time.strftime('%H:%M:%S')
# # print(timestamp)

# # letter = "k xa {}"
# # c = "pramul"
# # print(letter.format(c))

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 2 or n==1:
#         return 1
#     else:
#         return fibo(n-2) + fibo(n-1)
# def print_fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# # Example: Print the first 10 Fibonacci numbers
# n = int(input("Enter the number of Fibonacci numbers to print: "))
# print_fibonacci(n)
# print(fibo(0))
# print(fibo(1))
# print(fibo(5))
# print(fibo(10))

# #SETS
# s1={1,2,3,4}
# s2={4,5,6,7}
# print(s1.union(s2))
# #s1.update(s2)#updates the s1 wir new vaues od s2
# s3 = s1.intersection(s2)
# print(s3)
# print(s1,s2)
        
this is the disctionary and only the fist word refers to second but second doniot refer to the first one it means hary refer to poudel but poudel donot refer to harry
# dict = {
#     "harry" :"poudel",
#     "spoon": "patrick"
    
# }
# print(dict)
# print(dict.values)
# print(dict.keys())
# for key in dict.keys():
#     print(f"The value pair for the {key} is {dict[key]}")
# ep1={1:23,2:30,3:90,4:50}
# ep2={5:70,6:70}
# ep1.update(ep2)
# print(ep1, ep2,)

# for i in range (9):
#     print(i)
# else:
#     print("no i")

# a = 90
# b = 9
# print(a) if a>b else print(b) if b>a else print("hdfhjd")
# c = 1 if a>b else 2 if b>a else 3 if a==b else print(5)
# print(c)
marks = [12,23,98,22,22,34]
for i,mark in enumerate(marks,start=1):
    print(i,mark) '''


# import saw

# saw.welcome()
# saw.wel()

#os module

# import os

'''if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,10):
    os.mkdir(f"data/day{i+1}")'''
    
#replace the name of data like tutorial to Tutorial 
# for i in range(0,10):
#     os.replace(f"data/tutorial{i+1}",f"data/Tutorial {i+1}")
 
 
 
#list out the name of the number of file   
# folder = os.listdir("data")
# print(folder)
# y = 1
# def function():
#     x = 5
#     print(x)
#     global y
#     y = 5

# function()
# print(y)
# i = 0
# with open('filename.txt', 'r') as f:
#     while True:
#         i+=1
#         line = f.readline()
#         if not line:
#             break
#         m1 = line.split(",")[0]
#         m2 = line.split(",")[1]
#         m3 = line.split(",")[2]
#         print(f"the marks for hsitpry of student {i} is {m1}")
#         print(f"the marks for hsitpry of student {i} is {m2}")
#         print(f"the marks for hsitpry of student {i} is {m3}")

# with open ("my.txt",'a') as f:
#     lines=["gaurab\n","smaar\n","amul\n"]
#     f.writelines(lines)
##ooop
# class pramul:
#     name = "pramul"
#     age = 20
#     sirname = "poudel"
#     def pr(b):
#         b.name = "guarb"
#         b.age=19
#         print(f"{b.name} is {b.age}")
    
# a= pramul()
# # a.age=19
# # print(a.age)
# a.pr()

# def hello():
#     print("hllo")
# def plain():
#     print("plain")

# hello()
# plain()
# def gret():
#     print("Hello!")

# print(gret.__name__)  # Output: 'greet'

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def method(cls,s):
#         return cls(s.split("-")[0],int(s.split("-")[1]))
        
# s="harry-12000"
# e1=Employee(s.split("-")[0],int(s.split("-")[1]))
# print(e1.name)
# print(e1.salary)
# e2=Employee.method(s)
# print(e2.name)
# print(e2.salary)
class shape():
    def __init__(self,length):
        self.length=length
    def square(self):
        return self.length * self.length
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius)
    def area(self):
        return 3.14 * super().square()    
class rec(circle):
    def __init__(self,a):
        self.a=a
        super().__init__(a)
    def value(self):
        return 2 * super().area()
s = shape(6)
k = circle(7)
f=rec(7)
print(k.area())
print(s.square())
print(f.value())
