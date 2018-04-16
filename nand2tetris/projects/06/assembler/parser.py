import instructions as ins


lines=open('add.asm', 'r').read().split('\n');

lines = [x for x in lines if x[0:2]!='//'];

for i in range(len(lines)):
	for j in range(len(lines[i])):
		if (lines[i][j:j+2]=='//'):
			lines[i]=lines[i].replace(lines[i][j:], '');

lines = [x for x in lines if x!=''];


#I have to count the lines without labels, 
#and store them related to their element_string
#indexes...

def instruction_address_counter(as_list):
	instr_counter = [];
	for i in range(len(assembly)):
		instr_counter.append([]);
	counter = 0;
	for i in element_list:
		line = as_list[i];
		if line[0] != '(':
			instr_counter[i].append(i);
			instr_counter[i].append(counter);
			counter += 1;
		else:
			instr_counter[i].append(i);
			instr_counter[i].append(counter);
	return instr_counter;

def A_C_instruction(as_list):
	for i in range(len(assembly)):
		line = as_list[i];
		if line[0] == '@':
			as_list[i]  = ins.A_instr(line);
		elif line.find('=') != -1 or line.find(';') != -1:
			as_list[i] = ins.C_instr(line);
		element_list.remove(i);
	
	#now just the (XXX) and @symbol are not converted
	return as_list;


def symbol_recognizer(as_int):
	var_alloc_address = 16;
	for i in element_list:
		line = as_list[i];
		if line[0] == '@':		#if A instruction:
		#don't need to check if is @symbol, because
		#the element_list contains only indexes of
		#non converted A and C instructions.=>
		#(XXX) and @symbol
			if not_used(line[1:]):
				symbols[line[1:]]=bin(int(var_alloc_address));
				var_alloc_address += 1;



#lines now contains only strings with commands, like:
#['@2', 'D=D+M', '@LOOP', '(LOOP)', '@3', 'M=A', 'D;JMP', ...];

assembly = lines; #creating a mirror

element_list=list(range(len(assembly)));

print(instruction_address_counter(assembly));

print(assembly);
assembly = A_C_instruction(assembly);


print(assembly);
print(element_list);


#creating table of symbols

symbols = {};



