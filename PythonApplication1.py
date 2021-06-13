import string
import random
import sys

class meal:
    name = ""
    ingredients = []
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

full_meal_list = []

def initializeMainList():
    f_meal = open("Meals.txt", "r")
    for item in f_meal.readlines():
        meal_components = item.split(':')
        meal_name = meal_components[0]
        str1 = meal_components[1]
        str1 = str1.replace('\n', "")
        meal_ingredients = str1.split('+')
        full_meal_list.append(meal(meal_name,meal_ingredients))

def updateMealText():
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

def addMealMain():
    meal_name = input("Enter meal name:")
    ingr_list = [""]
    adding = True
    while adding:
        str1 = input("Exit[x] : Otherwise enter ingredient name:")
        if str1 == "x": 
            adding = False
            break
        ingr_list.append(str1)

    full_meal_list.append(meal(meal_name, ingr_list))
    updateMealText()
    
def removeMeal():
    target = input("Meal to remove: ")
    for item in full_meal_list:
        if target == item.name:
            full_meal_list.remove(item)
            updateMealText()
            return
    print("Meal not found")

def displayMealList(meal_list):
    counter = 1
    for item in meal_list:
        print(str(counter) + ". " + item.name)
        counter += 1

def printIngredientList(target):
    counter = 1
    for item in full_meal_list[target].ingredients:
        print(str(counter) + ". " + item)
        counter += 1

def chooseFourMeals():
    available_options = len(full_meal_list)
    numbers = random.sample(range(available_options-1), 4)
    meal_options = []
    counter = 0
    for item in numbers:
        value = numbers[counter]
        meal_options.append(full_meal_list[value])
        counter += 1
    return meal_options

def acceptMealSuggestion():
    accepted = False
    while accepted != True:
        temp = chooseFourMeals()
        displayMealList(temp)
        str1 = input("Accept Plan? [y]/[n]")
        if str1 == "y":
            return temp

def findInList(meal_name, list):
    for meals in list:
        if meals.name == meal_name:
            return meals

def editMealEntry():
    displayMealList(full_meal_list)
    target = int(input("\nMeal Number to edit: "))
    func = int(input("\nWhat would you like to edit? [1] Name [2] Ingredients: "))
    if func == 1:
        full_meal_list[target].name = input("\nEnter New Meal Name: ")
    elif func == 2:
        printIngredientList(target)
        target1 = int(input("\nIngredient Number to edit: "))
        full_meal_list[target].ingredients[target1] = input("\nEnter New Ingredient Name: ")
    updateMealText()


def writeGroceryList():
    planned_meals = acceptMealSuggestion()
    with open("Grocery_List.txt", "w+") as f:
        for item in planned_meals:
            f.write("Meal name:  " + item.name + "\n\nIngredients needed:\n")
            for it in item.ingredients:
                f.write(it + "\n")
            f.write("\n")

def addMeal():
    adding = True
    while adding == True:
        addMealMain()
        str1 = input("Done? [y]")
        if str1 == "y": break

def menuSelect(select):
    if select == 1:
        writeGroceryList()
    elif select == 2:
        addMeal()
    elif select == 3:
        editMealEntry()
    elif select == 4:
        removeMeal()
    elif select == 5:
        displayMealList(full_meal_list)
    elif select == 6:
        sys.exit(0)
    else:
        return mainMenu()
    

def mainMenu():
    
    print("""
    1. Create Meal Plan
    2. Add Meal
    3. Edit Meal
    4. Remove Meal
    5. Show Meals
    6. Exit
    """)
    user_select = int(input("Enter Option: "))
    menuSelect(user_select)
    
def startProgram():
    running = True
    initializeMainList()
    while running == True:
        mainMenu()


           
startProgram()
