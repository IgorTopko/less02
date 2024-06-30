def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Igor", 27) == "Hi. My name is Igor and I'm 27 years old", 'Test1'
assert say_hi("Mark", 32) == "Hi. My name is Mark and I'm 32 years old", 'Test2'
print("OK")