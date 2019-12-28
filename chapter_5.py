# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:46:46 2019

@author: Osheen
"""
#checking to modify
#CHAPTER 5

#practice

cars =['audi', 'tesla' , 'bmw', 'merc']
for car in cars:
    if car =='audi':
        print(car.title())
    else:
        print(car.lower())  
        
#aexercis 5.1######################
        
car='subaru'
print("car == 'subaru' I predicted rightly")
print(car =='subaru')

print("\ncar == 'mazda'  I was wrong" )
print(car == 'mazda')

food ='pizza'
print("food == 'pizza' checking for the western cusines")
print(food == 'pizza')
food_1='burger'
print("food_1 == 'burger' checking for the western cusines")
print(food_1 == 'burger')
food_2 = 'sushi'
print("food_2 == 'sushi' checking for the western cusines")
print(food_2 == 'sushi')
food_3='pasta'
print("food_3 == 'pasta' checking for the western cusines")
print(food_3 == 'pasta')
indian='roti'
print("indian == 'roti' checking for the indian cusines")
print(indian == 'roti')
indian_1= 'chawal'
print("indian_1 == 'chawal' checking for the indian cusines")
print(indian_1 == 'chawal')
print("\nMixing the order to get false statements")
print("indian== 'pizza' checking for the western cusines")
print(indian == 'pizza')
print("indian == 'burger' checking for the western cusines")
print(indian_1 == 'burger')
print("indian_1 == 'pasta' checking for the western cusines")
print(food_1 == 'pizza')
print("indian_1 == 'sushi' checking for the western cusines")
print(indian_1 == 'sushi')
print("food == 'roti' checking for the western cusines")
print(food == 'roti')
      


print("\n Conditional Tests")

car= 'bmw'
if car != 'audi':
    print( "I dont like this car")
print("\nchecking the case senstivity")
car.lower() == 'Bmw'
print(car)

n1 = 15
n1 <= 20
print( str(n1) +" you were right")
n1 >= 10
print(str(n1) +" My guesses are working")
n1> 7 and n1<100
print(str(n1) +" My lucky day")
n1<20 or n1< 21
print(str(n1) +" unbelievale")

checks= ['cow', 'sheep', 'horse', 'dog']
check='dog'
if check in checks:
    print(check + " My favorite animal")
check_1 = 'lion'
if check_1 not in checks:
    print(check_1+ " thats not a pet")


############Exercise %.3 to 5.7################

alien_color= 'green'
if alien_color == 'green':
    print("you earned 5 points to shoot " + alien_color +" alien.")
    
alien_color_2= 'red'
if alien_color_2 == 'green':
    print("you earned 5 points to shoot " + alien_color_2 +" alien.")
else:
    print("try again")
    
    
alien_color_3 = 'red'
if alien_color_3 =='green':
     print("you earned 5 points to shoot " + alien_color_3 +" alien.")
if alien_color_3 != 'green':
     print("you earned 10 points to shoot " + alien_color_3 +" alien.")
       
alien_color_4='blue'
if alien_color_4 =='green':
     print("you earned 5 points to shoot " + alien_color_4 +" alien.")   
else:
    print("you earned 10 points to shoot " + alien_color_4 +" alien.")
    
alien_color_5='yellow'
if alien_color_5 =='green':
     print("you earned 5 points to shoot " + alien_color_5 +" alien.")  
elif alien_color_5 =='yellow':
     print("you earned 15 points to shoot " + alien_color_5 +" alien.")  
elif alien_color_5 =='red':
     print("you earned 20 points to shoot " + alien_color_5 +" alien.")  


print ("\nIF ELIF ELSE")
age = 7
if age < 2:
    print("person is a baby")
elif age <4:
    print("the person is a toddller")
elif age <13:
    print("the person is a kid")
elif age <20:
    print("the person is a teenager")
elif age <65:
    print("the person is a adult")
else:
    print("the person is an elder")
    
    
fruits=['mango','cherry','orange','apple','berry']
fav_fruits=['banana','grapes']
fruit = 'mango'
if fruit in fruits:
    print(fruit+ " is just a fruit.")
if fruit in fav_fruits:
    print(fruit + " is my favorite fruit")
                   


                                              


                                              



                                              


                                              


    
     
     
     
     