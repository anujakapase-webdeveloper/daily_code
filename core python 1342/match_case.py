#grades for marks
marks=78
match marks:
 case 90|91|92|93|94|95|96|97|98|99|100:
  print("grade A")
 case 80|81|82|83|84|85|86|87|88|89:
  print("grade B")
 case 70|71|72|73|74|75|76|78|79:
  print("grade C")
 case 60|61|62|63|64|65|66|67|68|69:
  print("grade D")
 case 50|51|52|53|54|56|57|58|59:
  print("grade E")
 case _:
  print("grade F") 

#marks for grade
grade="A"
match grade:
 case "A":
  print("marks between 90 to 100")
 case "B":
   print("marks between 80 to 99")
 case "C":
  print("marks between 70 to 89")
 case "D":
  print("marks between 60 to 79") 
 case "E":
  print("marks between 50 to 69")
 case _:
  print("marks below 50")  

 #quater
quater=4
match quater:
 case 1:
  print("months:jan,feb,mar")
 case 2:
  print("months:apr,may,jun")
 case 3:
  print ("months:jul,aug,sep")
 case 4:
  print("months:oct,nov,dec")
 case _:
  print("invalid input")  


#taffic signal
color="Red" 
match color.lower():
 case "red" : 
  print("stop")
 case "yellow":
  print("ready to go")
 case "green":
  print("go")
 case _:
  print("invalid output") 

color="Red" 
match color.replace("Red","yellow"):
 case "red" : 
  print("stop")
 case "yellow":
  print("ready to go")
 case "green":
  print("go")
 case _:
  print("invalid output")   
   
 
 
  
