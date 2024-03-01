dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."
elif dog == "thirsty":
    owner = "Refilling water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "Snuggling."
else:
    owner = "Reading newspaper."


print(owner)
def control_flow(value):
    if value:
        print("Yep!")
    else:
        print("nope!")
control_flow(None)
control_flow(0)

age = 8
if age < 2:
  is_baby = 'baby'
elif age <= 10:
  is_baby = 'a toddler'
elif age < 23:
    is_baby = 'an teenager'
else:
    is_baby= 'an adult'
print(is_baby)
