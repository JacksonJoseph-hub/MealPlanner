import string
import random

full_meal_list = []

class meal:
    name = ""
    ingredients = []
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    

def updateMeal():
    with open("Meals.txt", "w") as f:
        for item in full_meal_list:
            f.write(item.name + ":")
            for it in item.ingredients:
                if it == item.ingredients[-1] or it == item.ingredients[0]:
                    f.write(it)
                else:
                    f.write(it + "+")
            f.write("\n")
    f.close()

def addMeal():
    meal_name = input("Enter meal name:")
    #meal_name = "*" + meal_name + "-"
    ingr_list = [""]
    adding = True
    while adding:
        str1 = input("Exit[x] : Otherwise enter ingredient name:")
        if str1 == "x": 
            #str1 + "-"
            adding = False
            break
        ingr_list.append(str1)

    obj = meal(meal_name, ingr_list)
    full_meal_list.append(obj)
    



def displayTotalMealList():
    for item in full_meal_list:
        print(item.name)

addMeal()
addMeal()
updateMeal()
#print(len(full_meal_list))
#print(full_meal_list[0].name)
#f_meal = open("Meals.txt", "r")
#for item in f_meal.readlines():         
    #print(item)


            

            



#with open("Meals.txt", "w") as f_meal:
 #   try:
  #      f_meal.write("*Cheeseburger-Patty, Burger, Cheese-" + '\n')
   #     f_meal.write("*Gnocchi-Spinach, Soup, Cream-" + '\n')
#        f_meal.write("*3-4, 6, 7-" + '\n')
 #   finally:
  #      f_meal.close()

#f_meal = open("Meals.txt", "r")
#for item in f_meal.readlines():
 #   str1 = item
 #   if str1.startswith("*") != True:
 #       print("Error, meal name wrong")
 #       continue
 #   meal_components = str1.split('-')
 #   obj = meal(meal_components[0],meal_components[1])
 #   full_meal_list.append(obj)
#if full_meal_list[0] != None:
#    for item in full_meal_list:
#        print(item.name)
#        print(item.ingredients)



    #print(meal_components[0])
    #print(meal_components[1])
    
    #obj.name = meal_components[0]
    #obj.ingredients = meal_components[1]

    #print(obj.name)
    #print(obj.ingredients)


    
    #full_meal_list.append(meal(meal_components[0],meal_components[1]))
    #print(full_meal_list)
    #meal_item_name = meal_components[0]
    #print("This is your string: " + str1)
    #print("This is new: ")
    #print(str1.replace('*',''))

    #str1.split('-')

    #print(item.split('-'))
    #print("\n")





#print(f_meal.readline())


#first_meal = meal("Cheeseburger",["Patty", "Burger", "Cheese"])
#print(first_meal)