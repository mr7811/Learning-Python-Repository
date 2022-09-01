#Use a program to test if string is a palindrome.
#status: completed

# pal = input("write a word")
# y =[]

# for c in pal:
#     y.append(c)

# z= y[::-1]
# h= y[:]
# if h == z:
#     print("yes")
# else:
#     print("no not a palindrome")


#Let’s say I give you a list saved in a variable:
#  a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# y=[z for z in a if z % 2 ==0]
# print(y)

#Rock paper scissors

# p1 = input("P1 type your move, type: rock paper or scissors")
# p2 = input("P2 type your move, type: rock paper or scissors")

# if p1 == "rock" and p2 == "scissors": print ("p1 wins")
# elif p1 =="rock" and p2 =="paper": print("p2 wins")
# elif p1 == p2: print("tie")
# elif p1 =="paper" and p2 =="rock": print("p1 wins")
# elif p1 == "paper" and p2 =="scissors": print("p2 wins")
# elif p1 =="scissors" and p2 =="rock": print("p2 wins")
# elif p1 =="scissors" and p2 =="paper": print("p1 wins")
# else: print("invalid typing type again")


# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists 

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = [y for y in a if y in b]
# print(c)

# Psuedo code: print out the range of numbers of the list then check if the length is greater than 1 if it is its not aprime number 


# num = int(input("type a number to find if it is prime"))

# listRange = list(range(1,num+1))

# divisorList=[]

# for number in listRange:
#     if num % number == 0:
#         divisorList.append(number)

# if len(divisorList) > 2:print("it is not prime")
# else: print("it is prime")

#type  a string and get it backwords problem

# ask_string = input("Type in a string and get it backwards")

# y = ask_string.split(" ")
    
# z= y[::-1]

# print(z)

