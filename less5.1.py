import keyword
import string

# value = "_"  #True
# value = "__" #False
# value = "___"  #False
# value = "x"  #True
# value = "get_value"  #True
# value = "get value"  #False
# value = "get!value"  #False
# value = "some_super_puper_value"  #True
# value = "Get_value"  #False
# value = "get_Value"  #False
# value = "getValue"  #False
# value = "3m"  #False
# value = "m3"  #True
# value = "assert"  #False
# value = "assert_exception" #True

result = True
if value[0].isdigit() or value in keyword.kwlist:
    result = False
elif value.count("_") == len(value) and len(value) > 1:
    result = False
else:
    for letter in value:
        if letter == "_":
            continue
        elif letter.isupper():
            result = False
            break
        elif (letter in string.punctuation or
                letter.isspace()):
            result = False
            break
print(result)

