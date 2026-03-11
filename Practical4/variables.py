a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
print("Change from 2004 to 2014:", d, "million")
print("Change from 2014 to 2024:", e, "million")
if d>e :
    print("Population growth slowed down")
elif d<e :
    print("Population growth accelerated.")
else :
    print ("Population growth stayed the same.")
# d = 0.25 million
# e = 0.22 million
# Since d > e, population growth slowed down.

X=True
Y=False
W=X or Y
print("X:", X)
print("Y:", Y)
print("W (X or Y):", W)
# Truth table for W = X or Y
# X      Y      W
# True   True   True
# True   False  True
# False  True   True
# False  False  False