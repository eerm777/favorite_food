#Create a list of your 10 favorite foods in order from best to least best.
#Print the list as a numbered list
#Print the list in alphabetical order (you can create a new list or change the original one)

favorite_foods = ["Chocolate Cake", "Pasta", "Turkey Sandwich",
                  "Pumpkin Pie", "Roast Beef", "Pizza", "Potato Chips",
                  "Popcorn", "Cookies", "Broccoli"]

for i, food in enumerate(favorite_foods):
    print(f"{i+1}. {food}")

sorted_list =favorite_foods
sorted_list.sort()





