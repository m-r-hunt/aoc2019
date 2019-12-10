import intcode

def run():
    init_memory = intcode.parse_input_to_memory("d2input.txt")

    ic = intcode.Intcode(init_memory)
    ic.set_noun_verb(12, 2)
    print(ic.run_program())

    for input1 in range(100):
        for input2 in range(100):
            ic = intcode.Intcode(init_memory)
            ic.set_noun_verb(input1, input2)
            output = ic.run_program()
            if output == 19690720:
                print(100*input1 + input2)
                return
            input2 += 1
        input1 += 1

run()
