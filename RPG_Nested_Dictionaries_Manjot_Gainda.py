#2D_Arrays_&_Nested_Dictionaries_Manjot_Gainda
#Nov. 21st, 2025
#This program makes use of arrays and nested arrays to create descriptions for characters, items
#and locations to be used in a python text-based game.
    
Characters = {                                     #A dictionary containing the two main characters                                                                     
    "Dan": {
        "Relationship": "Bobby's friend",          #Gives a brief description of the character
        "Fun Facts": "believes in ghosts",
        "Strength": "100"
        },
    "Bobby": {                                     #Next character
        "Relationship": "the main character",      #Gives a brief description of the character
        "Fun Facts": "gets scared easily",
        "Strength": "90"
        }
    }

print("\n")
for character in Characters:             #Loops through characters in the character dictionary
    data = Characters[character]         #Sets a variable to handle each individual character dictionary
    if int(data["Strength"]) >= 100:     #If a characters strentgh is greater than 100, they are given
        Strength = "pretty strong"       #a special attribute, otherwise they are labeled as weak
    else:
        Strength = "kind of weak"
        
    print (character, "is", data["Relationship"])  #Prints characters importance to the story
    print(character, data["Fun Facts"])            #Prints any interesting facts about the character                       
    print(character,"is ", Strength, "With a strength of", data["Strength"]) #Prints characters strength
    print("")

Locations = {    #A dictionary that contains the 3 main locations in the game
    "Auditorium": {
        "Exits": "1 exit",                        #Amount of exits at location
        "Danger Level": "low danger level",       #How dangerous the location is
        "Monster": "The Shrieking Conductor"      #The monster that haunts the location
        },
    "Basement": {                                 #Next location
        "Exits": "4 exits",
        "Danger Level": "medium danger level",
        "Monster": "The Sweeping Specter"
        },
    "Main Floor": {                               #Next location
        "Exits": "0 exits",
        "Danger Level": "high danger level",
        "Monster": "The Painless Panko"
        }
    }

Tiles = {
    "Blank Tile": {                                #Tile name
        "Info": "there is nothing here...",        #Tile info
        "Choice": "rest or move somewhere else"    #Available choices
        },
    "Boss Tile": {                                 #Next tile
        "Info": "there is a monster who just spotted you!",
        "Choice": "fight the monster, or run away"
        },
    "Ghost Tile": {                                   #Next tile
        "Info": "a ghost is on the same tile as you!",
        "Choice": "fight the ghost, run away, or attempt to communicate"
        },
    "Health Tile": {                                  #Next tile
        "Info": "there is a health pack right below your feet!",
        "Choice": "use the health pack or store it for later"
        }
    
    }

for tile in Tiles:            #Loops through all tiles in the Tile dictionary
    data = Tiles[tile]        #Sets a variable to handle each individual tile in the dictionary
    print("You are on a", tile, "and", data["Info"],
          "you may", data["Choice"])         #prints tile description
print("")

for place in Locations:                            #Loops through the locations dictionary
    data = Locations[place]                        #Sets a variable to handle each individual place in a location
    print ("The", place, "has", data["Exits"])     #Prints the amount of exits    
    print ("with a", data["Danger Level"])         #Prints the danger level
    print ("and is haunted by", data["Monster"])   #Prints the monster haunting that area
    print("")
                                                  
Inventory = {                         #A dictionary that contains the inventory of the two main characters
    "Dan": {                          #Dan's inventory
        "Camera": {                                            
            "Description": "takes photos",  #Brief description of item                
            "Damage": "0",                  #Amount of damage item does                
            "Uses": "2"                     #Amount of uses until item goes away
            },
        "Holy Water": {               #Next item
            "Description": "scares ghosts away",
            "Damage": "20",
            "Uses": "3"
            }
        },
    "Bobby": {                       #Bobby's inventory
        "Water Bottle": {
            "Description": "quenches thirst but makes noise",
            "Damage": "5",
            "Uses": "5"
            },
        "Sparky Head": {             #Next item
            "Description": "lets you become one with Sparky",
            "Damage": "10",
            "Uses": "2"
            },
        },
    }

for people in Inventory:                  #Loops through each individual character in the inventory dictionary
    print (people + "'s inventory:")      #Prints each characters name before printing their individual inventory
    for items in Inventory[people]:
        data = Inventory[people][items]   #Loops through every item in a characters inventory and prints
        print("The", items, data["Description"], "with", data["Damage"], "damage and", data["Uses"], "uses")
    print("")
