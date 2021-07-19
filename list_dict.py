import random

#Task 1
list_even = []
list_uneven = []

n = 100
for x in range(1,101):
    x = random.randint(1,100)


    if x%2 == 0:
        list_even.append(x)
        n = -1
        if n ==0:break
    else:
        list_uneven.append(x)
        n = -1
        if n == 0: break

print(list_even)
print(list_uneven)

sum_even = sum(list_even)
print(sum_even)
sum_uneven = sum(list_uneven)
print(sum_uneven)

#Task 2

dict_modernized = {'even': list_even, 'uneven': list_uneven, 'even_sum': sum_even, 'uneven_sum': sum_uneven}
print(dict_modernized)
print(dict_modernized['even'])


number_float = random.uniform(1,3)
number_float = round(random.uniform(1,3),2)

#Task 3
m = 0
list_float = []
list_float.append(number_float)

while_flag1 = True
while while_flag1:
    y = round(random.uniform(1, 3), 2)
    list_float.append(y)
    if list_float.count(y)!= 2:
        m=m+1
    elif list_float.count(y)==2:
        print(m, "iterations")
        print("The probability to get two equal numbers is 1/",m)
        while_flag1 = False
        break
