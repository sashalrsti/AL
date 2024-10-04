import os
import random

text_file = 'task.txt'
skill = 0
ingredients = 0

def load(skill, ingredients):
    try:
        with open(text_file, "r") as file:
            file_data = file.read().splitlines()
            skill = int(file_data[0])
            ingredients = int(file_data[1])
        return skill, ingredients
    except FileNotFoundError:
        return 0, 0

def save_data(skill, ingredients):
    with open(text_file, "w") as file:
        file.write(f"{skill}\n")
        file.write(f"{ingredients}")
    print("Data is saved!")

def delete_file(skill, ingredients):
    with open(text_file, "w") as file:
        file.write("0\n0")

def cooking_mama():
    return random.choice(["You successfully cooked a meal! Even better than Mama!", "You burnt it. Better luck next time!"])

def start_game():
    global skill, ingredients
    print("Start playing Walmart Version of Cooking Mama!")
    skill, ingredients = load(skill, ingredients)

    while True:
        print(f"Loaded your data\nSkill: {skill}\nNumber of ingredients: {ingredients}")
        print("1. Start cooking a meal")
        print("2. Get a number of ingredients")
        print("3. Save game and exit")
        print("4. Exit and delete data")
    

        player = input("Pick a choice: ")
       
        if player == "1":
            result = cooking_mama()
            if result == "You successfully cooked a meal! Even better than Mama!":
                gain_skill = random.randint(10,50)
                skill += gain_skill
                print(f"You successfully cooked a meal! Even better than Mama! You gained {gain_skill} skill points!")
                save_data(skill, ingredients)
            else:
                lose_skill = random.randint(10,20)
                skill -= lose_skill
                print(f"You burnt your cooking. Great, Mama is now mad. You lost {lose_skill} skill points.")
                save_data(skill, ingredients)
        
        elif player == "2":
            buy_ingredient = random.randint(1,5)
            ingredients += buy_ingredient
            print(f"You got {ingredients} ingredients!")
        
        elif player == "3":
            save_data(skill, ingredients)
            break

        elif player == "4":
            delete_file(skill, ingredients)
            print("You are now quitting and deleting your data.")
            break

start_game()




        




    


