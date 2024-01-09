import TuringMachine

def input_set(prompt, default_value):
    user_input = input(prompt + f" or use the following default input by pressing enter [{', '.join(default_value)}]: ")
    return set(user_input.split()) if user_input else default_value

def input_transitions(default_value):
    print(
        "Enter transitions (state, symbol: next_state, new_symbol, direction), type 'end' to finish. Press Enter to use default.")
    first_input = input()
    if not first_input:
        return default_value

    transitions = dict(default_value)
    transitions.update(parse_transition(first_input))

    while True:
        transition_input = input()
        if transition_input == 'end':
            break
        transitions.update(parse_transition(transition_input))

    return transitions

def parse_transition(transition_input):
    key, value = transition_input.split(':')
    state, symbol = key.strip().split(', ')
    next_state, new_symbol, direction = value.strip().split(', ')
    return {(state, symbol): (next_state, new_symbol, direction)}


default_states = {'start', 'init', 'right', 'shift0', 'shift1', 'shift', 'tidy', 'done',
          'readB', 'read', 'add0', 'add1', 'addA', 'rewrite', 'doubleL', 'double', 'back0',
          'back1', 'carry', 'have0', 'have1', 'aster'}
default_symbols = {'0', '1', '*', 'i', 'c', 'o'}
default_input_alphabet = {'0', '1', '*'}
default_blank_symbol = '_'
default_tape_alphabet = {'0', '1', '*', '_', 'i', 'c', 'o', '+'}
default_initial_state = 'start'
default_final_states = {'done'}
default_transitions = {
    ('start', '0'): ('init', '0', 'L'),
    ('start', '1'): ('init', '1', 'L'),
    ('init', default_blank_symbol): ('aster', '+', 'R'),
    ('aster', '0'): ('aster', '0', 'R'),
    ('aster', '1'): ('aster', '1', 'R'),
    ('aster', default_blank_symbol): ('right', '*', 'R'),
    ('right', '0'): ('right', '0', 'R'),
    ('right', '1'): ('right', '1', 'R'),
    ('right', '*'): ('right', '*', 'R'),
    ('right', default_blank_symbol): ('readB', default_blank_symbol, 'L'),
    ('readB', '1'): ('addA', default_blank_symbol, 'L'),
    ('readB', '0'): ('doubleL', default_blank_symbol, 'L'),
    ('addA', '0'): ('addA', '0', 'L'),
    ('addA', '1'): ('addA', '1', 'L'),
    ('addA', '*'): ('read', '*', 'L'),
    ('read', '0'): ('have0', 'c', 'L'),
    ('read', '1'): ('have1', 'c', 'L'),
    ('read', '+'): ('rewrite', '+', 'L'),
    ('have0', '0'): ('have0', '0', 'L'),
    ('have0', '1'): ('have0', '1', 'L'),
    ('have0', '+'): ('add0', '+', 'L'),
    ('add0', 'o'): ('add0', 'o', 'L'),
    ('add0', 'i'): ('add0', 'i', 'L'),
    ('add0', '1'): ('back0', 'i', 'R'),
    ('add0', '0'): ('back0', 'o', 'R'),
    ('add0', default_blank_symbol): ('back0', 'o', 'R'),
    ('back0', '0'): ('back0', '0', 'R'),
    ('back0', '1'): ('back0', '1', 'R'),
    ('back0', 'o'): ('back0', 'o', 'R'),
    ('back0', 'i'): ('back0', 'i', 'R'),
    ('back0', '+'): ('back0', '+', 'R'),
    ('back0', 'c'): ('read', '0', 'L'),
    ('rewrite', '0'): ('rewrite', '0', 'L'),
    ('rewrite', '1'): ('rewrite', '1', 'L'),
    ('rewrite', 'o'): ('rewrite', '0', 'L'),
    ('rewrite', 'i'): ('rewrite', '1', 'L'),
    ('rewrite', default_blank_symbol): ('double', default_blank_symbol, 'R'),
    ('double', '0'): ('double', '0', 'R'),
    ('double', '1'): ('double', '1', 'R'),
    ('double', '+'): ('double', '+', 'R'),
    ('double', '*'): ('shift', '0', 'R'),
    ('have1', '0'): ('have1', '0', 'L'),
    ('have1', '1'): ('have1', '1', 'L'),
    ('have1', '+'): ('add1', '+', 'L'),
    ('add1', 'o'): ('add1', 'o', 'L'),
    ('add1', 'i'): ('add1', 'i', 'L'),
    ('add1', '1'): ('carry', 'o', 'L'),
    ('add1', '0'): ('back1', 'i', 'R'),
    ('add1', default_blank_symbol): ('back1', 'i', 'R'),
    ('carry', '1'): ('carry', '0', 'L'),
    ('carry', '0'): ('back1', '1', 'R'),
    ('carry', default_blank_symbol): ('back1', '1', 'R'),
    ('back1', '0'): ('back1', '0', 'R'),
    ('back1', '1'): ('back1', '1', 'R'),
    ('back1', 'o'): ('back1', 'o', 'R'),
    ('back1', 'i'): ('back1', 'i', 'R'),
    ('back1', '+'): ('back1', '+', 'R'),
    ('back1', 'c'): ('read', '1', 'L'),
    ('doubleL', '0'): ('doubleL', '0', 'L'),
    ('doubleL', '1'): ('doubleL', '1', 'L'),
    ('doubleL', '*'): ('shift', '0', 'R'),
    ('shift', '0'): ('shift0', '*', 'R'),
    ('shift', '1'): ('shift1', '*', 'R'),
    ('shift', default_blank_symbol): ('tidy', default_blank_symbol, 'L'),
    ('shift0', '0'): ('shift0', '0', 'R'),
    ('shift0', '1'): ('shift1', '0', 'R'),
    ('shift0', default_blank_symbol): ('right', '0', 'R'),
    ('shift1', '1'): ('shift1', '1', 'R'),
    ('shift1', '0'): ('shift0', '1', 'R'),
    ('shift1', default_blank_symbol): ('right', '1', 'R'),
    ('tidy', '0'): ('tidy', default_blank_symbol, 'L'),
    ('tidy', '1'): ('tidy', default_blank_symbol, 'L'),
    ('tidy', '+'): ('done', default_blank_symbol, 'L'),
}


default_initial_tape = '11_11'


states = input_set("Enter all states separated by space", default_states)
symbols = input_set("Enter all symbols separated by space", default_symbols)
input_alphabet = input_set("Enter all input alphabet symbols separated by space", default_input_alphabet)
blank_symbol = input(f"Enter the blank symbol [{default_blank_symbol}]: ") or default_blank_symbol
tape_alphabet = input_set("Enter all tape alphabet symbols separated by space", default_tape_alphabet)
initial_state = input(f"Enter the initial state [{default_initial_state}]: ") or default_initial_state
final_states = input_set("Enter the final states separated by space", default_final_states)
transitions = input_transitions(default_transitions)
initial_tape = input(f"Enter the initial tape content [{default_initial_tape}]: ") or default_initial_tape


tm = TuringMachine.TM(states, symbols, blank_symbol, initial_state, final_states, transitions, initial_tape)
tm.run()
tm.print_trace()
encoded_tm = tm.encode_turing_machine(states, input_alphabet, tape_alphabet, transitions, initial_state, final_states)
print(encoded_tm)
