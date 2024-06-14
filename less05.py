my_list = [1000,5,12.3,220,12345,True,None,3232]
one_list = my_list[0:4]
two_list = my_list[4:8]
new_list = (one_list,two_list)
print (new_list)

my_list = [1000,5,12.3]
one_list = my_list [0:2]
two_list = my_list [2:3]
new_list = (one_list,two_list)
print (new_list)

my_list = [1000,5,12.3,220,12345,True,None]
one_list = my_list[0:4]
two_list = my_list[4:7]
new_list = (one_list,two_list)
print (new_list)

my_list = [1000]
one_list = my_list[0:]
two_list = my_list[:0]
new_list = (one_list,two_list)
print (new_list)

my_list = []
one_list = my_list[0:]
two_list = my_list[:0]
new_list = (one_list,two_list)
print (new_list)
