print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/__q____/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("WELCOME TO TREASURE ISLAND")
direction = input("Where the winding road meets its end, a fork in the path does lay. \nTo the LEFT or the RIGHT,"
      " which will be your way?")

if(direction.lower() == "left"):
    swin = input("The path leftward leads you to a river, tranquil as a painter's still life.\n"
                 "Shall you embrace adventure and SWIM, or choose WAIT and patience and watch the water's drift?")
    if(swin.lower() == "wait"):
        door = input("Choosing patience, you sit by the river's bank, letting the calm water's symphony sooth your spirit. "
                     "\nAs time passes, the river surrenders its secret - three mystical doors materialise, each a beacon with its own hue: "
                     "\none BLUE as the deepest ocean, "
                     "\nanother RED as fiery passion, "
                     "\nand the last YELLOW, luminous as the sun. "
                     "\nEach door stands tall, an invitation to an unknown destiny within your adventurous tale.")
        if(door.lower() == "yellow"):
            print("As you open the yellow door, victory instantly unfolds before you. A cascade of golden light celebrates your triumph. "
                  "\nCongratulations, adventurer! Your wise choices have crowned you the champion of this game. Well done!")
        elif(door.lower() == "red"):
            print("The red door, alluring and mysterious, was your choice. Yet as it swung open, a rush of intense heat met you. "
                  "\nA fierce flame roared, consuming all in its path. "
                  "\nYour adventure, regrettably, ended here in the fiery grasp of the red door’s gamble. "
                  "\nIt's a dreadful game over.")
        else:
            print("Drawn to the blue door's depths, you stepped through, unknowing of your impending fate. "
                  "\nInstantly, shadowy beasts lunged from the unseen, their presence an unforeseen terror. "
                  "\nTragically, your adventure concludes under their fierce assault. "
                  "\nThe game, alas, is over.")
    else:
        print("Embracing boldness, you plunge into the river to swim, only to find the tranquility deceiving.\n"
              "A fierce trout, guardian of these waters, makes its presence known, "
              "ending your adventure in a surprising and swift underwater encounter.\n"
              "GAME OVER")

else:
    print("Ah, the twist of fate! Veering to the right, you stumble and fall into the pit, thus marking the end of your"
          " journey. \nAn unexpected turn in this adventure game. Alas, it's game over.\nGAME OVER")