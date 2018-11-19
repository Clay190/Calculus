
#Clay Kynor
#11.19.18

func = input("Input your function: ")
num = int(input("Input how many rectangles you want "))
a = int(input("Input the start of your range "))
b = int(input("input the end of your range "))

n = (b-a)/num
total = 0

for i in range(0,num):
    x=i*(a+n)
    total += eval(func)*n
    print(eval(func)*n)*n
    
print(total)