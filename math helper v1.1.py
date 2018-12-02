print ("I can help you with some math. I am the IntelCalculator v1.1. I have been modified to run on Python 3.6.1.")
print ("What do you want me to do?")
g = raw_input()
if g == ("Calculate the area of a shape."):
                 print ("Enter the shape you want to calculate") # Confirming which shape user wants to be calculated
                 a = raw_input()
                 if a == ("triangle"):
                         print ("Enter the bottom length of the triangle")
                         b = float(raw_input())
                         print ("Enter the height of the triangle")
                         c = float(raw_input())
                         d = b*c/2
                         print ("The triangle's area is",x,"squared units.")
                 elif a == ("rectangle"):
                         print ("Enter the length of the rectangle")
                         e = float(raw_input())
                         print ("Enter the width of the rectangle")
                         f = float(raw_input())
                         class Rectangle():
                             def __init__(self,y,z):
                                 self.length = y
                                 self.breadth = z
                             def getArea(self):
                                 return self.length*self.breadth
                         a = Rectangle(e,f) 
                         if e == f:
                                 print ("That looks more like a square. Uh-oh.")
                         if e>f:
                                 print ("That should be the length of the rectangle.")
                         print ("The area of the rectangle is",a.getArea(),"squared units.")
                 elif a == ("square"):
                         print ("Enter the side length of the square")
                         h = float(raw_input())
                         i = h*h
                         print ("The area of the square is",f,"squared units.")
elif g == ("Calculate the percentage of one number to another."):
                 print ("Enter your first number")
                 j = float(raw_input())
                 print ("Enter your second number")
                 k = float(raw_input())
                 percentage = j/k*100
                 print ("The percentage of",h,"to",i,"is",percentage,"%.")
elif g == ("Check divisibility of x to y"):
                 print ("Enter your first number.")
                 l = float(raw_input())
                 print ("Enter your second number.")
                 m = float(raw_input())
                 def checkdiv(x,y):
                                if x>=y:
                                        if x%y == 0:
                                                print (x,"is divisible by",y)
                                        else:
                                                print (x,"is not divisible by",y)
                                else:
                                        print ("Your first number should be greater than the second. Restart me and try again.")
                 checkdiv(l,m)
elif g == ("Calculate perimeters of shapes"):
    print ("Which shape do you want to calculate?")
    n = raw_input()
    if n == ("square"):
        print ("Enter the side length of the square")
        o = float(raw_input())
        class Square():
            def perimeter(self,side):
               return side*4
        p = Square()
        print ("The square's perimeter is",p.perimeter(o),"units.")
    elif n == ("rectangle"):
        print ("Enter the length of the rectangle")
        q = float(raw_input())
        print ("Enter the breadth of the rectangle")
        r = float(raw_input())
        class Rectangle():
             def __init__(self,y,z):
                 self.length = y
                 self.breadth = z
             def getPerimeter(self):
                  return 2*(self.length+self.breadth)
        a = Rectangle(q,r)
        print ("The perimeter of the rectangle is",a.getPerimeter(),"units.")
    elif n == ("pentagon"):
        print ("Enter the side length of the pentagon")
        s = float(raw_input())
        perimeter = s*5
        print ("The perimeter of the pentagon is",perimeter,"units.")
elif g == ("Converting units"):
    print ("What type of measurenent units do you want to convert? (Volume, Weight, Length,...)")
    measurementType = raw_input()#If I transfer this program to Python 3, change raw_input() into input()
    if measurementType == ("Volume"):
        print ("Enter your first unit")
        unit1 = raw_input()
        print ("How many units of that measurement unit do you want to convert?")
        num1 = float(raw_input())
        print ("Enter your second unit")
        unit2 = raw_input()
        if unit1 == "ml" and unit2 == "cl":
            total = num1*0.1
            print (num1,unit1,"(either singular or plural) equals",total,unit2,"(singular or plural again).")
                



