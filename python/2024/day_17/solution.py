def get_combo_value(operand, registers):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    return None  # operand 7 is reserved

class Computer:
    def __init__(self, program, registers=None):
        self.program = [int(x) for x in program.split(',')]
        self.registers = registers or {'A': 0, 'B': 0, 'C': 0}
        self.ip = 0  # instruction pointer
        self.output = []

    def adv(self, operand, target_register='A'):
        combo_value = get_combo_value(operand, self.registers)
        divisor = 2 ** combo_value
        self.registers[target_register] = self.registers['A'] // divisor

    def bxl(self, operand):
        self.registers['B'] ^= operand

    def bst(self, operand):
        combo_value = get_combo_value(operand, self.registers)
        self.registers['B'] = combo_value % 8

    def jnz(self, operand):
        if self.registers['A'] != 0:
            self.ip = operand
            return True
        return False

    def bxc(self, _):
        self.registers['B'] ^= self.registers['C']

    def out(self, operand):
        combo_value = get_combo_value(operand, self.registers)
        self.output.append(str(combo_value % 8))

    def run(self):
        while self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]

            if opcode == 0:
                self.adv(operand)
            elif opcode == 1:
                self.bxl(operand)
            elif opcode == 2:
                self.bst(operand)
            elif opcode == 3:
                if self.jnz(operand):
                    continue
            elif opcode == 4:
                self.bxc(operand)
            elif opcode == 5:
                self.out(operand)
            elif opcode == 6:
                self.adv(operand, 'B')
            elif opcode == 7:
                self.adv(operand, 'C')

            self.ip += 2

        return ','.join(self.output)

def part1():
    input_data = open('python/2024/day_17/inputs.txt').read().strip()
    sections = input_data.split('\n\n')
    
    # Parse registers
    registers = {}
    for line in sections[0].splitlines():
        reg, value = line.split(': ')
        registers[reg[-1]] = int(value)
    
    # Parse program
    program = sections[1].replace('Program: ', '').strip()
    
    # Run program
    computer = Computer(program, registers)
    return computer.run()

def part2():
    input_data = open('python/2024/day_17/inputs.txt').read().strip()
    sections = input_data.split('\n\n')
    program = sections[1].replace('Program: ', '').strip()
    target_numbers = [int(x) for x in program.split(',')]
    
    # Try values for register A starting from 1
    a = 1
    while True:
        registers = {'A': a, 'B': 0, 'C': 0}
        computer = Computer(program, registers)
        output = computer.run()
        output_numbers = [int(x) for x in output.split(',')]
        
        if program == output:
            return a
        # Check if output matches program
        if output_numbers == target_numbers:
            return a
        
        a += 1
        if a % 10000 == 0:
            print(f"Tried up to {a}...")

if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")