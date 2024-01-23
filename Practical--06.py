fh=open('Output.txt','w')

number=int(input("Enter a number :"))

Sum = 1
for i in range (1,number+1) :
    Sum = Sum * i

print(Sum)

fh.write(f'The factorial of '+ (str(number)) + ' is '+ str(Sum))
fh.close()