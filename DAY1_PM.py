### DAY 1 PYTHON DSA

# Print Biodata:


name=input ("enter your name:")
age=int(input("enter your age:"))
department=input("enter your department:")
rollno=int(input("enter your roll number:"))
mobno=int(input("enter your mobile number:"))
address=input("enter your address:")
print("name:",name)
print("age:",age)
print("department:",department)
print("roll number:",rollno)
print("mobile number:",mobno)
print("address:",address)


# Boolean (T/F)
is_student = True
is_logged_in = False
print("Is the user a student?", is_student)
print("Is the user logged in?", is_logged_in)

# calculate Area of rectangle
length=float(input("Enter length"))
width=float(input("Enter width"))

# a=l*w
area=length*width
print("Area of rectangle = ",area)
 
#Types of variables
name = "Poras"
age = 21
height = 5.11
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# calculate simple interest
# SI=(p*R*t)/100
p=float(input("Enter principal:"))
r=float(input("enter rate:"))
t=float(input("Enter time"))
si=(p*r*t)/100
print("Simple intrest = ",si)


# Swap two numbers
a=6
b=9
a,b=b,a
print("a = ",a)
print("b = ",b)


# Find square,cube of a number
a=int(input("enter any number:"))
sqr=a*3
cube=a*6
print("Square = ",sqr)
print("Cube = ",cube)


# Convert minits to hours
minits=int(input("Enter minits:"))
hours=minits/60
print("hours = ",hours)

# Calculate Average of 3 number
print("Enter three numbers:")
num1=float(input())
num2=float(input())
num3=float(input())
average=(num1+num2+num3)/3
print("Average = ",average)

# Convert celsius to fahrenheit
celsius=float(input("Enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in fahrenheit = ",fahrenheit)

# Convert km to meters
km=float(input("Enter distance in kilometers:"))
meters=km*1000
print("Distance in meters = ",meters)

# Convert rupees to dollar
rupees=float(input("Enter amount in rupees:"))
dollar=rupees/83
print("Amount in dollars = ",dollar)

# calculate total marks and percentage cgpa
print("Enter marks of 5 subjects:")
marks1=float(input())
marks2=float(input())
marks3=float(input())
marks4=float(input())
marks5=float(input())
total_marks=marks1+marks2+marks3+marks4+marks5
percentage=(total_marks/500)*100
cgpa=percentage/8.9
print("Total marks = ",total_marks)
print("Percentage = ",percentage)
print("CGPA = ",cgpa)



### Create variables for:
# name
# branch
# college
# year
name = "Poras"
branch = "RAI"
college = "RBU"
year = 2
print("Name = ",name)
print("Branch = ",branch)
print("College = ",college)
print("Year = ",year)


print("Hello Students")
age=21
#More examples
name = "Poras"
salary = 1000000
temperature = 40
print(type(name))
print(type(salary))
print(type(temperature))



price = 89.99
height = 5.11
temperature = 40
print(type(price))
print(type(height))
print(type(temperature))


#show types of variables
age = 21
print(type(age))

name = "Poras"
print(type(name))
is_student = True
print(type(is_student))

#String
name = "Poras"
city = "Nagpur"
course = "Python"
print("Name:", name)
print("City:", city)
print("Course:", course)

#Typecasting
age="21"
age=int("21")
age=age+3
print(age)


# This is string, not number.
age = "21"
# Convert to integer:
age = int("21")

# integer==>floating point number
num = 45
# Convert to float:
num = float(45)


# Convert number to string
num = 69
print(type(num))
text = str(num)
print(type(text))

num1 = "15"
num2 = "30"
print(num1+num2)
result = int(num1) + int(num2)
print(result)


# Taking input from user
age=input("enter your age:")
# ag1=int(input("Enter value ag1:")) type casting
print(age)
print(type(age))


# find your current age
byear=int(input("Enter your birth year:"))
cyear=2026
age1=cyear-byear
print(age1)


# Take input from user.
age = input("Enter your age: ")
print(age)



# input() always returns string.
# Convert to integer:
age = int(input("Enter your age: "))

# Example:
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(age)

