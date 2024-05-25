# How to determine the grade?
# A is 90% or greater (A>=90)
# B is 80% or greater (B>=80)
# C is 70% or greater (C>=70)
# D is 60% or greater (D>=60)
# F is below than 60% (F<60)
# At least 70% to pass a class



percentage = input("What's your grade percentage? ")

if float(percentage) >= 70:
    if float(percentage) >= 90:
        letter = "A"
    elif float(percentage) >= 80:
        letter = "B"
    elif float(percentage) >= 70:
        letter = "C"
    passed = True
else:
    if float(percentage) >= 60:
        letter = "D"
    else:
        letter = "F"
    passed = False

if (float(percentage) % 10) >= 7 and letter in("B", "C", "D"):
    sign = "+"
elif (float(percentage) % 10) < 3 and letter in("B", "C", "D"):
    sign = "-"
else:
    sign = ""

if passed:
    print(f"Congratulations! You passed with a grade of {letter}{sign}!")
else:
    print(f"You failed the course with a grade of {letter}{sign}. Better luck next time!")