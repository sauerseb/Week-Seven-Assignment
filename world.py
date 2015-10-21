# Framework for Conway's game of life
# Evan Sauers
# CIS-125-82A
# Collaborated with Dr. Neumann

# List of Functions
# populate()
# display()
# generation()
# main()

#Function populate
#Preconditions
#   random is imported
#   world is created as list
#   height is defined (as integer)
#   width is defined (as integer)
#Postcondition
#   world is populated with ?? (string)

# "Populate" code below:

def populate(petri_dish, h=80, w=22):
    import random
    for x in range(h):
            row = []
            for y in range(w):
                    row.append(0)
            petri_dish.append(row)

# "rpopulate" code below:

def rpopulate(petri_dish, h=80, w=22):
    import random
    for x in range(h):
            row = []
            for y in range(w):
                    row.append(random.randint(0, 1))
            petri_dish.append(row)
            
# Function display(world,h,w)
# Preconditions
#   world is populated
# Postcondition
#   world is not changed

# "Display" code below:

def display(world, h = 22, w = 80):
    worldstring = ""
    for x in range(h):
        for y in range(w):
            if world[x][y] == 1:
                worldstring += "*"
            else:
                worldstring += " "
        worldstring += '\n'
    print(worldstring)


# Function generation(world,h,w)
# Preconditions
#   world is populated
# Postconditions
#   Returns new world

# "Generation" code below:

def generation(petri_dish, h=22, w=80):
    new_world = []
    populate(new_world, h, w)
    
    n = 0    
    for x in range(1,h-1):
        for y in range(1,w-1):
            n = petri_dish[x-1][y-1] +  \
                petri_dish[x-1][y] +  \
                petri_dish[x-1][y+1] +  \
                petri_dish[x][y-1] +  \
                petri_dish[x][y+1] +  \
                petri_dish[x+1][y-1] +  \
                petri_dish[x+1][y] +  \
                petri_dish[x+1][y+1]

            
            if petri_dish[x][y] == 0:
                if n == 3:
                    new_world[x][y] = 1
                else:
                    new_world[x][y] = 0
            else: #(the cell is now alive)
                if n < 2 or n > 3:
                    new_world[x][y] = 0
                else:
                    new_world[x][y] = 1
    # Return the new_world to make it the new world as it comes in
    return new_world


def main():
    world = []
    height = 22
    width = 80
    rpopulate(world, height, width)
    display(world, height, width)
    key = input("Press q to quit, any other key to continue: ")
    while key != 'q':
        world = generation(world, height, width)
        display(world, height, width)
        key = input("Press q to quit, any other key to continue: ")

    print("Goodbye!")


if __name__ == '__main__':
    main()
