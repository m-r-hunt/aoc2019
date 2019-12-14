import math
from collections import defaultdict

def run():
    reactions = {}
    with open("d14input.txt", "r") as file:
        text = file.read()
        lines = text.split("\n")
        for line in lines:
            parts = line.split(" => ")
            if len(parts) < 2:
                continue
            product = parts[1]
            product_parts = product.split(" ")
            inputs = []
            for ip in parts[0].split(", "):
                pp = ip.split(" ")
                inputs.append((int(pp[0]), pp[1]))
            reactions[(product_parts[1])] = (int(product_parts[0]), inputs)

    def try_making(oreamount_made):
        needs = {"FUEL": oreamount_made}
        spare = defaultdict(int)
        while len(needs) > 1 or not "ORE" in needs:
            type = ""
            for t in needs:
                if t == "ORE":
                    continue
                type = t
                break
            quantity = needs[type]
            amount_made, inputs = reactions[type]
            times_to_run = math.ceil(quantity / amount_made)
            spare[type] += times_to_run * amount_made - quantity
            for iquantity, itype in inputs:
                aquantity = iquantity * times_to_run
                spare_used = min(aquantity, spare[itype])
                aquantity -= spare_used
                spare[itype] -= spare_used
                if aquantity > 0:
                    if itype in needs:
                        needs[itype] += aquantity
                    else:
                        needs[itype] = aquantity
            del needs[type]
            #print("Running", reactions[type],"this many times:", times_to_run)
            #print(needs, spare)
        return needs["ORE"]
    print(try_making(1))

    # Fairly crude search strategy formulated via trial and error.
    # There must be a better way to do this?
    oreamount_made = 1
    while True:
        oreamount_made *= 2
        cost = try_making(oreamount_made)
        if cost >= 1000000000000:
            break
    while True:
        oreamount_made -= 100000
        cost = try_making(oreamount_made)
        if cost <= 1000000000000:
            break
    while True:
        oreamount_made += 1
        cost = try_making(oreamount_made)
        if cost >= 1000000000000:
            break
    print(oreamount_made-1)


run()
