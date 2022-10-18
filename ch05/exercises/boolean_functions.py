

def percentage_to_letter(score = 0):
    if score >= 90:
        lettergrade = "A"
    elif 90 > score >= 80:
        lettergrade = "B"
    elif 80 > score >= 70:
        lettergrade = "C"
    elif 70 > score >= 60:
        lettergrade = "D"
    elif 60 > score:
        lettergrade = "F"
    return lettergrade

def is_passing(letter = None):
    if letter == "A":
        return True
    elif letter == "B":
        return True
    elif letter == "C":
        return True
    elif letter == "D" or "F":
        return False
grade_input = float(input("Input your grade: "))
converted_grade = percentage_to_letter(grade_input)
converted_grade = str(converted_grade)
print("Letter grade:",converted_grade)
print("T/F value of is_passing() function:",is_passing(converted_grade))

if is_passing(converted_grade) == False:
    print("Fail")
else:
    print("Pass")