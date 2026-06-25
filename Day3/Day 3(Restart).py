# Conditions Statements
#Logical Ops

print("Privet Welcome to The Last Ride")                # if/else conditions
height = int(input("Enter Your Height(in cm):"))
bill = 0

if height > 120 :
    print("Congrats You Can Ride The Rollercoster")
    age = int(input("Tell Me How Old Yor Are ?"))
    # Nested if/else statements
    if age < 12:
        bill = 5
        print("Kids  Tickets are $5")
    elif age >= 45 and age <= 55:
        print("You Can Enjoy the last ride for free")
    elif age <= 18:
        bill = 7
        print("Youth Tickets $7")
    else:
         bill = 12
         print("You Need to Pay $12 For a ticket ")

    wants_photo = input("Do You Want Photo Y or N")
    if wants_photo == "Y" :
      bill += 3
      print(f"Your Final bill is {bill}")
else:
    print("Ops You Need To Grow Taller")





