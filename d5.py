import intcode

def run():
    init_memory = intcode.parse_input_to_memory("d5input.txt")

    ic1 = intcode.Intcode(init_memory)
    ic1.set_input([1])
    ic1.run_program()
    print(ic1.output)

    ic2 = intcode.Intcode(init_memory)
    ic2.set_input([5])
    ic2.run_program()
    print(ic2.output)

run()
