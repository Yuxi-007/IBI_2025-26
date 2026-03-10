a=5.08
b=5.33
c=5.55
d=b-a
e=c-d
print("Change from 2004 to 2014:", d, "million")
print("Change from 2014 to 2024:", e, "million")
if d>e :
    print("Population growth slowed down")
elif d<e :
    print("Population growth accelerated.")
else :
    print ("Population growth stayed the same.")
