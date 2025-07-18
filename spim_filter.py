p1="HEY this is saleh"
p2="make alot of money"
p3="for more information call me"

msg=input("Enter a msg : ")
if((p1 in msg) or (p2 in msg) or (p3 in msg)):
    print("This is spam!")
else:
    print("Not a spam")