

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
    print(lettergrade)
    return str(lettergrade)

def is_passing(letter = None):
    if letter == "A" or "B" or "C":
        final_result = True
    else:
        final_result = False
    print(final_result)
    return final_result


grade_input = float(input("Input your grade: "))
converted_grade = percentage_to_letter(grade_input)
print("Letter grade:",converted_grade)

if is_passing(converted_grade) == True:
    print("Pass")
elif is_passing(converted_grade) == False:
    print("Fail")