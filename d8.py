import math

def countn(s, n):
    count = 0
    for c in s:
        if c == n:
            count += 1
    return count


def zeroes(s):
    return countn(s, "0")

def run():
    data = ""
    with open("d8input.txt", "r") as file:
        text = file.read()
        data = text.split("\n")[0]
    width = 25
    height = 6
    size = width*height
    layers = [data[n*size:(n+1)*size] for n in range(0, math.floor(len(data) / size))]
    sorted_layers = sorted(layers, key=zeroes)
    print(countn(sorted_layers[0], "1") * countn(sorted_layers[0], "2"))

    message = ""
    for y in range(height):
        for x in range(width):
            n = y*width + x
            px = ""
            for layer in layers:
                if layer[n] == "2":
                    continue
                px = "#" if layer[n] == "1" else " "
                break
            message += px
    for y in range(height):
        print(message[y*width:(y+1)*width])


run()
