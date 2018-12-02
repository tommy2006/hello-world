print "How many test scores do you have?"
a = input()
if a == 2:
    print "Enter your first score."
    b = float(raw_input())
    print "Enter your second score."
    c = float(raw_input())
    marks = [b,c]
    sum = 0
    for m in marks:
        sum = sum+m
        GPA = sum/2
    print "Your GPA is",GPA,"marks."
if a == 3:
    print "Enter your first score."
    d = float(raw_input())
    print "Enter your second score."
    e = float(raw_input())
    print "Enter your third score."
    f = float(raw_input())
    marks = [d,e,f]
    sum = 0
    for m in marks:
        sum = sum+m
        GPA = sum/3
    print "Your GPA is",GPA,"marks."
if a == 4:
    print "Enter your first score."
    g = float(raw_input())
    print "Enter your second score."
    h = float(raw_input())
    print "Enter your third score."
    i = float(raw_input())
    print "Enter your fourth score."
    j = float(raw_input())
    marks = [g,h,i,j]
    sum = 0
    for m in marks:
        sum = sum+m
        GPA = sum/4
    print "Your GPA is",GPA,"marks."
if a == 5:
    print "Enter your first score."
    k = float(raw_input())
    print "Enter your second score."
    l = float(raw_input())
    print "Enter your third score."
    m = float(raw_input())
    print "Enter your fourth score."
    n = float(raw_input())
    print "Enter your fifth score."
    o = float(raw_input())
    marks = [k,l,m,n,o]
    sum = 0
    for m in marks:
        sum = sum+m
        GPA = sum/5
    print "Your GPA is",GPA,"marks."
