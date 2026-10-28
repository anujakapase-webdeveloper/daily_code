s = "Python" 
print(s[0])  #p
print(s[-1]) #n
print(len(s))#6

s = "Kiran"  
x = s 
s = s + " Academy" 
print(x) 
print(s)

s = "Python"
print(s[1]) 
print(s[-2]) 
print(s[3])

s = "Academy" 
print(s[0] + s[-1])
print(s[2] + s[-3])

'''s = "Python" 
s[0] = "J" 
print(s)'''#it cannot be changed because it ia immutable

s = "kiranacademy"
print(s[0:5]) 
print(s[5:]) 
print(s[:5])

s = "kiranacademy" 
print(s[::2]) 
print(s[1::2])

s = "Python" 
print(s[::-1]) 
print(s[-1::-2])

s = "kiranacademy" 
print(s[-2:1:-2])

s = "abcdefghij" 
print(s[8:2:-2]) 
print(s[2:8:2])

s = "python programming" 
print(s.upper()) 
print(s.capitalize()) 
print(s.title())

s = "  Python  " 
print(len(s)) 
print(len(s.strip())) 
print(s.strip())

s = "java python java" 
print(s.count("java")) 
print(s.find("python")) 
print(s.find("sql"))

s = "Kiran Academy" 
print(s.replace("Academy", "Classes"))
print(s.lower())

s = "Java,Python,SQL" 
x = s.split(",") 
print(x) 
print(x[1])

s = "Python" 
print(s[5:1:-2]) 
print(s[1:5:2])

s = "kiranacademy" 
print(s[-1:-8:-2]) 
print(s[-3::-3])

s = "PythonProgramming" 
print(s.lower()[::-2])

s = "  kiran academy  " 
print(s.strip().title().replace(" ", "_"))

s = "banana" 
print(s.find("a")) 
print(s.rfind("a")) 
print(s.count("an"))

s = "kiranacademy" 
print(s[10:2:-3]) 
print(s[2:10:3])

s = "Python" 
print(s[-1:-7:-2]) 
print(s[-2::-2])

s = "  Python Programming  " 
print(s.strip().lower().replace("python", "java").title())

s = "mississippi" 
print(s.count("ss")) 
print(s.count("issi")) 
print(s.find("sip"))

s = "one-two-three-four" 
x = s.split("-") 
print(x) 
print(":".join(x[::-1]))

s = "PyThOn123" 
print(s.swapcase()) 
print(s.isalnum()) 
print(s.isalpha())

s = "academy"
print(s.startswith("aca")) 
print(s.endswith("emy")) 
print(s.startswith("ad", 2))

s = "banana" 
print(s.replace("a", "A", 2)) 
print(s.replace("na", "NA", 1))

s = "abcabcabc" 
print(s.find("abc", 1)) 
print(s.rfind("abc", 0, 7)) 
print(s.count("abc", 1, 8))

s = "  kiran academy python  "
print(s.strip()[::-1].upper()) 
print(s.strip().split()[1][::-1])

name="python"
print(name.center(7,"-"))
print(name.index("p"))
print(name.find("x"))