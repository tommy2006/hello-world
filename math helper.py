print ("I can help you with some math. I am the IntelCalculator v1.1. I have been modified to run on Python 3.6.1.")
print ("What do you want me to do?")
g = input()
if g == ("Calculate the area of a shape."):
                 print ("Enter the shape you want to calculate") # Confirming which shape user wants to be calculated
                 a = input()
                 if a == ("triangle"):
                         print ("Enter the bottom length of the triangle")
                         b = input()
                         print ("Enter the height of the triangle")
                         c = input()
                         d = b*c/2
                         print ("The triangle's area is",x,"squared units.")
                 elif a == ("rectangle"):
                         print ("Enter the length of the rectangle")
                         e = input()
                         print ("Enter the width of the rectangle")
                         f = input()
                         if e == f:
                                 print ("That looks more like a square. Uh-oh.")
                         if e>f:
                                 print ("That should be the length of the rectangle.")
                         g = e*f
                         print ("The area of the rectangle is",d,"squared units.")
                 elif a == ("square"):
                         print ("Enter the side length of the square")
                         h = input()
                         i = h*h
                         print ("The area of the square is",f,"squared units.")
elif g == ("Calculate the percentage of one number to another."):
                 print ("Enter your first number")
                 j = input()
                 print ("Enter your second number")
                 k = input()
                 percentage = j/k*100
                 print ("The percentage of",h,"to",i,"is",percentage,"%.")
elif g == ("Check divisibility of x to y"):
                 l = input()
                 m = input()
                 def checkdiv(x,y):
                                if x>=y:
                                        if x%y == 0:
                                                print (x,"is divisible by",y)
                                        else:
                                                print (x,"is not divisible by",y)
                                else:
                                        print ("Your first number should be greater than the second. Restart me and try again.")
                 checkdiv(l,m)           
