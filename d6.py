def run():
    orbits = {}
    with open("d6input.txt", "r") as file:
        text = file.read()
        for line in text.split("\n"):
            parts = line.split(")")
            if len(parts) >= 2:
                orbits[parts[1]] = parts[0]

    #print(orbits)
    counts = {"COM": 0}
    total = 0
    def count_orbits(body):
        if body in counts:
            return counts[body]
        else:
            count = count_orbits(orbits[body])+1
            counts[body] = count
            return count
        # Dumb bruteforce method works fine...
        #if body == "COM":
        #    return 0
        #else:
        #    return 1 + count_orbits(orbits[body])
    for body in orbits:
        total += count_orbits(body)
    print(total)

    you_orbit_chain = [orbits["YOU"]]
    val = orbits["YOU"]
    while val != "COM":
        you_orbit_chain.append(orbits[val])
        val = orbits[val]
    san_orbit_chain = [orbits["SAN"]]
    val = orbits["SAN"]
    while val != "COM":
        san_orbit_chain.append(orbits[val])
        val = orbits[val]
    common_body = None
    transfers = 0
    for body in you_orbit_chain:
        if body in san_orbit_chain:
            common_body = body
            break
        transfers += 1
    print(common_body)
    for body in san_orbit_chain:
        if body == common_body:
            break
        transfers += 1
    print(transfers)
    # Smarter way (but also likely to get it wrong at least once)
    print(counts[orbits["YOU"]] + counts[orbits["SAN"]] - 2*counts[common_body])

run()
