def valid(pw):
    pw = str(pw)
    found = False
    for d in range(5):
        if d > 0 and pw[d-1] == pw[d]:
            continue
        if pw[d] == pw[d+1]:
            extra = False
            for dd in range(d+2, 6):
                if pw[d] == pw[dd]:
                    extra = True
            if not extra:
                found = True
    if not found:
        return False
    for d in range(5):
        if pw[d] > pw[d+1]:
            return False
    return True

def run():
    count = 0
    for pw in range(382345, 843167):
        if valid(pw):
            count += 1
    print(count)

print(valid(123444))
print(valid(111122))
run()
