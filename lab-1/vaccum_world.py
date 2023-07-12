# Reflex based vaccum agent

# Two squares are in the world
sq_A = 'A'
sq_B = 'B'

# Goal state and current state definition
goal_state = {sq_A:'Clean', sq_B:'Clean'}
current_state = {sq_A:'', sq_B:''}

cost = 0

# Take input the square the agent is currently in
current_square = ''
while current_square not in ['A', 'B']:
    current_square = input('Enter square the agent is in (A/B):')

# Take input for state of each square
for square in current_state.keys():
    while True:
        current_state[square] = input(f'Enter state of square {square} (Dirty/Clean): ')
        if current_state[square] in ['Dirty', 'Clean']:
            break

def actuate(action:str):
    """Acts as actuator and changes current state and current square according to action"""

    global current_square
    global cost
    print()
    if action == 'Suck':
        print(f'Square {current_square} is dirty, sucking dirt!')
        cost += 1
        current_state[current_square] = 'Clean'
        print(f'Square {current_square} is now clean.')
    if action == 'Right':
        print(f'Square {current_square} is clean, moving right!')
        current_square = sq_B
        cost += 1
        print(f'Moved to square {current_square}.')
    if action == 'Left':
        print(f'Square {current_square} is clean, moving left!')
        current_square = sq_A
        cost += 1
        print(f'Moved to square {current_square}.')
    print()

def ReflexVaccumAgent():
    """Returns a program for reflex based vaccum agent."""

    def program(percept):
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        elif location == sq_A:
            return 'Right'
        elif location == sq_B:
            return 'Left'
    return program

vaccum = ReflexVaccumAgent()

while(current_state != goal_state):
    percept = (current_square, current_state[current_square])
    action = vaccum(percept) 
    actuate(action)

print('Total cost = ', cost)
