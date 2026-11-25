#121 is a palindrome
num=121
if str(num)==str(num)[::-1]:
  print(f"{num} is a palindrome")
else:
  print(f"{num} is not a palindrome")

#sum of even number 1 to 50 
total_sum=0
for num in range(2,51,2):
  total_sum+=num
print("the sum of even numbers",total_sum)  


