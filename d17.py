import intcode

def run():
    memory = intcode.parse_input_to_memory("d17input.txt")
    memory[0] = 2
    #memory[191] = 9999
    memory[1047] = 9999
    memory[1164] = 9999
    ic = intcode.Intcode(memory)
    ic.input = [ord(c) for c in "A\nL,6,R,12,L,6,R,12,L,10,L,4,L,6,L,6,R,12,L,6,R,12,L,10,L,4,L,6,L,6,R,12,L,6,L,10,L,10,L,4,L,6,R,12,L,10,L,4,L,6,L,10,L,10,L,4,L,6,L,6,R,12,L,6,L,10,L,10,L,4,L,6,L,6,R,12,L,10,L,4\nL,10,L,4,L,6\nL,6,L,10\ny\n"]
    img = ""
    while not ic.is_halted():
        ic.run_to_output()
        if ic.output == ord("\n"):
            print(img)
            #input()
            img = ""
        else:
            img += chr(ic.output)
    print(ic.output)
    ic.f.close()

run()
