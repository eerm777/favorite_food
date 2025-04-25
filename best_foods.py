#Create a list of your 10 favorite foods in order from best to least best.
#Print the list as a numbered list
#Print the list in alphabetical order (you can create a new list or change the original one)

favorite_foods = ["Chocolate Cake", "Yaki Udon", "Bar-B-Q Short Ribs", "Pizza", "Shrimp Tempura Roll", "Chocolate Chip Cookie", "Pesto Pasta Salad", "Fried Chicken", "Burger", "Peanut Butter Cup"  ]

print("FOODS IN ORDER OF PREFERENCE")
print()
for i in range(len(favorite_foods)):
    print(str(i + 1) +" "+ favorite_foods[i])

alphabetical = favorite_foods
alphabetical.sort()
print()
print("FOODS IN ALPHABETICAL ORDER")
print()

for food in alphabetical:
    print("- " + food)
    
