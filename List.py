# list in python is same as String 
# indexing starts from 0 .
# marks=[22.3,65.7,23.6,13.6,23.8]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[3])

# In python *lists* are Accessable & Changeable 
# but in *string* values are only Accessable not Changeable 
# student=["naman",45.7,"dhani"]
# print(student)
# student[0]="replace"
# print(student)

# print(student[0])
# student[0]=35
# print(student)

# Some Practise Questions :
# 1)
# movies=["kabir singh","dhurandar 2","shiddat"]
# print(movies)
# movies[0]=input("Enter your First Favourite Movie name : ")
# movies[1]=input("Enter your Second Favourite Movie name : ")
# movies[2]=input("Enter your Third Favourite Movie name : ")
# print(movies)

# or 

# movies=[]
# print(movies)
# mov1=input("Enter your First Favourite Movie name : ")
# mov2=input("Enter your Second Favourite Movie name : ")
# mov3=input("Enter your Third Favourite Movie name : ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# 2) Check for a Palindrome List :
# list=[1,"abd","abd",1]
# list2=list.copy()
# list2.reverse()

# if(list==list2) :
#     print("Palinderome")
# else :
#     print("Not palindriome")

#  or 

list=[1,"abd","abd",1]
list2=list.copy()
list2.reverse()
print(list==list2)

