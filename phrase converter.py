import string
print "Enter the word or phrase you want to convert."
a = raw_input()
print "Do you want to capitalize, turn every character into lowercase, or turn every character into uppercase?"
b = raw_input()
if b == "capitalize":
    print string.capitalize(a)
if b == "turn every character into lowercase":
    print string.lowercase(a)
if b == "turn every character into uppercase":
    print string.upper(a)
