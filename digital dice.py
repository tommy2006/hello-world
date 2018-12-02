from random import randint
print "Give lower limit of dice"
a = input()
print "Give upper limit of dice"
b = input()
print "Type q to quit, or any other key to continue."
while True:
    print ">>> "+str(randint(a,b))
    if raw_input() == 'q':
            break;
