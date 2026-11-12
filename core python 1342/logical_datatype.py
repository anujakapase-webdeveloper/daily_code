#find duplicate values in a list
num=[23,65,65,45,87,15,73,15]
unique_list=[]
for items in num:
    if items not in unique_list:
      unique_list.append(items)
print("unique list",unique_list)    

#separate even and odd
num=[23,5,4,6,8,7,24,1,7,5]
even=[]
odd=[]
for i in num:
   if i%2==0:
      even.append(i)
   else:
      odd.append(i)
print("even number:",even)
print("odd number:",odd)      

#frequency item
my_list = [1, 2, 2, 3, 3, 3, 4]
frequency_dict = {}
for item in my_list:
  if item in frequency_dict:
    frequency_dict[item] = frequency_dict[item] + 1
  else:
    frequency_dict[item] = 1
print("Element frequency:", frequency_dict)

#non zero list
my_list = [0, 1, 9, 0, 3, 12, 0]
non_zeros = []
zeros_count = 0
for num in my_list:
  if num == 0:
    zeros_count = zeros_count + 1
  else:
    non_zeros.append(num)
for i in range(zeros_count):
  non_zeros.append(0)
print("Zeros aakhir me jaane ke baad:", non_zeros)

#reverse the tuple  
my_tuple = (1, 2, 3, 4, 5)
reversed_list = []
for i in range(len(my_tuple) - 1, -1, -1):
  reversed_list.append(my_tuple[i])
reversed_tuple = tuple(reversed_list)
print("Reversed Tuple:", reversed_tuple)

#maximum and minimum
my_tuple = (10, 45, 2, 89, 23)
maximum = my_tuple[0]
minimum = my_tuple[0]
for num in my_tuple:
  if num > maximum:
    maximum = num
  if num < minimum:
    minimum = num
print("Maximum element:", maximum)  
print("Minimum element:", minimum)  

#tuple element frequency
my_tuple = (1, 2, 3, 2, 4, 2, 5)
target = 2
count = 0
for item in my_tuple:
  if item == target:
    count = count + 1
print("Element:", count)