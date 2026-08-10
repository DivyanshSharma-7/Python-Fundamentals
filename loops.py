# There are only 2 types of Loops in Python :- 
# a) while loop
# b) for loop

# 1) **while loop** :
# i=1
# while i<=5:
#     print("Hello world !!")
#     i+=1

# Some Practice Questions :
# 1)
# i=1
# while i<=100:
#     print(i)
#     i+=1

# 2)
# i=1
# n=int(input("Enter any Number : "))
# while i<=10:
#     print(n*i)
#     i+=1
# print("code ended !!")

# # 3)
# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# n=len(list)
# while i<n:
#     print(list[i])
#     i+=1

# 4)
# list=(1,4,9,16,25,36,49,64,81,100)
# i=1
# search=49
# while i<len(list):
#     if(list[i]==search):
#         print("FOUND at index :",i)
#     else :
#         print("finding ....")
#     i+=1


# break & Contiinue :
# a) *break* :
# tup=(1,4,9,16,25,36,49,64,81,100)
# i=1
# search=49
# while i<len(tup):
#     if(tup[i]==search):
#         print("FOUND at index :",i)
#         break
#     else :
#         print("finding ....")
#     i+=1

# b) *continue* :
# i=1
# while i<=10:
#     if(i==7):
#         i+=1
#         continue
#     print(i)
#     i+=1


# 2) **for loop** :
# list=[2,4,7,3,6]         # it's also work with tuple & string .

# for el in list:
#     print(el)

# string="python"
# for chr in string :
#     print(chr)
# else :
#     print("code ended !!")      # else only works when loops ends .


# ****Some Practise Questions**** :
# 1)
# tup=(1,4,9,16,25,36,49,64,81,100,9)
# search=9
# idx=0
# for el in tup:
#     if(el==search):
#         print("found at : ",idx)
#         break                        # return only once 
#     idx+=1

# range() function :- important in loops !!
# seq=range(5)
# for el in seq:
#     print(el)

    # or


# for el in range(5):
#     print(el)
# print("next")
# for el in range(2,10):
#     print(el)
# print("next")
# for el in range(2,10,2):
#     print(el)


# *****Some basic Questions Using range() function :
# for el in range(1,101):
#     print(el)

# for el in range(100,0,-1):
#     print(el)

# n=int(input("Enter any number : "))
# for el in range(n,n*11,n):
#     print(el)
    # or
# n=int(input("Enter any number : "))
# for i in range(1,11):
#     print(n*i)


# ******last Two Practise Problem(basics) Based on loops*******
# 1) print the sum of first n numbers .
# i=1;
# sum=0;
# n=int(input("enter any number : "))
# while i<n+1:
#     sum+=i
#     i+=1
# print("total sum is : ",sum)

#          or
# using range() function :
# n=int(input("enter any number : "))
# sum=0
# for i in range(1,n+1) :
#     sum+=i
# print("total sum is :",sum)

# 2) find the factorial of given no (n) !
n=int(input("enter any number : "))
fact=1
i=1
for i in range(1,n+1):
    fact*=i;
print("factorial is :",fact)











