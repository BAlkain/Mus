#fist_name = "Beñat"
#last_name = "Alkain"
#full_name = first name +" "+ last_name
#print("Hello " + full_name)
#print(type(name))

#age = 21
#age += 1
#print("Your age is: "+str(age))
#print(type(age))

#height = 250.5
#print("Your height is:", str(height) +"cm")
#print(type(height))

#human = False
#print("Are you a human: "+str(human))
#print(type(human))

#name = "Beñat"
#age = 23
#attractive = True

#name, age, attractive = "Beñat",23, True

#print(name)
#print(age)
#print(attractive)

#Spongebob = Patrick = Sandy = Squidward = 30
#print(Spongebob)

#name = "Beñat"
#print(len(name))
#print(name.find("B"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("e"))
#print(name.replace("e","a"))
#print(name*3)

#x = 1
#y = 2.0
#z = "3"

#x= str(x)
#y=str(y)
#z= str(z)

#print("X is "+str(x))
#print("Y is "+str(y))
#print(z*3)

#name = input("What is your name? ")
#age = int(input("How old are you? "))
#height = input("How tall are you? ")

#print("Hello " + name)
#print("You are "+str(age)+" years old")
#print("You are "+str(height)+" cm tall")

#import math
# pi=-3.14
# x=1
# y=2
# z=3
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z))
# print(min(x,y,z))

# name = "Beñat Alkain"
# fist_name = name[:5]
# last_name = name[6:]
# funky_name = name[::2]
# reversed_name = name[::-1]
#
# print(fist_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])

# age = int(input("How old are you? "))
# if age == 100:
#     print("You are a century old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# temp = int(input("What is the temperature oustside? "))
# if not(temp >= 0 and temp <= 30):
#     print("The temperature is bad today!")
#     print("stay inside!")
# elif not(temp < 0 or temp >30):
#     print("The temperature is good today!")
#     print("go outside!")

# while 1==1:
#     print("Help! I'm stuck in a loop!")

# name=""
# while not name:
#     name = input("Enter your name: ")
# print("Hello "+name)

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):
#     print(i)

# for i in "Beñat Alkain":
#     print(i)

# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# rows = int(input("How many rows?:"))
# columns = int(input("How many columns?:"))
# symbol = input("Enter a symbol to use:")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i=="-":
#         continue
#     print(i,end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# food = ["pizza","hamburger","cheese", "hotdog"]
# food[0] = "sushi"
# print(food[0])
# food.append("ice cream")
# food.remove("hamburger")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()
# for x in food:
#     print(x)

# drinks = ["coffee","soda","tea"]
# dinner = ["pizza","hamburger","hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks,dinner,dessert]
# print(food[1][2])

# student=("Beñat",21,"male")
# print(student.count("Beñat"))
# print(student.index("male"))
# for x in student:
#     print(x)
#
# if "Beñat" in student:
#     print("Beñat is here!")

# utensils = {"fork","spoon","knife"}
# dishes={"bowl","plate","cup","knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dinner_table=utensils.union(dishes)
# for x in dinner_table:
#     print(x)

# print(utensils.difference(dishes))
# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# capitals={'USA':'Washington DC','India':'New Dehli','China':'Beijing','Russia':'Moscow'}
# # print(capitals['Russia'])
# # print(capitals['Germany'])
# # print(capitals.get('Germany'))
# # print(capitals.keys())
# # print(capitals.items())
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
# for key,value in capitals.items():
#     print(key,value)

# name = "beñat Alkain!"
# # if(name[0].islower()):
# #     name = name.capitalize()
# first_name = name[:5].upper()
# last_name = name[6:].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)

def hello(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day")

hello("Beñat","Alkain",23)

