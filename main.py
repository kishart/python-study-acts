
#print ("Hello World!")

#coding exercise
#character_job="pirate"
#character_ride="ship"
#character_souvenir="gold"
#character_pet="parrot"

#print("There was once a " + character_job + " who loved adventure.")
#print("The " + character_job + " would take her " + character_ride + " to unknown places.")
#print("She brings home a lot of " + character_souvenir)
#print("Then she goes home to her pet " + character_pet + ", Chuckles.")


#print("Roses are red, violets are blue")

#if 10>7:
   # print("ten is greater than seven!")
#if 16<42:
   # print("sixteen is less than forty-two!")

#print("a long time ago, in a galaxy far, far away...")


#def nice_day(name):
#    print("Have a nice day, " + name + "!")

#nice_day("Puso")


#march 9 act: input function
#name = input("Enter your name: ")
#print("Hello, " + name + "!")

#input function number dli pwede ang plus 
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

#print("The first number is " , num1 , "while the second number is " , num2 )

# input add numbers 
#def addNum(num1, num2):
 #   total = num1 + num2
 #   return (total)
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter first number: "))

#print ("Total: " ,addNum(num1, num2))


#activity input
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#favColor = input("Enter your favorite color: ")
#favMov = input("Enter your favorite movie: ")
#mobileNum = int(input("Enter your mobile number: "))
#motto = input("Enter your motto in life: ")

#print("My name is " + name + ".")
#print("I am " , age , "years old.")
#print("My favorite color is " + favColor + ".")
#print("My favorite movie is " , favMov , ".")
#print("My mobile number is " , mobileNum , ".")
#print("My motto in life is " + motto + ".")



#activity data types

#print(10>7)
#print(str(73911))
#print(tuple("Thank God is Friday!"))
#print (float(4302))
#print(int(3299.35640))


#march 10 classes
#class Customers:
 #   greeting ="Welcome to the coffee palace!"

#c_1=Customers()
#c_1.name ="Samirah"
#c_1.beverage = "Iced Caffe Latte"
#c_1.food = "Cinnamon roll"
#c_1.total = 225

#c_2=Customers()
#c_2.name ="Jerry"
#c_2.beverage = "Caramel macchiato"
#c_2.food = "Glazed doughnut"
#c_2.total = 230

#print(Customers.greeting)
#print(c_1.beverage)
#print(c_2.food)



#arithmetic operators 
#print(217 * 6)
#print(600 + 35234)
#print(67 //12)
#print(56329 %982)
#print(34**5)



#comparison and logical operators

#my_age=25
#mom_age=60
#sister_age=28

#print(mom_age<sister_age and my_age==22)
#print(mom_age==61)
#print(mom_age>34 or sister_age==22)
#print(mom_age>=54)
#print(not(sister_age<=400 and my_age==22))

#March 11 if else elif statement
#x=332
#y=2031

#if x >= y:
#   print("x is greater than or equal to y")
#elif x==y:
#   print("x is equal to y")
#else:
#   print("x is less than y")


#for loops
#furniture =["table", "chair", "cabinet","desk", "couch"]
#for x in furniture:
 #     if x == "cabinet":
 #        continue
 #     print(x)


#while loops
#i=1
#while i<15:
#   print(i)
 #  i+=1
   
#else:
#   print("i is no longer less than 15")


#March 12 init method:

#class Customers:
 #   greeting="welcone to the cofee palace"

#    def __init__(self, name, beverage, food, total):
 #        self.name=name
 #        self.beverage=beverage
#         self.food=food
#         self.total=total

#c_1=Customers("Samirah", "Iced Caffe Latte", "Cinnamon roll", 225)
#c_2=Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
#c_3=Customers("Jasmine", "Cappuccino", "Blueberry muffin", 220)
#c_4=Customers("Jasper", "Espresso", "Chocolate chip cookie", 215)
#c_5=Customers("Jenny", "Cafe Mocha", "Strawberry cheesecake", 240)

#print(Customers.greeting)
#print(c_1.name)
#print(c_1.beverage)
#print(c_1.food)
#print(c_1.total)

#print(c_2.name)
#print(c_2.beverage)
#print(c_2.food)
#print(c_2.total)


#inheritanceclass ClubMembers:
#class ClubMembers:
#   def __init__(self, name, birthday, age, favoriteFood, goal):
#        self.name = name
 #       self.birthday = birthday
#        self.age = age
#        self.favoriteFood = favoriteFood
#        self.goal = goal

#  def display1(self):
#       print("Name: ", self.name)
 #      print("Birthday: ", self.birthday)
 #      print("Age: ", self.age)
#       print("Favorite Food: ", self.favoriteFood)
 #      print("Goal: ", self.goal)

#class ClubOfficers(ClubMembers):
 #  def __init__(self, name, birthday, age, favoriteFood, goal, position):
   #     super().__init__(name, birthday, age, favoriteFood, goal)
 #       self.position = position
   #     ClubMembers.__init__(self, name, birthday, age, favoriteFood, goal)

   #def display2(self):
 #      print("Name: ", self.name)
 #      print("Birthday: ", self.birthday)
 #      print("Age: ", self.age)
 #      print("Favorite Food: ", self.favoriteFood)
  ##     print("Position: ", self.position)
#m_1 = ClubMembers("Tom", "January 15", 14, "Ice Cream", "To be happy")
#o_4 = ClubOfficers("Vera", "February 12", 13, "Pizza", "To be successful", "Treasurer")

#m_1.display1()
#o_4.display2()
       
""""dictionaries

flavors = {"vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"}
toppings = {"almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"}

ice_cream = dict(zip(flavors, toppings))
     
print(ice_cream)
ice_cream["chocolate"] = "blueberries"
ice_cream.update({"match": "pistachios", "ube": "mango slice"})
print(ice_cream)

"""
""""handling, creating and writing to a file 
f=open("pythonessay.txt", "w")
f.write("I like python because it's very interesting")
f=open("pythonessay.txt", "a")
f.write("/nI plan to learn data visualization")
f.write("/n I want to work in the field of secret")
f.write("/n secret")
f=open("pythonessay.txt", "r")
f.close()

"""
""" read mode
f=open("pythonessay.txt", "r")
print(f.read())
"""
"""single line
f = open("pythonessay.txt", "r")
print(f.readline())
"""
"""for loops
f = open("pythonessay.txt", "r")
for x in f:
  print(x)

"""
"""remove file
import os
if os.path.exists("pythonessay.txt"):
    os.remove("pythonessay.txt")

else:
  print("The file did not exist")
  
"""

print("helklw")