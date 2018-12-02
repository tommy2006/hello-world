print "Enter your first word."
a = raw_input()
print "Enter your second word."
b = raw_input()
if a<b:
    print a,"comes before",b,"and",b,"comes before",a,"."
elif a>b:
    print a,"comes after",b,"and",b,"comes before",a,"."
