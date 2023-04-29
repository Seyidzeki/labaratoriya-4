# Data Tipleri
# Text Type
x = "Salam Men Zeki"
print(x)
print(type(x))

# Numeratic Type (int)
y = 21
print(y)
print(type(y))

# Numeratic Type (float)
z = 2.2
print(z)
print(type(z))

#Complex
a = 3j
print(a)
print(type(a))

# Ardicilliqlar (list)
e = ["alma","heyva","nar"]
print(e)
print(type(e))

# Ardicilliqlar (tuple)
r = ["alma","heyva","nar"]
print(r)
print(type(r))

# # range
t = range(9)
print(t)
print(type(t))

# bool
d = False
print(d)
print(type(d))

# Global Deyisen
w = "Zeki"
def myFunc():
    w = "Aga"
    print("Salam men " + w)
myFunc()
print("Salam Men " + w)

# Operatorlar (Riyazi Operatorlar)

n = 7
m = 2

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n % m)
print(n ** m)
print(n // m)

# Operatorlar (Teyinat Operatorlar)
f = 3
print(f)
f += 3
print(f)
f -= 3
print(f)
f *= 3
print(f)
f /= 3
print(f)
f %= 2
print(f)
f //= 3
print(f)
f **= 3
print(f)

# Operatorlar (Muqayise Operatorlar)
u = 65
i = 64
print(u == i)
print(u != i)
print(u > i)
print(u < i)
print(u <= i)
print(u >= i)

# Operatorlar (Mentiqi Operatorlar)
s = 6
print(s > 5 and s < 7)
print(s > 3 or s > 345)
print(not(s > 3 or s > 345))

# Sert Operatoru (if else)
g = 65
h = 23
if g > h:
  print("g boyukdur h-dan")
elif g == h:
  print("g ve h beraberdir")
else:
  print("g kicikdir -dan")