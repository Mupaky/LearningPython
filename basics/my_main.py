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

def repeat(f, n):
    return [f() for i in range(n)]
# repeat(lambda x: print(x * x), 5)


def mapply(f, lst):
    return [f(x) for x in lst]
# mapply(lambda x: print(x * 5 ), "Hello world")

#slising the String
# txt = "The best things in life are free!"
# print(txt[:])
#modify the String
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

# print("\u0065")

# def fib(n):
#     if n < 1: return 0
#     if n < 2: return 1
#     return fib(n-1) + fib(n-2)
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
