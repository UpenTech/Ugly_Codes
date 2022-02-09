#The Pythagorean Container
var = []

for a in range(1,1001):
    for b in range(1,1001):
        c = (a**2 + b**2) ** (1/2)
        if int(c) == c:
            var.append((a,b,int(c)))

#Filtering Pythagorean Numbers
for each in var:
    num1, num2, num3 = each
    if num1 + num2 + num3 == 1000:
        print(num1,"*",num2,"*",num3, "=",num1*num2*num3)
        break

