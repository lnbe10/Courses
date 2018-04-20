#here i open the assembly archive, store the instructions in a list
# lines = ['@12', 'M=D+M', '(LOOP)', '0;JMP']
#and store the addresses in wich they are\ to wich they refer (in the case of (XXX) instructions)

lines=open('Rect.asm', 'r').read().split('\n');

lines = [x for x in lines if x[0:2]!='//'];

for i in range(len(lines)):
	line = lines[i];
	line = line.split('//')[0];
	for j in range(len(line)):
		if (line[j:j+2] == '\t'):
			lines[i] = line.replace(line[j:j+2], '');
		elif (line[j] == ' '):
			lines[i] = line.replace(line[j], '');

lines = [x for x in lines if x!=''];

f=open('lines.txt', 'w');
for i in range(len(lines)):
	f.write(lines[i]+'\n');
f.close()


def instruction_address_counter(lines):
	instr_counter = [];
	counter = 0;
	for i in range(len(lines)):
		instr_counter.append([]);
		line = lines[i];
		if line[0] != '(':
			instr_counter[i].append(i);
			instr_counter[i].append(counter);
			counter += 1;
		else:
			instr_counter[i].append(i);
			instr_counter[i].append(counter);
	return instr_counter;

assembly_table = [['line', 'instructions', 'memory_address']];

for i in range(len(lines)):
	assembly_table.append([instruction_address_counter(lines)[i][0], lines[i], instruction_address_counter(lines)[i][1]]);
