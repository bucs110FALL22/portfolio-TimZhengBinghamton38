myvalues = [10*5,10**2,15/10,15//10,-15//10,15%10,10%15,10%10,0%10,10/15]
print(myvalues)

# last answer does not properly indicate that 2/3 in decimal is 0.6 repeating unto infinity

rate = input("Current Exchange Rate of USD to Euros: ")
amount = input("Amount to Exchange: ")

rate = float(rate)
amount = float(amount)
total = amount*rate
result = total - 3.00
print(result)