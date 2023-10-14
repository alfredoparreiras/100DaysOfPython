line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
chars = list(position)
x = None
y = None

if(len(chars) > 0):
    if chars[0].upper() == "A":
        x = 0
    elif chars[0].upper() == "B":
        x = 1
    elif chars[0].upper() == "C":
        x = 2
    else:
        print("X axis has a Problem")

if chars[1] == "1":
    line1[x] = "X"
elif chars[1] == "2":
    line2[x] = "X"
elif chars[1] == "3":
    line3[x] = "X"
else:
    print("Y axis has a Problem")

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")