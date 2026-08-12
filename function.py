# def sum(a,b):          # function definition . a,b is parameters 
#     s=a+b
#     return s

# print("sum is : ",sum(3,4))      # sum(3,4)) --> function calling .  3,4 is arument 

# def print1():
#     print("very nice !!")

# print1()
# output=print1()
# print(output)

# ****Ques:- Average of 3 numbers .
# def avg(a,b,c):
#     avg=(a+b+c)/3
#     return avg

# print(avg(2,4,6))

# or

# def avg(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg

# avg(2,4,6)

# default parameters.
# def mul(a,b=4):
#     mul=a*b
#     return mul
# print(mul(2))

# Some Practise Questions :
# 1)
# list1=[1,3,5,6,7,3,3]
# list2=[1,4,5,3,9]

# def len_list(list):
#     print(len(list))

# len_list(list1)
# len_list(list2)

# 2)
# list1=[1,3,5,6,7,3,3]
# list2=[1,4,5,3,9]

# def print_list(list):
#     for el in list:
#         print(el,end=" ")

# print_list(list1)

# 3)
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact

# print(fact(5))

# 4) USD to INR .
# def convert(usd):
#     inr=usd*95.34
#     print(usd,"USD=",inr,"INR")
#     # return inr

# convert(float(input("enter usd :")))

# 5)
# def odd_even(num):
#     if(num%2==0):
#         return "EVEN"
#     else:
#         return "ODD"

# result=odd_even(int(input("Enter any number :")))
# print(result)
# or
def odd_even(num):
    if(num%2==0):
        print("EVEN")
    else:
         print("ODD")

odd_even(int(input("Enter any number :")))

