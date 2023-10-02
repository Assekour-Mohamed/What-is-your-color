x = int(input("enter x coordinate"))
y = int(input("enter x coordinate"))
if (x < 0 or x > 90) or (y < 0 or y > 70):
    color = "out of the schema"
elif (x > 10 and x < 85) and (y > 10 and y < 55):
    if (x > 25 and x < 50) and (y > 20 and y < 45):
        color = "Yellow"
    else:
        color = "Blue"
elif y > 60:
    if (x > 15 and x < 45) or (x > 60 and x < 85):
        color = "Red"
else:
    color = "Yellow"

print("you are in the color ", color)
