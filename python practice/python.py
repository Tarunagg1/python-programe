n = 5;
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# for row in range(n):
#     for col in range(n):
#        if col==0 or row==(n-1) or row==col:
#            print("*",end="")
#        else:
#             print(end=" ")
#     print()   

# ````````````````````````````````````````````````````````````````````````````````````
# num = int(input("enter the number: "))
# res = 0
# for i in range(1,num):
#     if(num % i == 0):
#         res +=i
# print(res)
# if(num == res):
#     print("perfect")
# else:
#     print("not perfect")

# ````````````````````````````````````````````````````````````````````````````````````````
# name = input("enter number: ")
# rev = " "
# for i in name:
#     rev = i+rev
# print(rev)

# ````````````````````````````````````````````````````````````````````````````````````````````
a = [910,520,48,4,484,84,8184]
n = len(a);
# for i in range(0,n-1):
#     min = i;
#     for j in range(i+ 1,n):
#         if a[min] > a[j]:
#             min = j
#     if min != i:
#         swap = a[i]
#         a[i] = a[min]
#         a[min] = swap
# print(a)

# ``````````````````````````````````````````````````````````````````````````````````````
# for i in range(n-1):
#     for j in range(n-1-i):
#      if(a[j] > a[j+1]):
#         temp = a[j]
#         a[j] = a[j+1]
#         a[j+1] = temp
# print(a)

# ``````````````````````````````````````````````````````````````````````````````````````````
# lower = int(input("enter the lower num: "))
# upper = int(input("enter the upper num: "))

# for num in range(lower,upper):
#     revnum = int(str(num)[::-1])
#     if num == revnum: 
#         if num > 1:
#             for i in range(2,num):
#                 if(num %i == 0):
#                     break
#             else:
#                 print(num)    


# ``````````````````````````````````````````````````````````````````````````````````````
# def binaryfunction(list,key):
#     low , high = 0 ,len(list);
#     found = False
#     while low<=high and not found:
#         mid = (low+high) // 2;
#         if key == list[mid]:
#             found = True
#         elif key > list[mid]:
#             low = mid+1
#         else:
#             high = mid-1
#     if(found == True):
#         print("key found")
#     else:
#         print("not found")
              
# list = [2,5,6,10,16,19]
# key = int(input("enter the number: "))
# binaryfunction(list,key);

# ``````````````````````````````````````````````````````````````````````````````````````````````````
# s1 = input("enter 1st string: ")
# s2 = input("enter 2st string: ")
# str1 = sorted(s1)
# str2 = sorted(s2)
# if(len(str1) == len(str2)):
#     if(str1 == str2):
#         print("anagram")
#     else:
#         print("not")
# else:
#     print("len not mathc")


# ``````````````````````````````````````````````````````````````````````````````````````````````````````
# l2 = []
# def getmag(list):
#     for i in list:
#         if type(i) == list:
#             getmag(i)
#         else:
#             l2.append(i)
#     return max(l2)
# l1 = [84,854,984,8,94,48,48]            
# print(getmag(l1))

# ``````````````````````````````````````````````````````````````````````````````````````````````````
# year = int(input("enter the year: "))
# if(year %4 == 0 ):
#     if year %100 == 0:
#         if year %400 == 0:
#             print("leap year")
#         else:
#             print(year,"not leap")
#     else:
#         print(year,"is leap")
# else:
#     print(year,"not leap")
       
# ````````````````````````````````````````````````````````````````````````````````````````````
# row = int(input("enter the row: "))
# col = int(input("enter the col: "))
# print("enter tht number of first matrix element")
# martix1 = [[int(input()) for i in range(col)] for j in range(row)]

# print("enter tht number of first matrix element")
# matrix2 = [[int(input()) for i in range(col)] for j in range(row)]

# res = [[0 for i in range(col)] for j in range(row)]
# for i in range(row):
#     for j in range(col):
#         for k in range(col):
#             res[i][j] += martix1[i][k] * matrix2[k][j]
# for r in res:
#     print(r)

# ````````````````````````````````````````````````````````````````````````````````````````````````
q1 = "what ia py? \n a.yes \n b.noc\n c.none \n d.mm "
q2 = """what ia py?
a.yes
b.no
c.none
d.mm
"""
q3 = """what ia py?
a.yes
b.no
c.none
d.mm
"""
q4 = """what ia py?
a.yes
b.no
c.none
d.mm
"""
q5 = """what ia py?
a.yes
b.no
c.none
d.mm
"""
# question = {q1:"a",q2:"b",q3:"c",q4:"d",q5:"a"}
# name = input("enter your name: ")
# print(f"hello!! welcome {name}")
# score = 0
# qcount = 1;
# print(len(question))
# print(question)
# for i in question:
#     print(f"{qcount}. {i}")
#     flag1 = input("dou want to skip question (yes/no): ")
#     if flag1 == "yes":
#         continue;
#     ans = input("enter your answer: ")
#     if(ans == question[i]):
#         print("answer is correct you got 1 point")
#         score+=1
#     else:
#         print("answer is wrong 1 point loose point")
#         score-=1
#     flag2 = input("dou want to exit from here (yes/no): ")
#     if(flag2 == "yes"):
#         break
        
# print("final score is: ",score)

# ``````````````````````````````````````````````````````````````````````````

# class employee:
#     increment = 1.5
#     def __init__(self,fname,lname,salery):
#         self.fname = fname
#         self.lname = lname
#         self.salery = salery
        
#     def incrementsal(self):
#          self.salery = int(self.salery)*employee.increment
         
#     @classmethod     
#     def changeinc(cls,amt):
#         cls.increment = amt
#     @classmethod
#     def fromstr(cls,empstr):
#         fname,lname,salery = empstr.split("-")
#         return cls(fname,lname,salery)
#     @staticmethod
#     def isopen(day):
#         if(day == 'sunday'):
#             return False
#         else:
#             return True
    
# class programer(employee):
#     def __init__(self,fname,lname,salery,programing,exp):
#         super().__init__(fname,lname,salery)
#         self.programing =programing
#         self.exp = exp

#     def __add__(self,other):
#         return self.salery + other.salery
#     @property
#     def email(self):
#         if self.fname == None:
#             return 'email not set'
#         else:
#             return self.fname +'.'+ self.lname + "@gmail.com"
    
#     @email.setter
#     def email(self,giveemail):
#         namelist = giveemail.split('@')[0].split('.')
#         self.fname = namelist[0]
#         self.lname = namelist[1]
        
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
        
#     def __str__(self):
#         return 'Employee is ({} , {} , {})'.format(self.fname,self.lname,self.salery)

    
# harry = employee("harry","jacksons",20);
# tarun  = employee("tarun","aggarwal",10);
# nidhi = employee.fromstr("nidhi-garg-40")
# harsh = programer("harsh","walia",100,"java",1)
# aravind = programer("aravind","menon",200,"hacking",0)

# print(harsh.salery)
# harsh.incrementsal()
# print(harsh.email)
# del harsh.email
# print(harsh.email)



# ``````````````````````````````````````````````````````````````````````````````````
# class flyingVehicle:
#     def __init__(self,fspeed):
#         print(f"Speed of flying vechel is: {fspeed}")

# class landVehicle(flyingVehicle):
#     def __init__(self,lspeed,fspeed):
#         super().__init__(fspeed)
#         print(f"Speed of land vechel is: {lspeed}")
        
# class waterVehicle(landVehicle):
#     def __init__(self,wspeed,fspeed,lspeed):
#         super().__init__(lspeed,fspeed)
#         print(f"Speed of water vechel is: {wspeed}")

# class speed(waterVehicle):
#     def __init__(self,fspeed,lspeed,wspeed):
#         super().__init__(wspeed,fspeed,lspeed)
        
# vh = speed(10,20,30)

# ````````````````````````````````````````````````````````````````````````````````
# class camera:
#     def __init__(self):
#         print("camera is avilable")
#     def frontcamera(self,whichcam):
#         def mp8(self):
#             print("this is 8mp camera")
#         def mp16(self):
#             print("this is 16mp camera")
#         def mp32(self):
#             print("this is 32mp camera")
#         def mp64(self):
#             print("this is 64mp camera")
        
        # if whichcam == 'mp8':
        #     mp8(self)
        # elif whichcam == 'mp16':
        #     mp16(self)
        # elif whichcam == 'mp32':
        #     mp32(self)
        # else:
        #     mp64(self)
           
# cam = camera()              
# cam.frontcamera("mp32");            

# ``````````````````````````````````````````````````````````````````````````
# from datetime import datetime
# print(ord('A'))
# print(chr(97))
# print(datetime.now())
# print(type(10))

# cityname = input("Enter the value comma seprated city name: ");
# l = list(cityname.split(','));
# print(sorted(l))

