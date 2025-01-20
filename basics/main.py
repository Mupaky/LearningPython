# def ask_question(question, answer):
#     user_answer = input(question)
#     return user_answer.lower() == answer.lower()
#
#
# def main():
#     score = 0
#     questions = {
#         "What's the capital of France? ": "Paris",
#         "What's 2 + 2? ": "4",
#         "What's the color of the sky? ": "blue"
#     }
#
#     for question, answer in questions.items():
#         if ask_question(question, answer):
#             score += 1
#     print(f"You scored {score}/{len(questions)}")
#
#
# main()
# from typing import List, Optional
# import json
# import itertools

# slising the String
# txt = "The best things in life are free!"
# print(txt[:])
# modify the String
# a = " Hello, World! "
# print(a.upper())
# print(a.lower())
# print(a)
# print(a.strip())

# a = "Hello, World!"
# print(a.replace("H", "J"))
# a = a.split(",")
# for b in a:
#     print(b.strip())

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

#
# txt = "We are the so-called \"Vikings\"      from the north.    "
# print(txt.join("ads"))

# print(bool("Hello"))
# print(bool("0"))
#
# class myclass():
#   def __len__(self):
#     return 0
#
#   def myFunction(self):
#       return True
#
#
#
# myobj = myclass()
# print(bool(myobj))
# print(myobj.myFunction())

# def myFunction() :
#   return True
#
# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

# x = 201
# y = 100
# print(complex(x ** y))
# print(x // y)
# x ^= 1
# print(x)
# if x is not y:
#     print("Not The Same Object")
# else:
#     print("They are the same object")
#
# sequenceOne = "Helloow"
# sequenceTwo = "Helloow World"
#
# if sequenceOne not in sequenceTwo:
#     print("Not The Same sequence")
# else:
#     print("Returns True if a sequence with the specified value is present in the object")


# thislist = ["apple", "banana", "cherry"]
# print(thislist[-3])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
#
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[3:] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# del thislist[len(thislist)-1]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# for i in thislist:
#   print(i)
# #Same as the one above but more adaptable
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])
#
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i <= len(thislist)-1:
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# # newlist = [x.upper() for x in fruits]
# # newlist = ['hello' for x in fruits]
# newlist = [x if len(x) >= 5 else "orange" for x in fruits]
# print(newlist)

# def myfunc(n):
#   return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)
#
# y = 10
# x = y
# y -= 5
# print(x)
# thislist = ["apple", "banana", "cherry"]
# thislistTwo = thislist
# thislist.clear()
# print(thislistTwo)

# list1 = ['a', 'b' , 'c']
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# green, yellow, *red = fruits
#
# print(green)
# print(yellow)
# print(red)
#
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
#
# people = {("Gergana", "Goncheva"): 27, ("Georgi", "Zhelev"): None}
#
# vals = list(people.values())
# keys = list(people.keys())
#
# new_dict = dict(zip(keys, vals))
# print(new_dict)
#
# names = ["Gergana", "Gergana", "Georgi"]
#
# print(set(names))
#
# print(people)
#
#
# print(len(mytuple))
#
# print(mytuple.__len__())
# print(mytuple)


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.keys()
#
# print(x) #before the change
#
# car["color"] = "white"
#
# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.values()
#
# print(x) #before the change
#
# car["year"] = 2020
#
# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.items()
#
# print(x) #before the change
#
# car["year"] = 2020
#
# print(x) #after the change

# #deleting everything even dict and more variables
# x = 5
# print(x)
# del x
# #this will throw an error
# print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)
#
# newDict = mydict.copy()
# print(newDict)
#
# newDict.pop("brand")
# print(thisdict)
# print(mydict)
# print(newDict)

# if 5 > 2:
#     print("Yes")

# а = 5
# isinstance(а)

# a = "asd"
# b = "as"
# c = "d"
# d = b + c
# print(a is d)
# print(a is (b+c))

# a = [1, 2, 3]
# a.reverse()
# print(sorted(a) + a)
# print(a.sort())
# print(a)
# print(a.count(4))

# import platform
#
# x = dir(platform)
# print(platform)
# import datetime
#
# x = datetime.datetime.now()
#
# print(x.year)
# print(x.strftime("%A"))
#
# # In format month/day/year
# print(x.strftime("%x"))


# def myfunc1():
#     x = "Jane"
#
#     def myfunc2():
#         nonlocal x
#         x = "hello"
#
#     myfunc2()
#     return x
#
#
# print(myfunc1())

# t = tuple(["str"])
# print(hash(t))
# t[0][0] = "a"
# print(t)

# a = {1, 2, 3}
# b = {4, 5}
# print(list(a) + list(b))

# u = {"a": 1}
# del u["a"]
#
# print(u)


# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def __init__(self, name, age, grades):
#         super().__init__(name, age)
#         self.grades = grades


# s = Student("Gosho", 32)
# s.grades = {"Math": 6, "English": 5, "Geography": 4.5}

# t = Student("Gosho", {"Math": 56, "English": 6, "Geography": 3})
# print(f"{s} , {t}")


# class example:
#
#     def __init__(self):
#         print("One")
#
#     def __init__(self):
#         print("Two")
#
#     def __init__(self):
#         print("Three")
#
#
# e = example()

# a = Person("Ivan", 30)
# b = Person("Ivan", 42)
#
# print(a == b)
#
# c = Person(1, 30)
# d = Person(1, 42)
#
# print(c == d)
# print(hash(1) == hash(1))
# print(hash("Ivan") == hash("Ivan"))
#
# for i in range(110):
#     print(i)

# print(bool([0]))

# print([i for i in range(10)] == [0,1,2,3,4,5,6,7,8,9])

# a = ['a', 's', 'd', 'f', 'g', 'h']
#
# print(a[::-1])

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.name == other.name
#
#     def __hash__(self):
#         return hash(self.name)
#
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"
#
#
# a = Person("Gosho", 30)
# b = Person("Gosho", 43)
#
# [print(x) for x in ["Are those two objects same?", hash(a) == hash(b), a, b]]

# Comprehension dict/list/set
# uneven = {x//2: x for x in range(100) if x % 2 != 0}
# print(uneven)
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def throw_up(self):
#         print("Ball of fur out")
#
#     def make_sound(self):
#         print("Meow")
#
#
# my_cat = Cat("ryan", 14)
# my_cat.throw_up()
# my_cat.make_sound()
# print(my_cat.name)
# print(my_cat.age)


# Homework
# def add_expense(expenses):
#     try:
#         amount = float(input("Enter expense amount: "))
#         expenses.append(amount)
#     except ValueError:
#         amount = 0
#
#
# def total_expenses(expenses):
#     return sum(expenses)
#
#
# def main():
#     expenses = []
#     while True:
#         add_expense(expenses)
#         if input("Add another expense? (y/n): ") != 'y':
#             break
#
#     print(f"Total expenses: ${total_expenses(expenses):.2f}")
#
#
# main()


# for i in range(10000):
#     if i == 9:
#         print(i)
# else:
#     print(-1)
# x = 5

# print(~-1)

# u = {1: 2, 2: 3, 'a': 4}
# p = list(u.values())
#
# print(p[1:2])


# x = 5
#
# y = x ** 2
# y += 1
#
# print(x := y, x)


# is_prime = lambda x: all([x % i != 0 for i in range(2, x // 2 + 1)])
#
# [print(h) for h in range(10000) if is_prime(h) and h != 0]
# def my_lambda(y):
#     return lambda z : z * y
#
#
# my_doubler = my_lambda(5)
# print(my_doubler(5))
#
#
# def myfunc(n):
#     return lambda a : a * n
#
#
# mydoubler = myfunc(2)
# print(mydoubler(11))


# t = (u := 2)
#
# print(t)

# import os

# file = open('ok.txt', 'a')
#
#
# file.write("hohohoho\nhohoho")


# file = open('ok.txt', 'a')
# file.write('Hello World\n')
# file.write('My Name is')
# file.close()
# file = open('ok.txt', 'rt', encoding='utf-8').readline()
# my_list = []
# [my_list.append(x) for x in file.split( )]
# my_list = [y for y in my_list]
# print(my_list)


# def capital_indexes(string):
#     return [x for x in range(len(string)) if string[x].istitle()]
#
#
# print(capital_indexes('HeLlO'))


# def mid(string):
#     if len(string) % 2 == 0:
#         return ""
#     else:
#         return string[len(string) // 2]


# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
#
#
# def online_count(dct):
#     return list(dct.values()).count('online')
#
#
# print(online_count(statuses))


# def random_number():
#     return math.ceil(random.random() * 100)
#
#
# for x in range(10000000):
#     y = random_number()
#     print(y) if y == 99 else ""

# def only_ints(x, y):
#
#     if isinstance(x, int) and isinstance(y, int) and not isinstance(x, bool) and not isinstance(y, bool):
#         return True
#     return False
#
#
# print(only_ints(1, True))


# def double_letters(string):
#     for x in range(len(string) - 1):
#         if string[x] == string[x+1]:
#             return True
#
#     return False

# def add_dots(string: str):
#     list_with_dots = ""
#     for x in range(len(string) - 1):
#         list_with_dots += string[x] + "."
#     list_with_dots += string[len(string) - 1]
#     return list_with_dots
#
#
# def remove_dots(string: str):
#     list_without_dots = ""
#     for x in range(len(string)):
#         if string[x] != ".":
#             list_without_dots += (string[x])
#     return list_without_dots
#
# print(add_dots("test"))
# print(remove_dots(add_dots("test")))


# def count(string: str):
#     list_of_words = string.split("-")
#     counter = 0
#     for x in list_of_words:
#         if is_containing_vowel(x):
#             counter += 1
#     return counter
#
#
# def is_containing_vowel(word):
#     for letter in word:
#         if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
#             return True
#     return False
#
#
# print(count("met-a-phor"))

# def is_anagram(first, second):
#     if len(first) != len(second):
#         return False
#     first_word = list(first)
#     second_word = list(second)
#
#     for letter in first_word:
#         if second_word.__contains__(letter):
#             second_word.remove(letter)
#     if not second_word:
#         return True
#     return False
#
#
# print(is_anagram("typhoon", "opython"))

# def flatten(lists):
#     new_list = []
#     for a_list in lists:
#         new_list.extend(a_list)
#     return new_list
#
# print(flatten([[1, 2], [3, 4]]))


# import random
#
#
# def play_game():
#     number = random.randint(1, 100)
#     guess = None
#     attempts = 0
#
#     while guess != number:
#         guess = int(input("Guess a number between 1 and 100: "))
#         attempts += 1
#
#         if guess < number:
#             print("Too low!")
#         elif guess > number:
#             print("Too high!")
#
#     print(f"Correct! It took you {attempts} attempts.")
#
#
# def main():
#     while input("Play the game? (y/n): ") == 'y':
#         play_game()
#
#
# main()


# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     return x / y if y != 0 else "Cannot divide by zero!"
#
#
# def main():
#     while True:
#         x = float(input("Enter first number: "))
#         y = float(input("Enter second number: "))
#         operation = input("Choose operation (+, -, *, /): ")
#
#         if operation == '+':
#             print("Result:", add(x, y))
#         elif operation == '-':
#             print("Result:", subtract(x, y))
#         elif operation == '*':
#             print("Result:", multiply(x, y))
#         elif operation == '/':
#             print("Result:", divide(x, y))
#         else:
#             print("Invalid operation.")
#
#         if input("Continue? (y/n): ") != 'y':
#             break
#
#
# main()

# import random
#
#
# def shorten_url(url):
#     return f"http://short.ly/{random.randint(1000, 9999)}"
#
#
# def main():
#     urls = {}
#     while True:
#         url = input("Enter a URL to shorten: ")
#         short_url = shorten_url(url)
#         urls[short_url] = url
#         print(f"Shortened URL: {short_url}")
#
#         if input("Shorten another URL? (y/n): ") != 'y':
#             break
#
#
# main()


# import random
#
#
# def play_round():
#     user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
#     computer_choice = random.choice(['rock', 'paper', 'scissors'])
#     print(f"Computer chose: {computer_choice}")
#
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#         (user_choice == 'paper' and computer_choice == 'rock') or \
#         (user_choice == 'scissors' and computer_choice == 'paper'):
#         return "You win!"
#     else:
#         return "You lose!"
#
#
# def main():
#     seed = int(input("Enter RNG seed: "))
#     random.seed(seed)
#     while True:
#         result = play_round()
#         print(result)
#
#         if input("Play again? (y/n): ") != 'y':
#             break
#
#
# main()

# def fibonacci(n):
#     a, b = 0, 1
#     sequence = []
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence
#
#
# def main():
#     n = int(input("Enter the number of Fibonacci terms: "))
#     print(f"Fibonacci sequence: {fibonacci(n)}")
#
#
# main()


# def largest_difference(a_list: list):
#     return max(a_list) - min(a_list)
#
# def div_3(number):
#     return number % 3 == 0


# def get_row_col(position: str):
#     if len(position) != 2:
#         return
#     col = 0
#     row = int(position[1]) - 1
#     if position[0] == "A":
#         col = 0
#     elif position[0] == "B":
#         col = 1
#     elif position[0] == "C":
#         col = 2
#
#     return tuple((row, col))
#
#
# print(get_row_col("A3"))


# strring =  "gosho"
#
# print(strring[::-1])
# def twoSum(nums: List[int], target: int) -> List[int]:
#     int_list = []
#     index = 0
#     while index < len(nums):
#         sum = 0
#         if index + 1 < len(nums):
#             sum = nums[index] + nums[index + 1]
#         if target == sum:
#             return list((index, index + 1))
#         index += 1
#     return []
#
# print(twoSum([2,7,11,15], 26))


# def addTwoNumbers(l1: Optional[List], l2: Optional[List]) -> Optional[List]:
#     list_one = l1[::-1]
#     list_two = l2[::-1]
#     number1 = 0
#     number2 = 0
#     var = ""
#     for x in list_one:
#         var += str(x)
#
#     number1 = int(var)
#     var = ""
#
#     for y in list_two:
#         var += str(y)
#
#     number2 = int(var)
#
#     number1 += number2
#     var = str(number1)
#     var = var[::-1]
#     new_list = []
#
#     for number in var:
#         new_list.append(int(number))
#
#     return new_list
#
#
# print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))


# def lengthOfLongestSubstring(s: str) -> int:
#     old_count = 0
#     new_count = 0
#     index_of_repeating = 0
#     index = 1
#     while index < len(s):
#         sub = s[index_of_repeating:index]
#         for x in sub:
#             sub_index = sub.index(x)
#             if sub_index < len(sub):
#                 if x in sub[sub_index + 1:]:
#                     index_of_repeating = sub.index(x) + 1
#                     break
#                 else:
#                     new_count += 1
#         index += 1
#         if old_count < new_count:
#             old_count = new_count
#         new_count = 0
#     return old_count
#
# print(lengthOfLongestSubstring("pwwkew"))

# import os

# print(dir("folder"))
# file = open("folder\\newpython.py", "a")
#
# file.write("def my_def():\n    print('hello geri')"
#            "\n \ndef another(x):\n    print(x)")
#
# file.close()
#
# from folder import newpython
#
# newpython.my_def()
# newpython.another(2)

# strt = bytearray("dsd", 'utf-8')
# print(strt)

# os.remove("folder")
#
# print("\uff27\uff25\uff32\uff29\u2764")
#
# print('22222' == '22222')

# u = 'abcdé'
# print(ord(u[-1]))

# s = "a\xac\u1234\u20ac\U00008000"
#
# print([ord(c) for c in s])
# s = "name".encode('utf-8')
# print(s.decode('utf-8'))
# print("name".encode('utf-8'))
#
# print('I am on \N{FIRE}!')
# print('I am on \N{WHITE CHESS KNIGHT}!')
# print(ord('\N{FIRE}'))


# import unicodedata


# u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)
#
# for i, c in enumerate(u):
#     print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
#     print(unicodedata.name(c))
#
# # Get numeric value of second character
# print(unicodedata.numeric(u[1]))

# for x in range(1000000):
#     try:
#         if str(x).encode('utf-8') != '\ud800':
#             print(chr(x))
#     except NameError:
#         print(NameError)

# print(unicodedata.name('ퟪ'))
# print(unicodedata.category('ퟪ'))
# print(unicodedata.name('A'))
# print(unicodedata.category('A'))
# print(unicodedata.category('a'))
#
# print(unicodedata.name('Б'))
# print(unicodedata.category('Б'))
# print(unicodedata.category('б'))

# print(unicodedata.normalize('NFD', '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'))


# import unicodedata
#
# def compare_caseless(s1, s2):
#     def NFD(s):
#         return unicodedata.normalize('NFD', s)
#
#     return NFD(NFD(s1).casefold()) == NFD(NFD(s2).casefold())
#
# # Example usage
# single_char = 'ê'
# multiple_chars = '\N{LATIN CAPITAL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
#
# print(compare_caseless(single_char, multiple_chars))
# print(single_char.casefold().encode('utf-8'))
# print(multiple_chars.casefold().encode('utf-8'))
# print(f'{single_char.casefold()}  and  {multiple_chars.casefold()}')

# import re
# p = re.compile(r'\f+')
#
# s = "Over \u0e55\u0e57 57 flavours"
# m = p.search(s)
# print(s)
# print(m)
# print(repr(m.group()))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person = Person("Georgi", 30)
#
# print(f"Name: {person.name}\nAge: {person.age}")
#
# del person

# for x in [1,2,3,4,5]:
#     print(x)
#
# print(x + 1)
# del x
#
# x = 7
# print(x)

# mystr = "banana"
# myit = iter(mystr)
# myit2 = iter(mystr)
#
# print(f"{next(myit)}{next(myit)}{next(myit)}{next(myit)}{next(myit)}{next(myit)}")
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(next(myit2))
# print(sum([1, 2, 3, 4, 5]))


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)
#
# for x in "myiter":
#     print(x)
#
# print(x)


# def myfunc():
#   x = 300
#   print(x)
#
# myfunc()
#
# print(x:=5)

# def myfunc():
#     global x
#     x = 300
#
#     #Use global if you want to change global variable in the scope
#     def myinnerfunc():
#         global x
#         x = 5
#         print(x)
#
#     myinnerfunc()
#
#
# myfunc()
#
#
# def another_function():
#     print(x)
#
#
# another_function()


# def myfunc1():
#     x = "Jane"
#
#     def myfunc2():
#         nonlocal x
#         x = "hello"
#
#     myfunc2()
#     return x
#
#
# print(myfunc1())

# import sys as s
#
#
#
# # print(s.warnoptions)
# for x in "utf-8":
#     print(ord(x))

# # print("\u0065")
# from functools import cache
# @cache
# def fib(n):
#     if n < 1: return 0
#     if n < 2: return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(100))
#
# print(fib(100))

# def f(a=[]):
#     a.append(1)
#     return a
#
# f()
#
# print(f())

# import json
#
# file = open("folder\\data.json", "a")
#
#
# data = [{
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York",
#     "isEmployed": True,
#     "skills": ["Python", "Data Analysis", "Machine Learning"],
#     "education": {
#         "undergraduate": "Computer Science",
#         "postgraduate": "Data Science"
#     }
# }]
#
# y = json.dumps(data)
#
# file.write(y)
# file.close()
#
# file = open("folder\\data.json", "rt")
#
# z = json.loads(file.read())
#
# print(z[0]['age'])


# def fib(n):
#     if n < 1:
#         return 0
#     if n < 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(10))

# x = {i for i in [1, 2, 3, 4, 5, 6] if i % 2 != 0}
#
# print(x)

# y = {1: 2, 3: 4, 5: 6, 7: 8}
#
# for z, val in y.keys():
#     print(z)
#     print(val)


# print(r"\n" == "\\n")
#
#
#
#
#
# print([1, 2, 3] + [[2]])


# def f(a, b=1, c=2, d=3, e=4, f=5):
#     print(a+b+c+d+e+f)
#
# print(f(4))
#
# print(f)


# def sumv(*args):
#     return args[0] + sumv(*args[1:]) if len(args) > 0 else 0
#
# print(sumv(1,2,3,4,5))

# def pro(*args, **kwargs):
#     print(args, kwargs)
#
#
# # pro()
#
# pro(1, 2, 3, *[2, 3, 4, 5], json.loads('{"name":"John", "age":30, "car":null}'))


# def sumv(*args):
#     return args[0] + sumv(*args[1:]) if len(args) > 0 else 0
#
#
# print([1, 2, 3, 4, 5])

# def repeat(f, n):
#     return [f() for i in range(n)]
# repeat(lambda x: print(x * x), 5)


# def mapply(f, lst):
#     return [f(x) for x in lst]
# mapply(lambda x: print(x * 5 ), "Hello world")

# index = 0
#
# path = "test.txt"
# file = open(path, "a")
# file.write(f"{index}: New line\n")
# file.close()
#
# index += 1
#
# file = open(path, "a")
# file.write(f"{index}: New line\n")
#
# file_context = open(path, "rt").read()
# print(file_context)
#
# file.close()
#
# file_context = open(path, "rt").read()
# print(file_context)
#
#
# index += 1
#
# file = open(path, "a").write(f"{index}: New line\n")


# file_context = open(path, "rt").read()
# print(file_context)


# help("__init__")

# import my_main as my
#
# dir(my)

# f = lambda x, l: print(x * i) for i in l
#
# for i in map(f([]), [1, 2, 3, 4, 5]):
# print([5 * x for x in [1, 2, 3, 4, 5]])


# def fun_decorator(fun):
#     def inner():
#         fun()
#         print("You become a zombie")
#     return inner
#
# @fun_decorator
# def be_real():
#     print("You are real person")
#
#
# be_real()

# def my_func(*args):
#     my_list = [1, 2, 3, 4, 5]
#     my_list += list(*args)
#     print(my_list)
#
#
# my_func([5, 4, 3, 2, 1])

# start = 0
# def my_gen(s=1):
#     for i in range(1, 101, 5):
#         yield i
#         yield i+100
#
# for i in my_gen():
#     print(i)

# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# seq2 = []
# def sq(x):
#     return x * x
#
# for i in map(lambda x: x * x, seq):
#     seq2.append(i)
#
# print(seq2)
#
# for j in filter(lambda x: x % 2 == 0, seq):
#     print(j)
#
# import functools as f
#
# def sum2():
#     a = 200
#     return a
#
# add = lambda x, y: x + y
# mut = lambda x, y: x * y
#
# print(f.reduce(add, seq))
# print(f.reduce(mut, seq))
# print(f.reduce(add, ["geeks", "for", "geeks"]))


# from typing import final
# from typing import Final
#
# STATICC = Final[int: 10]
#
# print(STATICC.__str__())


# def fib(n):
#     if n < 1: return 0
#     if n == 1: return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# def printer(f, name):
#     def inner(*args, **kwargs):
#         print(f"{name} was called with args {args} and {kwargs}")
#         return f(*args, **kwargs)
#
#     return inner
#
#
# fib = printer(fib) # Decorate the function with printer
# fib(5) # Prints 15 lines like this: "fibonacci was called with args (5,) and {}" and returns 5

# def f(n):
#     print(f"Now printing n: {n}")
#     if len(n) > 100: return 0
#     return f(n * 2)
#
#
# def printer2(f, name):
#     def inner(*args, **kwargs):
#         print(f"Name: {name} was called with {args} and {kwargs}")
#         return f(*args, **kwargs)
#
#     return inner
#
#
# f = printer2(f, "Function f")
# f([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


# f = lambda x: lambda y: y * y
# k = f(5)
# print(k(5))


# l = [1, "2"]
# print(l)


# list = [1, 2, 3, 4, 5, 6, 7]
#
# value = 'yes' if True else 'no'
# print(value)

# print(dir(itertools))


# import sys


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Code to execute before calling the original function
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)  # Call the original function with any arguments
#         # Code to execute after calling the original function
#         print("Something is happening after the function is called.")
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("Alice")


# def my_decorator(fun):
#     def wrapper(*args, **kwargs):
#         print("Inner decorator called")
#         result = fun(*args, **kwargs)
#
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def my_print(name):
#     print(f'This is the x : {name}')
#
# my_print("Alice")


# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         sorted_nums = sorted(nums1 + nums2)
#         if len(sorted_nums) % 2 == 0:
#             x = sorted_nums[int(len(sorted_nums) / 2 - 1)]
#             y = sorted_nums[int(len(sorted_nums) / 2)]
#             return (x + y) / 2
#         return sorted_nums[int((len(sorted_nums) - 1) / 2)]
#
#
# sol = Solution()
#
# print(sol.findMedianSortedArrays([1,2], [3]))


# def my_generator(nums):
#     for num in nums:
#         if num % 2 != 0:
#             yield num + 10000000
#
#
# my_gen = my_generator(range(10000))
#
# print(my_gen.__next__())
# print(my_gen.__next__())
# print(next(my_gen))
#
# hoho = iter("sda&&&&~)S)S)S)S)Ý")
# print(type(hoho))

# lis = iter(range(10))
#
# for x in range(20):
#    print(next(lis))


# print(~0+1)


# def my_func(a, b, *args, t=5):
#     return args
#
# print(my_func(2,3, 4, 3, 2, 1, t=2))

# def my_docstring_function():
#     """This function is created to
#     say hello to the world
#     :return: "Hello world!"
#     """
#
#     def inner():
#         print("Hiiii")
#
#     inner()
#     return "Hello world!"
#
#
# (a, *b, c) = [1, 1, 2, 3, 3]
#
# print(b)
# print(help(my_docstring_function))
# print(my_docstring_function())
# print(dir(my_docstring_function))


# from functools import cache
#
# @cache
# def fib(n):
#     if n < 1: return 0
#     if n == 1: return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(55))

# from functools import partial
#
# def b():
#     res = []
#     for i in range(10):
#         res.append(partial(lambda x, i: x + i, i=i))
#     return res
#
#
# print(list(map(lambda x: x(0), b())))

# from abc import ABC, abstractmethod
#
# class Walkable(ABC):
#     @abstractmethod
#     def walk(self):
#         """Abstract method that must be implemented by subclasses."""
#         pass
#
# class Person(Walkable):
#     def __init__(self, name):
#         self.name = name
#
#     def walk(self):
#         print(f"{self.name} is walking.")
#
#
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     def walk(self):
#         """Basic walking method for animals."""
#         print(f"{self.name} is walking in a basic way.")
#
#     @abstractmethod
#     def make_sound(self):
#         """Abstract method that each animal subclass must implement."""
#         pass
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_sound(self):
#         print(f"{self.name} says Woof!")
#
#     # Optionally, override the walk method
#     def walk(self):
#         print(f"{self.name} the dog is happily walking!")
#
#
#
# # Creating objects
# person = Person("Alice")
# dog = Dog("Buddy")
#
# # Calling walk method
# person.walk()  # Output: Alice is walking.
# dog.walk()     # Output: Buddy the dog is walking.

# class Koko():
#     def __str__(self):
#         return "Hello KKKKKK"
# k = Koko()
# print(k)
# print(repr(k))


# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#
# p = Person("koko")
# p.name = "dsada"
# print(p.name)

# import time
#
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute")
#         return result
#     return wrapper
#
# @timing_decorator
# def calculate_sum(n):
#     return sum(range(n))
#
# calculate_sum(100000000)

# class Calculator:
#
#     def add(self, a):
#         pass
#
#     def add(self, a, b=0, c=0):
#         return a + b + c
#
#
# calc = Calculator()
# print(calc.add(5))
# print(calc.add(5, 10))
# print(calc.add(5, 10, 15))


# class Point:
#     def __new__(cls, x, y):
#         instance = super().__new__(cls)
#         instance._x = x
#         instance._y = y
#         return instance
#
#     @property
#     def x(self):
#         return self._x
#
#     @property
#     def y(self):
#         return self._y
#
#     def __setattr__(self, name, value):
#         raise AttributeError("Cannot modify immutable instance")
#
#
# point = Point(5, 10)
# print(point.x, point.y)  # Output: 5 10
#
# try:
#     point.x = 20
# except AttributeError as e:
#     print(e)
#
# class Wedding():
#     bride = "GerGon"
#     groom = "GeoZhe"
#
#     def __init__(self, bride_family:list, groom_family:list, friends:list):
#         self.guests = bride_family + groom_family + friends
#
#     def start_wedding(self, status):
#         if(status == True):
#             for guest in self.guests:
#                 self.send_invite(guest)
#         return "What a wonderful day!"
#
#
#     def send_invite(self, guest):
#         # Add address to the invite and make it with personal touch
#         print(f"{guest} is invited!")
#
# wedding = Wedding([])
#
# wedding.start_wedding(True)

# def f(arg: str) -> int:
#     return len(arg)


#ERROR
# def f(x: int | float) -> int | float:
#     return x * x
#
# f("sda")


# import is_squares
#
# def main():
#     """
#     You are expected to write a Python function that is passed a list of
#     integers and returns True / False depending on whether all numbers
#     in the list are squares of integers, themselves.
#
# Note: You are NOT allowed to edit main.py and will receive an error if you do so!
# Note: You have only THREE (3) attempts. After that, you won't be able to Grade your solution.
#     :return:
#     """
#     numbers = []
#     while True:
#         numstr = input("Enter a number: ")
#         numbers.append(int(numstr))
#         if input("Add another number? (y/n): ") != 'y':
#             break
#     print(is_squares.is_list_squares(numbers))
#
# if __name__=="__main__":
#     main()

# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# IndentationError
# for i in range(10):
# print(19)

# class R:
#     a = 1
#     def __init__(self):
#         self.a = 2 # This would just overshadow R.a
#         self.b = 2
#     def c(self, arg):
#         print(self, arg)
#
# r = R()
# print(r.a, r.b) # First is class variable, second is instance variable
# print(r.c(42), R.c(r, 42)) # Same result
#
# print(R.a)
# R.a += 1
# print(R.a)

# class A: pass
# class B(A): pass
# class C(A,B): pass # TypeError: Cannot
# #create a consistent method resolution
# #order (MRO) for bases A, B
# a = "5"
# b = "5"
# print(a + b)


# print("sorry no sorry \n" * 100)


# !/usr/bin/env python3

# class TuringMachine:
#     def __init__(
#             self,
#             tape=None,
#             blank_symbol="_",
#             transitions=None,
#             start_state="q0",
#             accept_state="q_accept",
#             reject_state="q_reject",
#     ):
#         """
#         Initialize a Turing Machine.
#
#         :param tape: list of symbols representing the initial tape content
#         :param blank_symbol: symbol denoting a blank
#         :param transitions: a dict representing the transition function
#             {
#                 (current_state, current_symbol): (next_state, symbol_to_write, move_direction)
#             }
#         :param start_state: the starting state
#         :param accept_state: the accepting state
#         :param reject_state: the rejecting state
#         """
#         # If no tape is provided, use a single blank symbol
#         self.tape = tape if tape else [blank_symbol]
#         self.blank_symbol = blank_symbol
#
#         # Transition function: dict[(current_state, symbol_on_tape)] = (next_state, symbol_to_write, move_dir)
#         self.transitions = transitions if transitions else {}
#
#         # Machine states
#         self.start_state = start_state
#         self.accept_state = accept_state
#         self.reject_state = reject_state
#
#         # Initialize machine
#         self.current_state = self.start_state
#         self.head_position = 0  # Start on the leftmost symbol of the tape
#
#     def step(self):
#         """Perform a single step of the Turing Machine."""
#         # 1. Read the current symbol under the head
#         current_symbol = self.tape[self.head_position]
#
#         # 2. Look up the transition in the dictionary
#         if (self.current_state, current_symbol) not in self.transitions:
#             # No valid transition => We reject by default (or just stop)
#             self.current_state = self.reject_state
#             return
#
#         next_state, write_symbol, move_dir = self.transitions[(self.current_state, current_symbol)]
#
#         # 3. Write the symbol on the tape
#         self.tape[self.head_position] = write_symbol
#
#         # 4. Update the state
#         self.current_state = next_state
#
#         # 5. Move the head
#         if move_dir == "R":
#             self.head_position += 1
#         elif move_dir == "L":
#             self.head_position -= 1
#         else:
#             raise ValueError("Invalid move direction. Use 'L' or 'R'.")
#
#         # Make sure the head is always within bounds of the tape
#         if self.head_position < 0:
#             # Extend the tape on the left with a blank symbol
#             self.tape.insert(0, self.blank_symbol)
#             self.head_position = 0
#         elif self.head_position >= len(self.tape):
#             # Extend the tape on the right with a blank symbol
#             self.tape.append(self.blank_symbol)
#
#     def run(self, max_steps=1000, verbose=False):
#         """
#         Run the Turing Machine until it reaches the accept or reject state,
#         or until max_steps is exceeded.
#
#         :param max_steps: safety limit for the number of steps to avoid infinite loops
#         :param verbose: if True, prints debugging information at every step
#         :return: "ACCEPT", "REJECT", or "TIMEOUT"
#         """
#         steps = 0
#         while steps < max_steps:
#             if verbose:
#                 self.print_debug_info(steps)
#
#             # Check if we are in accept or reject state
#             if self.current_state == self.accept_state:
#                 return "ACCEPT"
#             if self.current_state == self.reject_state:
#                 return "REJECT"
#
#             # Perform one step
#             self.step()
#             steps += 1
#
#         # If we exceed max_steps, consider it a timeout
#         return "TIMEOUT"
#
#     def print_debug_info(self, step):
#         """Helper method to print debug info about the current step."""
#         tape_str = "".join(self.tape)
#         head_marker = " " * self.head_position + "^"
#         print(f"Step {step}:")
#         print(f"  State: {self.current_state}")
#         print(f"  Tape : {tape_str}")
#         print(f"         {head_marker}")
#
#
# def main():
#     """
#     Example usage of the TuringMachine class.
#
#     This example machine increments a unary number: e.g., input '111' -> output '1111'.
#     The tape symbol '1' means a mark, '_' means a blank.
#     """
#     # Example transition rules for a unary-increment Turing Machine
#     transitions = {
#         # (current_state, current_symbol): (next_state, write_symbol, move_direction)
#
#         # We start in q0 scanning the first '1'. We move right until we find a blank.
#         ("q0", "1"): ("q0", "1", "R"),
#         ("q0", "_"): ("q1", "1", "L"),  # Once we see the blank after the last 1, we turn it into a '1' and move left
#
#         # Once we go to q1, we move left until we find a blank (to ensure we end up over the first 1).
#         ("q1", "1"): ("q1", "1", "L"),
#         ("q1", "_"): ("q_accept", "_", "R"),  # Once we pass the left boundary, we accept
#     }
#
#     # Our tape: '111' means we start with 3 marks
#     tape = list("111")
#
#     # Create the Turing Machine
#     tm = TuringMachine(
#         tape=tape,
#         blank_symbol="_",
#         transitions=transitions,
#         start_state="q0",
#         accept_state="q_accept",
#         reject_state="q_reject",
#     )
#
#     # Run the machine
#     result = tm.run(max_steps=50, verbose=True)
#     print(f"Result: {result}")
#     print(f"Final tape: {''.join(tm.tape)}")
#     print(f"Head position: {tm.head_position}")
#
#
# if __name__ == "__main__":
#     main()


# !/usr/bin/env python3
# import time
#
#
# class TuringMachine:
#     def __init__(
#             self,
#             tape=None,
#             blank_symbol="_",
#             transitions=None,
#             start_state="q0",
#             accept_state="q_accept",
#             reject_state="q_reject",
#     ):
#         """
#         Initialize a Turing Machine.
#
#         :param tape: list of symbols representing the initial tape content
#         :param blank_symbol: symbol denoting a blank
#         :param transitions: a dict representing the transition function
#             {
#                 (current_state, current_symbol): (next_state, symbol_to_write, move_direction)
#             }
#         :param start_state: the starting state
#         :param accept_state: the accepting state
#         :param reject_state: the rejecting state
#         """
#         # If no tape is provided, use a single blank symbol
#         self.tape = tape if tape else [blank_symbol]
#         self.blank_symbol = blank_symbol
#
#         # Transition function:
#         # dict[(current_state, symbol_on_tape)] = (next_state, symbol_to_write, move_dir)
#         self.transitions = transitions if transitions else {}
#
#         # Machine states
#         self.start_state = start_state
#         self.accept_state = accept_state
#         self.reject_state = reject_state
#
#         # Initialize machine
#         self.current_state = self.start_state
#         self.head_position = 0  # Start on the leftmost symbol
#
#     def step(self):
#         """Perform a single step of the Turing Machine."""
#         current_symbol = self.tape[self.head_position]
#
#         # If there's no valid transition, go to reject state
#         if (self.current_state, current_symbol) not in self.transitions:
#             self.current_state = self.reject_state
#             return
#
#         next_state, write_symbol, move_dir = self.transitions[(self.current_state, current_symbol)]
#
#         # Write the new symbol to tape
#         self.tape[self.head_position] = write_symbol
#
#         # Update the current state
#         self.current_state = next_state
#
#         # Move the head
#         if move_dir == "R":
#             self.head_position += 1
#         elif move_dir == "L":
#             self.head_position -= 1
#         else:
#             raise ValueError("Invalid move direction. Use 'L' or 'R'.")
#
#         # If the head goes out of left boundary, extend tape on the left
#         if self.head_position < 0:
#             self.tape.insert(0, self.blank_symbol)
#             self.head_position = 0
#         # If the head goes beyond right boundary, extend tape on the right
#         elif self.head_position >= len(self.tape):
#             self.tape.append(self.blank_symbol)
#
#     def run(self, max_steps=1000, step_delay=0.5):
#         """
#         Run the machine until accept or reject or until max_steps is exceeded.
#
#         :param max_steps: maximum steps to run before timing out
#         :param step_delay: time (in seconds) to wait between steps (for visualization)
#         :return: "ACCEPT", "REJECT", or "TIMEOUT"
#         """
#         for step in range(max_steps):
#             # Visualize the current step
#             self.visualize(step)
#
#             # Check if in accept or reject state
#             if self.current_state == self.accept_state:
#                 print("Machine reached ACCEPT state!\n")
#                 return "ACCEPT"
#             if self.current_state == self.reject_state:
#                 print("Machine reached REJECT state!\n")
#                 return "REJECT"
#
#             # Perform a step
#             self.step()
#
#             # Pause for a visual effect
#             time.sleep(step_delay)
#
#         print("Machine TIMEOUT: exceeded max steps.\n")
#         return "TIMEOUT"
#
#     def visualize(self, step):
#         """
#         Visualize the Turing Machine state, tape, and head position.
#         """
#         print(f"Step {step:03d} | State: {self.current_state}")
#
#         # Build a string to represent the tape
#         tape_str = ""
#         for i, symbol in enumerate(self.tape):
#             if i == self.head_position:
#                 # Mark the tape cell under the head with brackets
#                 tape_str += f"[{symbol}]"
#             else:
#                 tape_str += f" {symbol} "
#         print(f"Tape: {tape_str}\n")
#
#
# def main():
#     """
#     Example usage:
#     This Turing Machine increments a unary number on the tape.
#     For instance, '111' -> '1111'.
#     The tape symbol '1' is a mark, '_' is blank.
#     """
#     # Transition rules for a unary-increment Turing Machine
#     transitions = {
#         # (current_state, current_symbol): (next_state, symbol_to_write, move_dir)
#
#         # State q0: move right until blank, then change blank to '1' and go to q1
#         ("q0", "1"): ("q0", "1", "R"),
#         ("q0", "_"): ("q1", "1", "L"),
#
#         # State q1: move left until a blank, then accept
#         ("q1", "1"): ("q1", "1", "L"),
#         ("q1", "_"): ("q_accept", "_", "R"),
#     }
#
#     # Initial tape: 3 marks
#     tape = list("111")
#
#     # Create the TuringMachine instance
#     tm = TuringMachine(
#         tape=tape,
#         blank_symbol="_",
#         transitions=transitions,
#         start_state="q0",
#         accept_state="q_accept",
#         reject_state="q_reject",
#     )
#
#     # Run the machine with a 0.5-second delay between steps
#     result = tm.run(max_steps=50, step_delay=0.5)
#     print(f"Result: {result}")
#     print(f"Final tape: {''.join(tm.tape)}")
#     print(f"Head position: {tm.head_position}")
#
#
# if __name__ == "__main__":
#     main()

#
#
# for i in range(1, 6):
#     print(i)

# sample_list = [1, 1, 8, 4, 4, 2, 4, 8]
# my_dict = dict()
# for i in sample_list:
#     if my_dict.get(i):
#         value = my_dict.get(i) + 1
#         my_dict[i] = value
#     else:
#         my_dict.update({i: 1})
# print(my_dict)

# sample_list = ["luxuriant", "silly", "dizzy", "frightening", "blink", "silly", "enjoy", "suspend", "blink", "reward",
#                "blink", "fact", "debt", "marble", "blink", "yak", "frightening", "suspend", "debt"]
# my_dict = dict()
#
# for i in sample_list:
#     if my_dict.get(i):
#         value = my_dict.get(i) + "*"
#         my_dict[i] = value
#     else:
#         my_dict.update({i: " |*"})
#
# for item in my_dict:
#     print(item + my_dict[item])


# print(str('"""ds ad as    """').strip("\""))


# budget_value = 10.5
#
# try:
#     file = open("C:\\Users\\georg\\Desktop\\wedding\\new_file.py", "w")
#     try:
#         file.write("Username: " + input("Enter Username:\n") + "\n")
#         file.write("Password: " + input("Enter password:\n") + f"\nBudget: {budget_value}")
#     except:
#         print("Something went wrong with writing")
#
#     finally:
#         file.close()
# except:
#     print("Something went wrong with opening")
#
# try:
#     file = open("C:\\Users\\georg\\Desktop\\wedding\\new_file.py", "rt")
#     try:
#         print(file.read())
#     except:
#         print("Something went wrong with writing")
#
#     finally:
#         file.close()
#
# except:
#     print("Something went wrong with opening")

import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

# xpoints = np.array([1, 2, 6,  8])
# ypoints = np.array([3, 8, 1, 7])
# xpointssss = [7, 5, 1, 9]
#
# # plt.plot(xpoints, ypoints, marker="o", ms=20, mec="r", mfc="r")
# # plt.show()
#
# plt.plot(xpoints, ls="-.")
# plt.plot(ypoints, ls="-.")
# plt.plot([4, 6, 5, 2, 1], ls="-.")
# plt.plot(xpointssss, ls="--")
# plt.show()


# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.plot(x, y)
#
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
#
# plt.title("Sports Watch Data", fontdict=font1)
# plt.xlabel("Average Pulse", fontdict=font2)
# plt.ylabel("Calorie Burnage", fontdict=font2)
#
# plt.show()


# class Cat:
#     spicies = "ulichna"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# cat1 = Cat("Gonzo", 3)
# print(cat1.spicies)
# Cat.spicies = "domashna"
# print(Cat.spicies)
# print(cat1.spicies)







