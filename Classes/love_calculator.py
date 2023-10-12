#
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."
#

# Requirement
# We should calculate how many times the letters from "TRUE LOVE" appears in both names. Based on that we should concat
# this two grades to get a final score.

#Getting Data from User.
print("### Welcome to Love Calculator ###")
first_name = input("Enter the first name : ")
second_name = input("Enter the second name : ")

#Calculating the Amount of occurences each letter has and total score.
combined_name = first_name.strip().lower() + second_name.strip().lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
first_score = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
second_score = l + o + v + e

total_score = str(first_score) + str(second_score)

# Displaying Result by the scored earned.
if int(total_score) < 10 or int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif int(total_score) > 40 and int(total_score) < 50:
    print(f"Your score is {total_score}, you're alright together.")
else:
    print(f"Your score is {total_score}.")

# Testing =
# Brad Pitt	Jennifer Aniston -> Output 73
# Angela Yu	Jack Bauer	-> Output 53
# Kanye West Kim Kardashian -> Output 42