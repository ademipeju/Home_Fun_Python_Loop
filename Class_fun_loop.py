# for i in range(6):
#     print(i)

# name= "Mike"
# num= 401
# print(name.upper())
# print(type(name))
# print(type(num))
# #range consist of start, stop, and step
# for i in range (1, 10):
#     print(i)
# #the step function 
# for i in range(5, 12, 3):
#     print(i)
# for i in range (5, 12, 3):
#     print(i)
# for school in range(2):
#     print(school)
# for muliplication in range(1,13):
#     print(muliplication*5)
# #examples of iterables are list, tuples, strings
# name_list= ["Damilola", "Tayo", "Tosin"]
# for name in name_list:
#     print(name)
# list_length= len(name_list)
# print (list_length)
# for i in range(list_length):
#     print(name_list[i])
# if i == 2:
#     name_list[i]= "Hajara"
#     print(name_list)
#     name = "President dami"
#     for letter in name:
#         print(letter)
#     for i in range(len(name)):
#         print(name[i])
#     #how to use the while loop. for while loop, you must set a condition
#     counter= 1
#     while counter < 10:
#         print("counting", counter)
#         counter+=1
#         if counter==6:
#             break
#     for letter in "Damilola":
#         print(letter)
#         break
    #for letter in the length of Damilola
LG_in_Kwara= ["Ilorin west", "Ekiti", "Oke-ero", "Ifelodun", "Barutee", "Asa"]
for LG in LG_in_Kwara:
    print(LG[-1])
# Python loops. 
#There are two primitive commands in Python
#The "while" loop and the "for" loop
# The "while" loop
i =  1
while i < 6:
    print(i)
    i += 1
#Break statement
y= 2
while y < 8:
    print(y)
    if (y==7):
        break
    y +=1
#continue statement
P = 0
while P < 6:
  P += 1
  if P == 3:
    continue
  print(P)

  w = 1
while w < 8:
  print(w)
  w += 1
else:
  print("w is no longer less than 8")
  #break statement
E=4
while E < 10:
   print(E)
   E += 1
else:
   print("I am a big girl")
City= ["Ilorin", "Lagos", "Ado"]
while City==City:
   print(City)
   break
Food= 1
while Food < 10:
   print(Food)
   Food +=1
else:
   print("Food is expensive")
#Python "For" loop
#"For" loop is use for iterating over a sequence, it can be a list, tuple, dictioanary...
fruit= ["Pawpaw", "Apple", "Banana", "Watermelon"]
for x in fruit:
   print(x)
for x in fruit:
   print(x[2])
for x in fruit:
   print(x[1])
#looping through a string
for x in "Banana":
   print(x)
#break statement using the "for" loop
cars=["Venza", "Bentley", "Rolls Royce", "BMW"]
for car in cars:
   print(car)
   if car == "Rolls Royce":
      break
for car in cars:
    print(car)
    if car == "Venza":
       break
# the "continue" statement helps to stop a loop and then continue in the next line or next character
#continue loop will not print the string or value selected.
school =["Unilorin", "Unilag", "Uniport", "UniAbuja", "Unimaid"]
school[4]= "Kwasu"
print(school)
for i in school:
   if i == "Kwasu":
      continue
   print(i)
for i in school:
   if i == "UniAbuja":
      continue
   print(i)
#The range() function
#To loop through a data set multiple times, range function is normally used and it saves a lot of time
for x in range(8):
   print(x)
for x in range(2,5):
    print(x)
#this is refered to as "start", "stop", and "step"
for x in range(2, 30, 3):
   print(x)
#Else in "for" loop
#Else is use to specify a block of code to executed after running through the loop.
for x in range(6):
   print(x)
else:
   print("finally finished")
#Using Else and Break. The Else loop will not be exceuted if it is stopped by a "break" function
for x in range(6):
   if x==3: break
   print(x)
else:
   print("finally finished")








    
    







    


