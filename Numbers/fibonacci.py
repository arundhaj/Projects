'''
Program to generate fibonacci sequence for the required number of digits
'''

def fibonacci(digit):
	sequence = [1]

	if digit > 1:
		sequence.append(1)

	while(len(sequence) < digit):
		sequence.append(sequence[-1] + sequence[-2])

	# convert int list to string list
	for i in range(len(sequence)):
		sequence[i] = str(sequence[i])

	return sequence

digit = int(raw_input('Enter number of digit required: '))
sequence = fibonacci(digit)

print ', '.join(sequence)
