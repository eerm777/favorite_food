favorite_foods = ["Steak", "Manti", "Loaded fries", "Shashlyk", "Shawerma", "Lagman", "Strawberry Cheescake Milkshake", "Brizol"]

<<<<<<< HEAD
print("FOODS IN ORDER OF PREFERENCE")
print()
for i in range(len(favorite_foods)):
    print(str(i + 1) + " " + favorite_foods[i])

alphabetical = favorite_foods
alphabetical.sort()
print()
print("FOODS IN ALPHABETICAL ORDER")
print()

for food in alphabetical:
    print("- " + food)

print("")

favorite_places = ["Bishkek", "Issyk-kul", "Gym", "Home", "Cyber-Club", "Beach", "Bathroom", "\'School\'"]

print("PLACES IN ORDER OF PREFERENCE")
print()
for i in range(len(favorite_places)):
    print(str(i + 1) + " " + favorite_places[i])

alphabetical_places = favorite_places
alphabetical_places.sort()
print()
print("PLACES IN ALPHABETICAL ORDER")
print()

for place in alphabetical_places:
    print("- " + place)


print("")


favorite_sports = ["Soccer", "Volleyball", "Table Tennis", "Boxing", "Wrestling", "MMA", "Football", "Basketball"]

print("SPORTS IN ORDER OF PREFERENCE")
print()
for i in range(len(favorite_sports)):
    print(str(i + 1) + " " + favorite_sports[i])

alphabetical_sports = favorite_sports
alphabetical_sports.sort()
print()
print("SPORTS IN ALPHABETICAL ORDER")
print()

for sport in alphabetical_sports:
    print("- " + sport)
=======
favorite_foods = ["Chocolate Cake", "Pasta", "Turkey Sandwich",
                  "Pumpkin Pie", "Roast Beef", "Pizza", "Potato Chips",
                  "Popcorn", "Cookies", "Broccoli"]

for i, food in enumerate(favorite_foods):
    print(f"{i+1}. {food}")

sorted_list =favorite_foods
sorted_list.sort()





>>>>>>> 06eba9b7226810794232276f12b540edac4ddfda
