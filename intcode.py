import math
from collections import defaultdict

def parse_input_to_memory(filename):
    init_memory = defaultdict(int)
    with open(filename, "r") as file:
        text = file.read()
        addr = 0
        for s in text.split(","):
            init_memory[addr] = int(s)
            addr += 1
    return init_memory


class ProgramBreak(Exception):
    pass

class UnknownArgMode(Exception):
    pass

class Intcode:
    def __init__(self, init_memory, dump_io=False):
        self.pc = 0
        self.rb = 0
        self.memory = defaultdict(int, init_memory)
        self.opcodes = {
            1: [3, self.opcode_add, 3],
            2: [3, self.opcode_multiply, 3],
            3: [1, self.opcode_input, 1],
            4: [1, self.opcode_output, None],
            5: [2, self.opcode_jump_if_true, None],
            6: [2, self.opcode_jump_if_false, None],
            7: [3, self.opcode_less_than, 3],
            8: [3, self.opcode_equals, 3],
            9: [1, self.opcode_adjust_rb, None],
            99: [0, self.opcode_halt, None],
        }
        self.input = []
        self.input_n = 0
        self.output = 0
        self.halted = False
        self.needs_input = False
        self.dump_io = dump_io

    def is_halted(self):
        return self.halted

    def add_input(self, input):
        self.input.append(input)
        self.needs_input = False

    def set_noun_verb(self, noun, verb):
        self.memory[1] = noun
        self.memory[2] = verb

    def opcode_add(self, a1, a2, dest):
        self.memory[dest] = a1 + a2

    def opcode_multiply(self, a1, a2, dest):
        self.memory[dest] = a1 * a2

    def opcode_halt(self):
        self.halted = True
        raise ProgramBreak

    def opcode_input(self, addr):
        if self.dump_io:
            print("INPUT!:", self.input[self.input_n])
        if len(self.input) > self.input_n:
            self.memory[addr] = self.input[self.input_n]
            self.input_n += 1
        else:
            self.pc -= 2
            self.needs_input = True
            raise ProgramBreak

    def opcode_output(self, val):
        if self.dump_io:
            print("OUTPUT:", val) 
        self.output = val
        raise ProgramBreak

    def opcode_jump_if_true(self, val, target):
        if val != 0:
            return target

    def opcode_jump_if_false(self, val, target):
        if val == 0:
            return target

    def opcode_less_than(self, v1, v2, dest):
        self.memory[dest] = 1 if v1 < v2 else 0

    def opcode_equals(self, v1, v2, dest):
        self.memory[dest] = 1 if v1 == v2 else 0

    def opcode_adjust_rb(self, a):
        self.rb += a

    def get_arg(self, n, mode, output_arg):
        val = self.memory[self.pc+n]
        if mode == 0 and n != output_arg:
            return self.memory[val]
        elif mode == 1 or (mode == 0 and n == output_arg):
            return val
        elif mode == 2 and n != output_arg:
            return self.memory[self.rb + val]
        elif mode == 2 and n == output_arg:
            return self.rb + val
        else:
            print("Unknown arg mode:", mode)
            raise UnknownArgMode

    def run_program(self):
        out = 0
        while not self.is_halted():
            out = self.run_to_output()
        return out

    def run_to_output(self):
        try:
            while True:
                opcode = self.memory[self.pc] % 100
                n_args, func, output_arg = self.opcodes[opcode]
                modes = [math.floor(self.memory[self.pc] / 10**(2+i)) % 10 for i in range(n_args)]
                args = [self.get_arg(i+1, modes[i], output_arg) for i in range(n_args)]
                self.pc += n_args + 1
                ret = func(*args)
                if ret != None:
                    self.pc = ret
        except ProgramBreak:
            # Exceptions for control flow.
            # I feel dirty, but it's the smoothest way to do this in python without hardcoding in the halt instruction.
            return self.memory[0]
