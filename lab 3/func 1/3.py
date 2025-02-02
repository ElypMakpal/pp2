def solve(numheads, numlegs):
    for rabbits in range(numheads+1):
        chickens=numheads-rabbits
        if 2*chickens+4*rabbits==numlegs:
            print("chickens:",chickens, "  " ,"rabbits:" ,rabbits)
solve(35,94)
