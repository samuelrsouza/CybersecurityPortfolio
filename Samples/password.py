import string

password = "he12dasdasdasdasdasdASA3lloasdasdW!ord"

length = len(password)
characters = [0, 0, 0, 0]  # [upper_case, lower_case, special, digits]

for c in password:
    if c in string.ascii_uppercase:
        characters[0] = 1
    elif c in string.ascii_lowercase:
        characters[1] = 1
    elif c in string.punctuation:
        characters[2] = 1
    elif c in string.digits:
        characters[3] = 1

with open('Source/most-common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in the common list.\nScore: 0 / 7")
    exit()

score = 0

if length > 5:
    score += 1
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 16:
    score += 1

print(characters)

print(f"Password length is {length}, adding {score} points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"Password has {sum(characters)} different character types! Adding {sum(characters) - 1} points!")

if score < 4:
    print(f"Password weak - score = {score}")
elif score == 4:
    print(f"Password is ok - score = {score}")
elif 4 <= score < 6:
    print(f"Password is decent - score = {score}")
else:
    print(f"Password is strong - score = {score}")
