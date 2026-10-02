print(r'''
THOMAS, the Hunter!
*******************************************************************************
    _                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',     fsc/as
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/
*******************************************************************************
''')
print("Welcome to Thomas, Cat Hunter.")
print("You are a Cat named Thomas, a small, deadly Cat-Assassin"
      "You greatly desire to hunt and kill neighborhood chipmunks near your home.")

direction_choice = input('You head out the back door of your house. \n'
                         'Where do you want to go?'
                         'Type left or right or straight.\n').lower()

if direction_choice == "straight":
    direction2 = input('Uhhh, that is a really busy road. You get hit by a car! Game Over.')

elif direction_choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake_choice = input('\t Type "wait" to wait for a boat. '
                        'Type swim to swim across.\n').lower()
    if lake_choice == "wait":
        print("You arrive at the island unharmed. "
              "There is a house with 3 doors")
        door_choice = input('\t One door is red, one is yellow and one is blue. '
                            'Which color door to you choose \n').lower()
        if door_choice == "red":
            print("It's a room full of fire. Game Over.")
        elif door_choice == "blue":
            print("You enter a room full of beasts. Game Over.")
        elif door_choice == "yellow":
            print("You found the chipmunk! Yay, You Win. Now rip it's little head off.")
        else:
            print("Wrong door choice - that door doesn't exist.  Game Over.")
    else:
        print("You are attacked by Killer Trout. Game Over.")
else:
    print("You fell in a hole. Game Over.")