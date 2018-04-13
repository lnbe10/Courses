#import not working .-.

#import tables
#os.system('python tables')
dest={ 	
		'null'	:'000',
		'M'		:'001',
		'D'		:'010',
		'MD'	:'011',
		'A'		:'100',
		'AM'	:'101',
		'AD'	:'110',
		'AMD'	:'111',
		};

jump={
		'null'	:'000',
		'JGT'	:'001',
		'JEQ'	:'010',
		'JGE'	:'011',
		'JLT'	:'100',
		'JNE'	:'101',
		'JLE'	:'110',
		'JMP'	:'111',
		};

compute={
			'0'		:'0101010',
			'1'		:'0111111',
			'-1'	:'0111010',
			'D'		:'0001100',
			'A'		:'0110000',
			'M'		:'1110000',
			'!D'	:'0001101',
			'!A'	:'0110001',
			'!M'	:'1110001',
			'-D'	:'0001111',
			'-A'	:'0110011',
			'-M'	:'1110011',
			'D+1'	:'0011111',
			'A+1'	:'0110111',
			'M+1'	:'1110111',
			'D-1'	:'0001110',
			'A-1'	:'0110010',
			'M-1'	:'1110010',
			'D+A'	:'0000010',
			'D+M'	:'1000010',
			'D-A'	:'0010011',
			'D-M'	:'1010011',
			'A-D'	:'0000111',
			'M-D'	:'1000111',
			'D&A'	:'0000000',
			'D&M'	:'1000000',
			'D|A'	:'0010101',
			'D|M'	:'1010101',
			};


lines=open('add.asm', 'r').read().split('\n');

lines = [x for x in lines if x[0:2]!='//'];

for i in range(len(lines)):
	for j in range(len(lines[i])):
		if (lines[i][j:j+2]=='//'):
			lines[i]=lines[i].replace(lines[i][j:], '');

lines = [x for x in lines if x!=''];

#lines now contains only strings with commands, like:
#['@2', 'D=D+M', '@LOOP', '(LOOP)', '@3', 'M=A', 'D;JMP', ...];

assembly = lines; #creating a mirror

element_list=list(range(len(assembly)));


def A_C_instruction(as_list):
	for i in range(len(assembly)):
		line = as_list[i];
		if line[0] == '@':		#if A instruction:
			address = bin(int(line[1:]))[2:]; #address='10101'
			quotient, remainder = divmod(len(address),16);
			if quotient > 0:
				print('Error: some address is too big');
			address = '0' * (16 - remainder) + str(address);
			#now address is 16-bit
			as_list[i] = address;
		
		# C instr
		# 1 11 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3
		elif line.find('=') != -1 or line.find(';') != -1:
			line= line.split(';');
			#line = ['M=D+M', 'JMP'] 
			for j in range(len(line)):
				line[j]=line[j].split('=');
				#line = [['M','MD'], 'JMP']
			instr = '111' + compute[line[0][1]] +  dest[line[0][0]];
			if len(line) > 1:
				instr += jump[line[1]];
			else:
				instr += '000';

			as_list[i] = instr;

		element_list.remove(i);

	return as_list;



print(assembly);
assembly = A_C_instruction(assembly);


print(assembly);
print(element_list);


