###DAY 2 DSA PROGRAMS

# Counting digits in number
number=int(input("enter any number:"))
count=0
while number>0:
    count+=1
    number//=10
print(count) 

# To check even odd number
number=int(input("enter any number:"))
if number%2==0:
    print("even number")
else:
    print("odd number")  


# Multiplications table 1-20
number=int(input("enter any number:"))
for i in range(1,21):
    print(number,"*",i,"=",number*i)
    

#Fibbonacci series
n=int(input("enter the number of terms:"))
a=0
b=1
count=0
if n<=0:
    print("please enter a positive integer")    
elif n==1:
    print("fibonacci sequence upto",n,":")
    print(a)
else:
    print("fibonacci sequence upto",n,":")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
        

# Armstrong number
number=int(input("enter any number:"))
order=len(str(number))
sum=0
temp=number
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if number==sum:
    print(number,"is an armstrong number")
else:print(number,"is not an armstrong number")


# prime number
number=int(input("enter any number:"))
if number>1:
    for i in range(2,number):
        if number%i==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:print(number,"is not a prime number")


# Pallindrome number or string
number=int(input("enter any number:"))
temp=number
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10
if number==reverse:
    print(number,"is a pallindrome number")
else:print(number,"is not a pallindrome number")
