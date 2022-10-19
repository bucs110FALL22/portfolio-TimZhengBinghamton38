

"""
This function multiplies a given number by another given number and outputs the result (limited to positive integers)
args:
    num (default is 0)
    multi_amount (default is 0)
return: multiplied number
"""
def multiply(num = 0,multi_amount = 0):
    original_num = num
    for _ in range(multi_amount-1):
        num += original_num
    return num

"""
This raises a given number to a given power
args:
    num (default is 0)
    multi_amount (default is 0)
return: number raised to a power
"""
def exponent(num = 0, power = 0):
    powernum = 1
    for _ in range(power):
        powernum = multiply(powernum, num)
    return powernum

"""
This squares a number
args: 
    num (default is 0)
return: squared number
"""
def square(num = 0):
    return exponent(num,2)


def main():
    num1 = int(input("Input the first number to multiply: "))
    num2 = int(input("Input the second number to multiply: "))
    print(multiply(num1,num2))
    num_power_1 = int(input("Input the number to raise: "))
    num_power_2 = int(input("Input the power to raise the number to: "))
    print(exponent(num_power_1,num_power_2))
    square_num = int(input("Input a number to square: "))
    print(square(square_num))
main()