today = 2021
reqTime = 0
age = 0
while (True):
    ageOrYob = int(input("Enter your age or year of birth"))

    if ageOrYob < 150 and ageOrYob > 0:
        reqTime = 100 - ageOrYob
        print(f"You will be 100 years old in year {today + reqTime} or we can say in {reqTime} years")
        break
    elif ageOrYob > 150 and ageOrYob <= 2021:
        age = today - ageOrYob
        reqTime = 100 - age
        print(f"You will be 100 years old in year {today + reqTime} or we can say in {reqTime} years")
        break
    else:
        print("Wrong age or year of birth entered")
        continue
