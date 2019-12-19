with open(r"advent_of_code\input2.txt", 'r') as f:
    intcode = list(map(int,f.read().split(",")))

def step_one(intcode):
    # for i in range(0, len(intcode)-1, 4):
    pointer = 0
    while intcode[pointer] != 99:
        opcode = intcode[pointer]
        noun = intcode[pointer+1]
        verb = intcode[pointer+2]
        third = intcode[pointer+3]
        if opcode == 1:
            intcode[third] = intcode[noun] + intcode[verb]
        elif opcode == 2:
            intcode[third] = intcode[noun] * intcode[verb]
        else:
            raise RuntimeError(f"invalid opcode: {intcode[pointer]}")
        pointer += 4

def step_two(intcode, noun, verb):
    intcode = intcode[:]
    intcode[1] = noun
    intcode[2] = verb
    step_one(intcode)
    return intcode[0]

print(step_two(intcode, 12, 2))

target = 19690720
  
for noun in range(100):
    for verb in range(100):
        output = step_two(intcode, noun, verb)
        if output == target:
            print(noun, verb, 100*noun+verb)
            break
