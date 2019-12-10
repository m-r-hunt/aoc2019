import intcode

def run():
    init_memory = intcode.parse_input_to_memory("d9input.txt")
    ic = intcode.Intcode(init_memory)
    ic.set_input([1])
    ic.run_program()
    print(ic.output)

    ic = intcode.Intcode(init_memory)
    ic.set_input([2])
    ic.run_program()
    print(ic.output)

run()
