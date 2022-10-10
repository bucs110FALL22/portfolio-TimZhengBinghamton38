
#the reason for layernumber + 1 is to ensure the amount of layers is correct in terms of humans
def star_pyramid():
    layernumber = int(input("Input the number of layers the pyramid has: "))
    pyramidmaterial = str("*")

    for i in range(1, layernumber + 1):
        print(pyramidmaterial*i)

star_pyramid()

def rstar_pyramid():
    layernumber = int(input("Input hte number of layers the inverted pyramid has: "))
    pyramidmaterial = str("*")

    layerorder = range(1, layernumber + 1)
    layerorder = layerorder.__reversed__()
    for i in layerorder:
        print(pyramidmaterial*i)

rstar_pyramid()
    