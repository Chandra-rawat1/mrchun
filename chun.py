#Write a python program to print a hello world thousand times in new line..

#for _ in range(1000):
    #print("Hello World")

#print("hello" \n*1000")

# write a program to find the data types.
# can you perform the addition of string and the integer
# write a program to find the ASCII value of the characters in your name
#K = input("Please enter a character: ")    
    
#print ("The ASCII value of '" + K + "' is ", ord(K))  

#print ("Please enter the String: ", end = "")  
# string = input()  
# string_length = len(string)  
# for K in string:  
#     ASCII = ord(K)  
#     print (K, "\t", ASCII)  

# write a program to perform the addition of first 20 number
# write a program show use case of bollean data type
# write aprogram to check from the user and render hello with the name of the user
#writre aprogram to convert string data type in to integer, integer into string, float into string, string to float

# write a program to find the data types.

# x = 5
# print(type(x))

# x = "Paribesh Pandey"
# print(type(x))

# # write a program to perform the addition of first 20 number
# a=sum(range(0, 20))
# print (a)


#argument with no return value

# def adding(a):
#     print("hello chandra")

#     adding(5)


# def adding(a):
#     print("hello", a)

#     return a**a

#write a function to show the use case of function with  combination of return value and argument.
# def adding(a):
#     print("hello chandra")

#     adding(5)


# def adding(a):
#     print("hello", a)

#     return a**a

# def adding(a,b,c,d=1):
#     add=a+b+c+d
#     print("add: ",a,b,c,d)
#     # print(a,b,c,d)
#     adding(5,4,43,55)


#write a function to print even number between two 2 and 50 and also perform the addition of those even number

# ll=int(input(" "))
# ul=int(input("Enter upper limit "))

# print("even")

# loop

# for i in range(2,52):
#     if i%2==0:
#         print(i)

#         def find_even();

# def find_even(a,b):
#     sum=0
#     for i in range(a,b):
#         if i%2==0:
#             sum+=i
#             print("sum is", sum)
# find_even(2,51)

# def find_odd(a,b):
#     sum=0
#     for i in range(a,b):
#         if i%2!=0:
#             sum+=i
#             print("sum is", sum)
# find_odd(2,51)

#write a program to check if given number is prime number or not

# def is_prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True
# print(is_prime(11))          


# num = int(input("Enter a number: "))

# If number is greater than 1
# if num > 1:
#    # Check if factor exist  
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")


#write a program to give the multiplication table of 5, 10, 17


# num = int(input(" Enter a number : "))        
# for a in range(1,11):    

#    print(num,'x',a,'=',num*a)  

#another method
# def multiply(a):
#    for i in range(1,11):
#       c=a*i
#       print("The multiplication table shows",c)
# multiply(5)
# multiply(10)
# multiply(17)

# Question 1: Write a program that prompts the user to enter their name and their favorite color. Then, create a message that combines their name and favorite color to form a personalized
# message. Finally, print the message on the console.
# name=input("Enter your name:")
# favolor=input("Your favourite color :")

# # print("Hi",name)
# print("Your favourite color is ",favolor)

# msg=name+favolor
# print(msg)

#Question 2: Write a program that prompts the user to enter asentence. Count and display the number of words in thesentence.
# Quick Two Line Codes
# countOfWords = len("Chandra".split())
# print("Count of Words in the given Sentence:", countOfWords)

# # Quick One Line Codes
# print(len("Iam sad".split()))

# # Quick One Line Code with User Input
# print(len(input("Enter Input:").split()))

#Create a list named "numbers" containing the numbers 1, 3,5, 7, and 9.

# numbers=[1,3,5,7,9]
# print(numbers[1])
# numbers[3]=10
# print(numbers)
# numbers.append(12)
# print(numbers)
# numbers.remove(5)
# print(numbers)

#Create a new list named "sliced_list" that contains a slice ofthe original list from the second to the fourth element.

# sliced_list=[5,7,9]
# print(sliced_list)

# combined_list=[2,4,6,8,10]
# sliced_list.extend(combined_list)
# print(sliced_list)

# #print (my_tuple+my_tuplet2)
# my_tuple=(99,8,1,2,1,3,4,5)

# new_tuple=sorted(my_tuple,reverse=True)
# print(tuple(new_tuple))

# 1. Define a tuple named my_tuple with the following elements: 10,20, 'a', 'b', True.

# my_tuples=(10,20,'a','b',True)
# print(my_tuples[2])
# print(my_tuple+my_tuples)
# repeated_tuple=((my_tuple)*4)
# print(repeated_tuple)

# print(len(repeated_tuple))

# #Perform slicing on the tuple my_tuple to extract a new tuple withelements 'a', 'b', and True. Store the result in a variable calledsliced_tuple.
# sliced_tuple=my_tuples[2:4]
# print(sliced_tuple)

#write a program to show multiplication table of first 20 prime numbers using nested for loop

# lower=2
# upper=4
# print("Prime umbers between ",lower,"and", upper,"are:")

# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2, num):

# num = int(input(" Enter a number : "))        
# for a in range(1,11):    

#    print(num,'x',a,'=',num*a)  


# def is_prime(number):
#    if number<2:
#       return False
#    for i in range(2, int(number**0.5)+1):
#       if number % i == 0:
#          return False
#       return True
   
# # if is_prime(10):
# #    print("prime num,ber")
# # else:
# #    print("not prime")
   
# count=0
# number=1
# prime_list=[]
# while count<20:
#    if is_prime(number):
#       prime_list.append(number)
#       count=count+1
# number = number +1

# print(prime_list)


# list=[]
# for j in range(20,30):
#    prime=1
#    for i in range(2,j):
#       if j%i==0:
#          prime=0
#          break
#       if prime==1:
#          list.append(j)
# print(list)

# #write a program to find the simple intrest
# def simple_interest(p,t,r):
#    #  print('The principal is', p)
#    #  print('The time period is', t)
#    #  print('The rate of interest is',r)
     
#     si = (p * t * r)/100
     
#     print('The Simple Interest is', si)
#     return si
# simple_interest(8, 6, 8)



# #write a program to find the perimeter of the rectangular ground
# a=4
# b=6
# perimeter_rect=2*(a+b)
# print(perimeter_rect)

# #write aprgram to find the irregular bodies

# #write a program to calculate volume of the cube
# l=5
# volume_cube=l*l*l
# print(volume_cube)

# #write a program to find the square root of a number.
# num=25
# sqrt=num**(1/2)
# print(sqrt)

# #write a progrm to find the error percentage
# av=1000
# ev=500
# ep=(av-ev)/ev*100
# print(ep)

# #take a string from the user as a input and check wether the string is rishab karki or not
# str="This is playboy Paribesh Pandey"
# if str=="Rishab Karki":
#    print(True)
# else:
#    print(False)

#write a program to find the area of the circle with radius 7.5, 20.39,100,129,139,600,1000, 5.6, 8.9, 12.7, 11.12, 12.13

   

def function_pie(radius):
    return radius
radius = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str((22/7) * radius**2))




        