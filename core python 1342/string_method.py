'''#string methods

#capitalize
name="anuja"
print(name.capitalize())#it used to convert first character into upper case

#casefold
name="aniket"
print(name.casefold())#casefold() method converts a string into lowercase more aggressively than lower()

#upper
name="jay"
print(name.upper())#It is used to convert string into uppercase

#lower
name="chotu"
print(name.lower())#It is used to convert string into lower case

#islower
name="gayatri"
print(name.islower())#It return result in True or False 

#index
name="shubhangi"
print(name.index("n"))#It return index position of a string character

#isalnum
age="sa22"
print(name.isalnum())#it check value and return True if value is alhabets or numeric.

#isnumeric
age=22
print(name.isnumeric())#It check value and return if a value is numeric

#title
text="python is a object-oriented programming language"
print(text.title())# capitalizes the first letter of every word

#count
name=input("enter your name:")
print(name.count("a"))#it return count of specific character of a string

#endwith
name="anuja kapase"
print(name.endswith("kapase"))#it check string ending value

#replace
name="anuja kapase"
print(name.replace("anuja","aniket"))#it used to replace vlues with current variable value

#startwith
name="jay chotu"
print(name.startswith("jay"))#It check staring value of a string


#How to print output
name="jay"
city="pune"
print("my name is ",name,"my city is",city)
print(f"my name is {name} ,my city is {city}")'''

text="Welcom To Python Class"
print(text.casefold())

text=["python","is","programming language"]
print(" ".join(text))