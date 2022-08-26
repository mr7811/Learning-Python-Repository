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