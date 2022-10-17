


def percentage_to_letter(score = 0):
        if score >= 90:
            lettergrade = str("A")
        elif 90 > score >= 80:
            lettergrade = str("B")
        elif 80 > score >= 70:
            lettergrade = str("C")
        elif 70 > score >= 60:
            lettergrade = str("D")
        elif 60 > score:
            lettergrade = str("F")
        return lettergrade
#why the heck am i using a list? idk
def is_passing(grade_convert):
    passgrade = ["A","B","C"]
    failgrade = ["D","F"]
    if grade_to_convert_to_passfail == passgrade[0] or passgrade[1] or passgrade[2]:
        result = str("Pass")
    if grade_to_convert_to_passfail == failgrade[0] or passgrade[1]:
        result = str("Fail")
    return result
grade_input = float(input("Input your grade: "))
        
grade_to_convert_to_passfail = percentage_to_letter(grade_input)
final_result = is_passing(grade_to_convert_to_passfail)

print(grade_to_convert_to_passfail)
print(final_result)