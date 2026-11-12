numbers = [10, 20, 10, 30, 20, 40]
result = list(set(numbers))
print(result)

#remove duplicate elements from a list
numbers=[12,5,4,4,3,6,5,6,4]
result=list(dict.fromkeys(numbers))
print(result)

#find second largest number 
number=[23,54,76,13,28,74]
unique_num=sorted(list(set(number)))
print("second  lerget num:",unique_num[-2])

#find even and odd numbers and store defferent lists
numbers=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("even numbers:",even)
print("odd numbers:",odd)    

#find common elements from  two lists
num1=[2,3,45,4,6,7]
num2=[4,2,6,5,98]
common=[]
for num in num1:
    if num in num2 and num not in common:
        common.append(num)
print("common elements:",common)

#move all zeros to the end
numbers = [0, 1, 0, 3, 12, 0, 5]
result = []
zeros = 0
for num in numbers:
    if num != 0:
        result.append(num)
    else:
        zeros += 1
result.extend([0] * zeros)
print(result)



