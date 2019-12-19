with open(r'advent_of_code\input.txt', 'r') as f:
   input = list(map(int,f.read().strip().split()))

def get_fuel(input):
    fuel = 0
    for mass in input:
        fuel += (mass//3)-2
    return fuel

def total_fuel(input):
    fuel = 0
    for mass in input:
        while (mass//3)-2 > 0:
            if (mass//3)-2 > 0:
                mass = (mass//3)-2
                fuel += mass
    # total = np.sum(fuel(x))
    return fuel

print(get_fuel(input))
print(total_fuel(input))
