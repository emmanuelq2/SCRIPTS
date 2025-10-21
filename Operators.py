# Maths operators

import math 
print(10 + 2)   # addition      
print(10 - 2)   # subtraction
print(10 * 2)   # multiplication    
print(10 / 3) # division
print(10 // 3) # integer division
print(10 % 3)   # modulo
print(10 ** 2)  # exponentiation

# maths functions
print(math.ceil(-4.7))
print(math.exp(2))
print(math.factorial(5))
print(math.floor(-4.7))
x = 8
print(math.isinf(x)) 
print(math.log(2))
print(math.log(8, 2))
print(math.log10(2))
print(math.pow(2, 3))
print(math.sqrt(16))
print(math.degrees(x))
print(math.radians(x))

# variables assignments
a = 5
b = 8   
a = a + 1
a += 1
a = a - 1
a -= 1
a = a * 2
a *= 2 

i = 5
j = 8
i = i + j
i += j
print(i)
i = 5
j = 8
i = i - j
i -= j
print(i)
i = 5
j = 8
i = i * j
i *= j
print(i)
i = 5
j = 8
i = i / j
i /= j
print(i)
i = 5
j = 8
i = i // j
i //= j
print(i)
i = 5
j = 8
i = i % j
i %= j
print(i)

# is vs ==
a = [1,2,3]
b = [1,2,3]
print(a == b) # True, because the values are the same
id(a)
id(b)
print(a is b)   # False, because the references are different
print(a is not b) # True, because the references are different
a = 257
b = 257
print(a == b) # True, because the values are the same
print(a is b) # False, because the references are different
a = -6
b = -6
print(a == b) # True, because the values are the same
print(a is b) # True, because the references are the same
a = -5
b = -5
print(a == b) # True, because the values are the same
print(a is b) # True, because the references are the same
a = 256
b = 256
print(a == b) # True, because the values are the same
print(a is b) # True, because the references are the same
