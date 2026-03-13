###DAY4 DSA PROGRAMS

#Remove duplicates in list
num=[1,3,5,6,5,3,4,6,7,2]
rem=[]
for i in num:
    if i not in rem:
        rem.append(i)
print("Actual list:",num)
print("After removing:",rem) 


#Find second largest number    
num=[1,3,5,6,5,3,4,6,7,2]
num.sort()
print("Second largest number is:",num[-2])

#Find area of rectangle
length=10
width=5
area=length*width
print("Area of rectangle is:",area)

#Find all pairs in a list whose sum eql to target
num=[2,4,3,5,7,8,9]
target=10
rem=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]+num[j]==target):
            rem.append((num[i],num[j]))
print("pair is ",rem)      

#Find frequency of each element in list
num=[1,2,2,3,3,3,4,4,5,5,5,5]
dict={}
for i in num:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

#Count how many times each element appears in list
num=[1,2,2,3,3,3,4,4,5,5,5,5]
dict={} 
for i in num:
    dict[i]=dict.get(i,0)+1
print(dict)
# 2nd approch
dict2={}
for i in num:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
print(dict2)    


#List functions
data=["hello","python","C++"]
print(data)
data.append("java")
print(data)
data.insert(2,"php")
print(data)
data.remove("hello")
print(data)


# list tuple set dictionary

# list [] tuple () {set} {key:value}
list=[1,1,2,3,3,4,6,7,"hello",'A']
print(type(list))
print(list)

tuple=(1,2,3,5,'A',"python","java")
print(tuple)
print(type(tuple))

set1={1,2,3,4,5}
print(set1)
print(type(set1))

dict={"name":"Poras","age":21,"city":"Nagpur"}
print(dict)
print(type(dict))

#list 2
marks=[8,15,32,45,69,43]
marks.sort()
print(marks)
marks.reverse()
print(marks)

# find second largset
num=[12,45,78,56,34,89]
maximum=second_max=float('-inf')
for i in num:
    if i>maximum:
        second_max=maximum
        maximum=i
    elif i>second_max and i!=maximum:
        second_max=i
print("second largest number:",second_max) 


# find all pairs sum is equal to target
num=[2,4,3,5,7,8,9]
target=10
rem=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]+num[j]==target):
            rem.append((num[i],num[j]))
print("pair is ",rem)


# find missing number in sequence
num=[1,2,4,5]
n=len(num)+1
total_sum=n*(n+1)//2
actual_sum=sum(num)
missing_number=total_sum-actual_sum
print("missing number is:",missing_number)


# find the maximum sum of contigious subarray
num=[-2,4,-3,6,-1,9,1,-5,8]
max_sum=float('-inf')
current_sum=0
for i in num:
    current_sum+=i
    max_sum=max(max_sum,current_sum)
    if current_sum<0:
        current_sum=0
print("maximum sum of contigious subarray is:",max_sum)


# through list separate even odd  numbers
num=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers:",even)
print("odd numbers:",odd)


# find common elements between two lists
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("common elements:",common)


# reverse list without using reverse function
num=[1,2,3,4,5]
reversed_list=[]
for i in range(len(num)-1,-1,-1):
    reversed_list.append(num[i])
print("reversed list:",reversed_list)


# find longest word in list
list=["hello","python","c","c++","FullstackJava"]
longest=""
for word in list:
    if len(word)>len(longest):
        longest=word
print("longest word is:",longest)


# list=["hello","python","c","c++","Java"]
# find the length of each word in list
list=["hello","python","c","c++","Java"]
lengths=[]
for word in list:
    lengths.append(len(word))
print("length of each word:",lengths)



