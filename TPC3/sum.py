import re

class SummingAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.total = 0

    def process(self, text):
        words = re.split(r'\s+', text)
        for word in words:
            for symbol, pattern in self.alphabet.items():
                if re.match(pattern, word):
                    self.current_state = self.transitions[self.current_state][symbol][0]
                    if symbol == r'\d+' and self.current_state == 'ON':
                        self.total += int(word)
                    elif symbol == '=':
                        print('total: ' + str(self.total))

states = {'ON', 'OFF'}
alphabet = {r'\d+': re.compile(r'\d+'), 'off': re.compile(r"[Oo][Ff]{2}"), 'on': re.compile(r"[Oo][Nn]"), '=': re.compile(r"=")}
transitions = {
    'ON': {
        'off': ('OFF', None),
        'on': ('ON', None),
        '=': ('ON', 'output'),
        r'\d+': ('ON', None)
    },
    'OFF': {
        'off': ('OFF', None),
        'on': ('ON', None),
        '=': ('OFF', 'output'),
        r'\d+': ('OFF', None)
    }
}

if __name__ == '__main__':
    import unittest

    class TestSummingAutomaton(unittest.TestCase):
        def setUp(self):
            self.automaton = SummingAutomaton(states, alphabet, transitions, 'OFF', {})

        def test_process(self):
            self.automaton.process("ON 5 10 OFF 7 ON 3 =")
            self.assertEqual(self.automaton.total, 18)

    unittest.main()

