# # num = 3
# # if num >= 0:
# #     print('the number is positive')
# # else:
# #     print('the number is negative')
# #
# # num1 = 5
# # if num1>= 0:
# #     print('the number is positive')
# # else:
# #     print( 'the number is negative')
#
# # x = 10
# #
# # if x == 1:
# #     print('x is 10')
# # elif x == 5:
# #     print('x is 5')
# # elif x == 10:
# #     print('x is 10')
# # else: print('x is not 10')
#
# def raindrops(number):
#     result = ''
#
#     if number % 3 == 0:
#         result += 'Pling'
#
#     if number %5 == 0:
#         result += 'Plang'
#
#     if number % 7 == 0:
#         result += 'Plong'
#
#     if result =='':
#         result = str(number)
#
#     return result
#
# print(raindrops(15))

# text = "welcome to gomycode"
# count = 0
#
# for letter in text:
#     if letter == "o":
#         count += 1
#
# print(count)

# import random
#
# random_number = random.randint(0, 1)
#
# if random_number == 0:
#     print("Heads")
# else:
#     print("Tails")

# succesful =  False
#
# for X in range(3):
#     print(X)
#     if succesful:
#         print('it is succesful')
#         break
# else:
#     print('not succesful')

# for x in range(5):
#     print('hello', x)
#
# fruits = ['apple', 'banana', 'cherry']
#
# for x in fruits:
#     print(x + '1')

# for x in range(3):
#     print(x * 2)
#
# total = 0
# for x in range(1,11):
#     total = total + x
# print(total)

# names = ['Ada', 'caleb', 'ade']
#
# for name in names:
#     print(name.upper())
#
# for num in range(2,22,2):
#     print(num)
#
# input()
# for num in range(2, 22 * 4):
#     print(num)
# input()

# import random
#
# cointoss = random.randint(0,1)
# print(cointoss)
#
# if cointoss == 1:
#     print('tail')
# else:
#     print('head')


import random

number = random.randint(1, 100)

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

guess = int(input("Enter your guess: "))

while guess != number:

    if guess > number:
        print("Your guess is too high. Guess again.")
    else:
        print("Your guess is too low. Guess again.")

    guess = int(input("Enter your guess: "))

print("Congratulations! You guessed the number correctly!")