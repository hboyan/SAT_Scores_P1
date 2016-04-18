#__author__ = 'Haley Boyan'

#Write a function with one argument. Find the area of a square.
def areasq(w):
    area = w*w
    print("The area of your square is "+str(area)+" square inches.")

#Write a function with two arguments. Find the area of a rectangle.
def arearect(w,h):
    area = w*h
    print("The area of your rectangle is "+str(area)+" square inches.")

#Write a function with three arguments. Find the surface area of cuboid.
def areacub(w,h,d):
    area = 2*((w*h)+(w*d)+(h*d))
    print("The surface area of your cuboid is "+str(area)+" square inches.")

#This function allows the user to choose their shape, input the size, and run the appropriate calculations.
def choice():
    choice=str(raw_input("What shape do you have? (s = square, r = rectangle, c = cuboid, q = quit)"))
    #unless the user quits, we move forward
    while choice!='q':
        try:
            #check if the choice is one of the shapes we can work with:
            if choice in "src":

                #All good? Get the width, since all the shapes have that. Also, make sure it's a positive number.
                w = float(raw_input("How many inches wide is it? "))
                while w<=0:
                    w = float(raw_input("Sorry, we can only use positive numbers. Try again. How wide is it? "))
                #if it's a square, that's all we need, so run the calculations.
                if choice=='s':
                    areasq(w)

                #if it's not a square (but was a valid shape) we need to keep going. Both of the other shapes have height.
                else:
                    h = float(raw_input("How many inches tall is it? "))
                    while h<=0:
                        h = float(raw_input("Sorry, we can only use positive numbers. Try again. How tall is it? "))

                    #if it's a rectangle, we have what we need.
                    if choice == 'r':
                        arearect(w,h)

                    #if it wasn't a square or a rectangle, it must have been a cuboid. Let's get the depth and calculate the area.
                    else:
                        d=float(raw_input("How many inches deep is it? "))
                        while d<=0:
                            d = float(raw_input("Sorry, we can only use positive numbers. Try again. How deep is it? "))
                        areacub(w,h,d)

            #if they didn't choose a valid shape to begin with, we need to give them another chance.
            else:
                print("That's not a valid choice, please try again. ")
            choice=str(raw_input("What shape do you have? (s = square, r = rectangle, c = cuboid, q = quit)"))

        #a common problem would be if they didn't enter a number to do the calculations. We should prepare to handle that error.
        except ValueError:
            print("Oh no! That's not a valid number. Let's try again.")
            choice=str(raw_input("What shape do you have? (s = square, r = rectangle, c = cuboid, q = quit)"))

choice()
