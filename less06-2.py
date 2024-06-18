my_list = [0,1,2,3,4,5,6,7,8,9,10,1000]
value = 0
for i in range(0,len(my_list),2):
    value += my_list[i]
    element = my_list[-1]
    result = element * value
print(result)