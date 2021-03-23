a = 12
b = 15.3
c = a + b

print(type(a)) # int
print(type(b)) # float

# Implicit conversion
print(type(c)) # float 

# Explicit conversion
e = 24
f = "age:"

# print(f + e) # TypeError 

print(f + str(e)) # age:24