# Recursion : it is a function that calls itself Repeatedly .
# Recursive Function .
# def Values(n):
#     if(n==0):
#         return
#     print(n)
#     Values(n-1)

# Values(5)

# **Some Practise Questions** :
# 1) Factorial Function through Recursion :
# def fact(n):
#     if(n==0 or n==1):
#         return 1;
#     else:
#         return n*fact(n-1)

# print("factorial is :",fact(4))

# 2) Sum of first natural numbers .
# def Sum(n):
#     if(n==0):
#         return 0;
#     # sum=0
#     else:
#          return n+Sum(n-1)

# print("Sum is :",Sum(10))

# 3) Write a recursive function to print all element in list .
# (hint : use list & index parameters)
# def print_list(list,index):
#     if(index==len(list)):
#         return 
#     print(list[index])
#     print_list(list,index+1)

# collection=[2,4,6,2,1]
# print_list(collection,0)

# 4) fibonnaci Series Using Recursion .
def fib(n):
    if(n==0):
        return 0;
    if(n==1):
        return 1;
    else:
         return fib(n-1) + fib(n-2)

n=int(input("Enter te number of terms :"))
for i in range(n):
    print(fib(i),end=" ")




