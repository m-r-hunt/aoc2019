import intcode
import itertools

def run_amplifiers(memory, phases):
    power = 0
    for phase in phases:
        ic = intcode.Intcode(memory)
        ic.set_input([phase, power])
        ic.run_program()
        power = ic.output
    return power

def feedback_amplifiers(memory, phases):
    amps = []
    for phase in phases:
        ic = intcode.Intcode(memory)
        amps.append(ic)
        ic.set_input([phase])
    power = 0
    while not amps[-1].is_halted():
        for amp in amps:
            amp.input.append(power)
            amp.run_to_output()
            power = amp.output
    return power


def run():
    init_memory = intcode.parse_input_to_memory("d7input.txt")
    powers = []
    for phases in itertools.permutations([0, 1, 2, 3, 4]):
        powers.append(run_amplifiers(init_memory, phases))
    print(max(powers))

    powers = []
    for phases in itertools.permutations([5,6,7,8,9]):
        powers.append(feedback_amplifiers(init_memory, phases))
    print(max(powers))

run()
