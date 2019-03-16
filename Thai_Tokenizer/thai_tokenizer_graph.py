#!/usr/bin/env python3
# graph style FSA

import sys
from typing import Type

input_file = sys.argv[1]
output_file = sys.argv[2]

v1 = ['เ', 'แ', 'โ', 'ใ', 'ไ']
c1 = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท',
      'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
c2 = ['ร', 'ล', 'ว', 'น', 'ม']
v2 = ['\u0E31', '\u0E34', '\u0E35', '\u0E36', '\u0E37', '\u0E38', '\u0E39', '\u0E47']
t = ['\u0E48', '\u0E49', '\u0E4A', '\u0E4B']
v3 = ['า', 'อ', 'ย', 'ว']
c3 = ['ง', 'น', 'ม', 'ด', 'บ', 'ก', 'ย', 'ว']


class StateNode:
    def __init__(self):
        self.state_number = None
        self.is_start = False
        self.is_end = False
        self.next_states = dict()  # dictionary where the keys are chartypes and the values are possible next nodes

    # given a char, return the next state
    def get_nextstate(self, char):
        if char in c2 and 'c2' in self.next_states:
            return self.next_states['c2']
        elif char in v2 and 'v2' in self.next_states:
            return self.next_states['v2']
        elif char in t and 't' in self.next_states:
            return self.next_states['t']
        elif char in v3 and 'v3' in self.next_states:
            return self.next_states['v3']
        elif char in c3 and 'c3' in self.next_states:
            return self.next_states['c3']
        elif char in v1 and 'v1' in self.next_states:
            return self.next_states['v1']
        elif char in c1 and 'c1' in self.next_states:
            return self.next_states['c1']
        else:
            return None


# make the nodes!
q0 = StateNode()
q0.state_number = 0
q0.is_start = True

string = "อ"
for chara in string:
    print(q0.get_nextstate(chara))

q1 = StateNode()
q1.state_number = 1

q2 = StateNode()
q2.state_number = 2

q3 = StateNode()
q3.state_number = 3

q4 = StateNode()
q4.state_number = 4

q5 = StateNode()
q5.state_number = 5

q6 = StateNode()
q6.state_number = 6

q7 = StateNode()
q7.state_number = 7

q8 = StateNode()
q8.state_number = 8

q9 = StateNode()
q9.state_number = 9

# populate the next_states list for each node
q0.next_states = {'v1': q1, 'c1': q2}
q1.next_states = {'c1': q2}
q2.next_states = {'c2': q3, 'v2': q4, 't': q5, 'v3': q6, 'c3': q9, 'v1': q7, 'c1': q8}
q3.next_states = {'v2': q4, 't': q5, 'v3': q6, 'c3': q9}
q4.next_states = {'t': q5, 'v3': q6, 'c3': q9, 'v1': q7, 'c1': q8}
q5.next_states = {'v3': q6, 'c3': q9, 'v1': q7, 'c1': q8}
q6.next_states = {'c3': q9, 'v1': q7, 'c1': q8}
q7.next_states = {'#': q1}
q8.next_states = {'#': q2}
q9.next_states = {'#': q0}

start_state: Type[StateNode] = q0  # keeps the int start state, shouldn't change
end_states = []


# use a loop to put each char as a dict item in each applicable node
def tokenize(line):
    # define a function that will take in a line of Thai text (without spaces), and return the line with spaces between the words
    curr_state: Type[StateNode] = q0
    print(str(curr_state.state_number))
    # next_state: Type[StateNode] = None
    output_string = ""
    for char in line:
        if curr_state is q7:
            curr_state = q1
        elif curr_state is q8:
            curr_state = q2
        elif curr_state is q9:
            curr_state = start_state

        output_string += char
        next_state = curr_state.get_nextstate(char)

        print(output_string)
        print("state: " + str(curr_state.state_number))
        print("->" + str(next_state.state_number))

        if next_state is q7 or next_state is q8:
            output_string += " " + char + "R"
        elif next_state is q9:
            output_string += char + " " + "L"
        curr_state = next_state
    return output_string


with open(input_file, 'r') as open_in:
    with open(output_file, 'w') as open_out:
        for line in open_in.readlines():
            spaced_line = tokenize(line.strip())  # needed to remove newlines-- thanks, Justin!
            open_out.write(spaced_line + "\n")
