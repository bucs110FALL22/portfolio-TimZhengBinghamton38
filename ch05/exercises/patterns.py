
#the reason for layernumber + 1 is to ensure the amount of layers is correct in terms of humans
layernumber = int(input("Input the number of layers the pyramid has: "))

def star_pyramid():
    pyramidmaterial = str("*")

    for i in range(1, layernumber + 1):
        print(pyramidmaterial*i)

def rstar_pyramid():
    pyramidmaterial = str("*")

    layerorder = range(1, layernumber + 1)
    layerorder = layerorder.__reversed__()
    for i in layerorder:
        print(pyramidmaterial*i)

star_pyramid()
rstar_pyramid()
    