#!/usr/bin/env python3

import sys

#input_file = sys.argv[1]
#output_file = sys.argv[2]

v1 = ['เ','แ','โ','ใ','ไ']
c1 = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
c2 = ['ร', 'ล', 'ว', 'น', 'ม']
v2 = ['\u0E31', '\u0E34', '\u0E35', '\u0E36', '\u0E37', '\u0E38', '\u0E39', '\u0E47']
t = ['\u0E48', '\u0E49', '\u0E4A', '\u0E4B']
v3 = ['า', 'อ', 'ย', 'ว']
c3 = ['ง', 'น', 'ม', 'ด', 'บ', 'ก', 'ย', 'ว']

def tokenize(): #line is the argument
	#define a function that will take in a line of Thai text (without spaces), and return the line with spaces between the words
	curr_state = None #tracks the current state, int
	start_state = 0 #keeps the int start state, shouldn't change
	end_states = [] #keeps a list of valid end states
	state_transitions = [] #2-d array representing the state transition matrix

	state_transitions = [[1,2,None,None,None,None,None,None],[None,2,None,None,None,None,None,None,],[7,8,3,4,5,6,9,None],[None,None,None,4,5,6,9,None],[7,8,None,None,5,6,9,None],[7,8,None,None,None,None,9,None],[7,8,None,None,None,None,9,None],[None,None,None,None,None,None,None,1],[None,None,None,None,None,None,None,2],[None,None,None,None,None,None,None,0]]
	for i in range(0, len(state_transitions)):
		print(state_transitions[i])

tokenize()


"""with open(in_file, 'r') as open_in:
	with open(out_file, 'w') as open_out:
		for line in open_in.readlines():
			spaced_line = tokenize(line)
			open_out.write(spaced_line) """