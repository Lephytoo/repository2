prompt = "Hello customer, what would you like?"
prompt += "\nThis is what we have: Food, Drinks or Books. Type 'done' when you are finished! \n"

while True:
    answer = input(prompt)
    if answer.lower() == 'Food':
        print("That sounds great! I will take you to the Food menu.")
    elif answer.lower() == 'Drinks':
        print("That sounds great! I will take you to the Drinks menu")
    elif answer.lower() == 'Books':
        print("That sounds great! I will take you to the Books menu")
    elif answer.lower() == 'done':
        break
    else:
        print("Sorry! We do not have that.")

