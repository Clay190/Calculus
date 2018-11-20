#Clay Kynor
#11.19.18

from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2

func = input("Input your function: ")
num = int(input("Input how many rectangles you want "))
a = float(input("Input the start of your range "))
b = float(input("input the end of your range "))

n = (b-a)/num
Ltotal = 0
Mtotal = 0
Rtotal = 0

for i in range(0,num):
    x=(i*n)+a
    Ltotal += eval(func)*n

for i in range(1,num+1):
    x=(i*n)+a
    Rtotal += eval(func)*n
    
for i in range(0,num):
    x = ((i*n)+a) + (n/2)
    Mtotal += eval(func)*n

print("LRAM", Ltotal)
print("MRAM", Mtotal)
print("RRAM", Rtotal)