#creating dictionary
dict={"name":"anuja","id":1,"marks":97,"subject":"python"}
print(dict)

#methods of dictionary
#copy
dic=dict.copy()
print(dic)

#get
dic=dict.get("name")
print(dic)

#keys
dic=dict.keys()
print(dic)

#values
dic=dict.values()
print(dic)

#items
dic=dict.items()
print(dic)

#update
dic=dict.update({"name":"aniket","id":2})
print(dic)
print(dict)

#pop
dic=dict.pop("id")
print(dic)
print(dict)

#popitem
dic=dict.popitem()
print(dic)
print(dict)

#clear
'''dic=dict.clear()
print(dic)
print(dict)'''

#fromkeys
keys=('a','b','c') 
values=1
new_dic=dict.fromkeys(keys,values)
print(new_dic)

#iterating a dictionary
for i,j in dict.items():
    print(i,j)

#set default
diction={"name":"jay","age":4,"city":"haragapur"}
age=diction.setdefault("sister","anuja")    
print(age)
print(diction)


