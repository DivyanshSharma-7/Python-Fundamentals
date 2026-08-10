# info={
#     "name":"idvy",
#     "cpa":"9.6",
#     "marks":[34,22,3,4,2],
#     12.8:67
# }
# print(type(info))
# print(info)
# print(info["name"])
# print(info[12.8])
# print(info["marks"])

# **mutable (changeable)**:

# info["marks"]=35
# print(info)

# info["last name"]="sharma"
# info[156]="goal"
# print(info)

# **Empty Dictionary** :

# null_dict={

# }
# print(null_dict)
# null_dict[467]=46
# null_dict["marks"]="Matters"
# print(null_dict)

# **Nested Dictionaries** :

# Student={
#     "name":"divy",
#     "std":"Btech",
#     "Subjects":{
# "pyhsics":24,
# "chemistry":53,
# "mathematics":45

#     }

# }
# print(Student)
# print(Student["Subjects"])
# print(Student["Subjects"]["mathematics"])

# **Dictionaries Methods** :
Student={
    "name":"divy",
    "std":"Btech",
    "Subjects":{
"pyhsics":24,
"chemistry":53,
"mathematics":45

    }

}
print(len(Student))       # Return No of Keys in Dictionaries !
print(Student.keys())
# type casting in List:
print(list(Student.keys()))

print(Student.values())
print(Student.items())
print(Student.get("name1"))   # no error --> None if name key is not in Dictionary
print(Student["name"])   # error if name key is not Dictionary

Student.update({"state":"uttar pradesh","first name":"None"})
print(Student)
