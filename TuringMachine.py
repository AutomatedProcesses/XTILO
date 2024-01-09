class TM:
    def __init__(self, states, symbols, blank_symbol, initial_state, final_states, transitions, initial_tape):
        """
        The function initializes the Turing machine with the given states, symbols, blank symbol, initial state, final
        states, transitions, and initial tape.

        :param states: The states parameter is a list that represents all the possible states of the Turing machine. Each
        state is represented by a unique string
        :param symbols: The "symbols" parameter represents the set of symbols that can be used on the Turing machine's tape.
        These symbols can include any characters or symbols that the Turing machine can read and write on its tape
        :param blank_symbol: The `blank_symbol` parameter is a symbol that represents an empty cell on the tape. It is used
        to initialize the tape and can be any symbol that is not in the set of input symbols
        :param initial_state: The initial state is the starting state of the Turing machine. It represents the state in
        which the machine begins its computation
        :param final_states: The `final_states` parameter is a list of states that are considered as final or accepting
        states in the Turing machine. When the Turing machine reaches one of these states, it halts and accepts the input
        :param transitions: The "transitions" parameter is a dictionary that represents the transition function of a Turing
        machine. It maps a tuple of the current state and the current symbol under the tape head to a tuple of the next
        state, the symbol to write on the tape, and the direction to move the tape head
        :param initial_tape: The initial_tape parameter is used to specify the initial content of the Turing machine's tape.
        It is a string that represents the symbols on the tape. For example, if the initial tape is '11*11', it means that
        the tape initially contains the symbols '1', '1', '*',
        """
        self.states = states
        self.symbols = symbols
        self.blank_symbol = blank_symbol
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = initial_state
        self.head_position = 0
        self.trace_log = []

        if initial_tape is not None:
            self.tape = list(initial_tape)
        else:
            raise ValueError('Wrong input. Please provide initial tape, e.g. \'11*11\'.')

    def step(self):
        """
        The function `step` performs a single step in a Turing machine by updating the current state, tape symbol, head
        position, and trace log, and then printing the current tape and head position.
        """
        current_symbol = self.tape[self.head_position]
        action = self.transitions.get((self.current_state, current_symbol))

        if action is not None:
            new_state, new_symbol, move_direction = action
            self.tape[self.head_position] = new_symbol
            self.current_state = new_state

            if move_direction == 'R':
                self.head_position += 1
                if self.head_position == len(self.tape):
                    self.tape.append(self.blank_symbol)
            elif move_direction == 'L':
                if self.head_position == 0:
                    self.tape.insert(0, self.blank_symbol)
                else:
                    self.head_position -= 1
            self.trace_log.append((self.current_state, current_symbol, action, ''.join(self.tape)))
        else:
            raise ValueError(f"No transition defined for state '{self.current_state}' and symbol '{current_symbol}'")
        tape_str = ''.join(self.tape)
        head_indicator = ' ' * self.head_position + '^'
        print(tape_str)
        print(head_indicator)

    def run(self):
        """
        The function runs a loop until the current state is one of the final states, and then prints a message indicating
        that the final state has been reached.
        """
        while self.current_state not in self.final_states:
            self.step()
        print('Final state reached.')

    def print_trace(self):
        """
        The function prints each log entry in the trace log.
        """
        for log_entry in self.trace_log:
            print(log_entry)

    def encode_turing_machine (self, states, input_alphabet, tape_alphabet, transitions, start_state, accept_states, reject_states=None):
        """
        The function `encode_turing_machine` encodes a Turing machine into a string representation using a specific encoding
        scheme.

        :param states: The parameter "states" represents the set of states in the Turing machine. It is a collection of all
        possible states that the machine can be in during its computation
        :param input_alphabet: The input_alphabet is a list of symbols that can be read from the tape by the Turing machine
        :param tape_alphabet: The `tape_alphabet` parameter represents the set of symbols that can be written on the tape of
        the Turing machine. It is a list of symbols that can be used as input or output on the tape
        :param transitions: The "transitions" parameter is a dictionary that represents the transitions of the Turing
        machine. Each key-value pair in the dictionary represents a transition from one state and symbol to another state,
        symbol, and movement direction
        :param start_state: The `start_state` parameter represents the initial state of the Turing machine. It is the state
        in which the Turing machine starts its computation
        :param accept_state: The `accept_state` parameter represents the state in the Turing machine where the machine
        should halt and accept the input
        :param reject_state: The `reject_state` parameter is an optional parameter that represents the state in which the
        Turing machine should transition to if it encounters a configuration that should be rejected. If no `reject_state`
        is provided, the Turing machine will halt and reject the input
        :return: a string that represents the encoding of a Turing machine.
        """
        states = list(states)
        input_alphabet = list(input_alphabet)
        tape_alphabet = list(tape_alphabet)

        states_encoding = '0' * len(states)
        m = len(input_alphabet)
        p = len(tape_alphabet) - m
        alphabet_encoding = f'0{m}10{p}'
        transitions_encoding = '11'.join(
            f'0{states.index(state)}10{tape_alphabet.index(symbol) + 1}10{states.index(next_state)}10{tape_alphabet.index(new_symbol) + 1}10{1 if move == "L" else 2}'
            for (state, symbol), (next_state, new_symbol, move) in transitions.items()
        )
        start_encoding = f'0{states.index(start_state)}'

        if isinstance(accept_states, (set, list)):
            accept_encoding = '11'.join(f'0{states.index(state)}' for state in accept_states)
        else:
            accept_encoding = f'0{states.index(accept_states)}'

        if reject_states:
            if isinstance(reject_states, (set, list)):
                reject_encoding = '11'.join(f'0{states.index(state)}' for state in reject_states)
            else:
                reject_encoding = f'0{states.index(reject_states)}'
        else:
            reject_encoding = ''

        encoding_parts = [states_encoding, alphabet_encoding, transitions_encoding, start_encoding, accept_encoding, reject_encoding]

        return '111'.join(encoding_parts)