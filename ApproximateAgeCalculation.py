# EN: This program calculates the approximate age of the user based on their year of birth.
# FA: In barname sen taghribye karbar ra bar asas sal tavaod an mohasebe mikonad.

from datetime import datetime

print("Welcome.\n\n")

# EN: Recieving the first name of user; This phase will be repeated if they don't enter anything as their name.
# FA: Daryaft nam kuchak karbar; In bakhsh agar karbar chizi be onvan esm khod vared nakonad tekrar mishavad.
Name = ""
while Name == "":
    Name = input("Please enter your first name: ")
    if Name == "":
        print("\nError.\nYou must enter your name.\n")

# EN: Letting the user to choose their birth year from Georgian and Solar calendar; This phase will be repeated until the user enters the right value (1 ya 2), this will prevent unintended behaviors and bugs.
# FA: Ejaze dadan be karbar baraye entekhab sal tavalod khod bein taghvim Miladi va Shamsi; In kar ta zamani tekrar mishavad ke karbar meghdar dorost (1 ya 2) ra vared konad, In baes pishgiri az raftar nakhaste va moshkelat mishavad.
Check = 0
while Check < 1 or Check > 2:
    Check = int(input("\nEnter one of these codes below:\n1. AD/CE (International and western calendar).\n2. Solar year (Iranian calendar).\n\nEnter: "))
    if Check < 1 or Check > 2:
        print("\nError.\nYou can only choose between 1 and 2.")

Birth_Year = 0
# EN: Recieving the year of birth of the user based on Georgian calendar (if the user have entered 1 in the last phase).
# FA: Daryaft sal tavalod karbar bar asas taghvim Miladi (agar karbar dar bakhsh ghavli 1 ra vared karde bashad).
if Check == 1:

    Current_Year = datetime.now().year
    
    # EN: This phase will be repeated if they input and invalid year; For example, if they input 0 or a year higher than the current year.
    # FA: In bakhsh agar karbar meghdad na motabar vared konad tekrar mishavad; Baraye mesal, agar karbar 0 ya sali bishtar az sal konuni vared konad.
    while Birth_Year < 1 or Birth_Year > Current_Year:
        Birth_Year = int(input("\nPlease enter the year of your birth: "))
        if Birth_Year < 1 or Birth_Year > Current_Year:
            print("\nError.\nThe inputed value is invalid.")

# EN: Recieving the year of birth of the user based on Solar calendar (if the user have entered 2 in the last phase).
# FA: Daryaft sal tavalod karbar bar asas taghvim Shamsi (agar karbar dar bakhsh ghavli 2 ra vared karde bashad).
else:

    # EN: Calculating the Solar year by subtracting the current Georgian year by 621.
    # FA: Mohasebeye sal Shamsi ba tafrigh sal Miladi konuni az 621.
    Current_Year = datetime.now().year - 621

    # EN: This phase will be repeated if they input and invalid year; For example, if they input 0 or a year higher than the current year.
    # FA: In bakhsh agar karbar meghdad na motabar vared konad tekrar mishavad; Baraye mesal, agar karbar 0 ya sali bishtar az sal konuni vared konad.
    while Birth_Year < 1 or Birth_Year > Current_Year:
        Birth_Year = int(input("\nPlease enter the year of your birth: "))
        if Birth_Year < 1 or Birth_Year > Current_Year:
            print("\nError.\nThe inputed value is invalid.")

# EN: Dispaying the approximate age of the user.
# FA: Namayesh sen taghribi karbar.
Age = Current_Year - Birth_Year
print(f"\nHey {Name}, You are approximately {Age - 1} to {Age} years old.")

# EN: End of program.
# FA: Payan barname.
print("\n\nProgram is over.")