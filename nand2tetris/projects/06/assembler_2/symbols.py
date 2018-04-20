from structuring import *


symbols = {
			'R0'		:'0',
			'R1'		:'1',
			'R2'		:'2',
			'R3'		:'3',
			'R4'		:'4',
			'R5'		:'5',
			'R6'		:'6',
			'R7'		:'7',
			'R8'		:'8',
			'R9'		:'9',
			'R10'		:'10',
			'R11'		:'11',
			'R12'		:'12',
			'R13'		:'13',
			'R14'		:'14',
			'R15'		:'15',
			'SCREEN'	:'16384',
			'KBD'		:'24576',
			'SP'		:'0',
			'LCL'		:'1',
			'ARG'		:'2',
			'THIS'		:'3',
			'THAT'		:'4'
};

def label_recognizer(table):
	for i in range(len(table)):
		line=table[i];
		if line[1][0] == '(':
			symbols[line[1][1:len(line[1])-1]] = line[2];
	return symbols

#some error in var_rec
def var_recognizer(table):
	free_address = 16;
	for i in range(len(table)):
		line = table[i];
		if line[1][0] == '@' and is_not_number(line[1][1]) and not( used(line[1][0][1:]) ):
			print(line[1][0][1:])
			symbols[line[1][1:]] = free_address;
			free_address += 1;

	return symbols

def used(symbol):
    try: 
        symbols[symbol]
        return True
    except KeyError:
        return False

def is_not_number(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

symbols = label_recognizer(assembly_table);
symbols = var_recognizer(assembly_table);

symbols_table = [['Symbol', 'memory_address']];

for i in symbols:
	symbols_table.append([i, symbols[i]]);

