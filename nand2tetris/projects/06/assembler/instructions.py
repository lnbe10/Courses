import tables as tb

def A_instr(line):
	address = 0;
	if str_is_int(line[1:]):
		address = bin(int(line[1:]))[2:]; #address='10101'
		quotient, remainder = divmod(len(address),16);
		if quotient > 0:
			print('Error: some address is too big');
		address = '0' * (16 - remainder) + str(address);
		#now address is 16-bit
	return address
# C instr
# 1 11 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3

def C_instr(line):
	line= line.split(';');
	#line = ['M=D+M', 'JMP'] 
	for j in range(len(line)):
		line[j]=line[j].split('=');
		
		#line = [['M','M+D'], 'JMP']
		print(line)
	instr = '111' + tb.compute(line[0][1]) +  tb.dest(line[0][0]);
	if len(line) > 1:
		instr += jump(line[1]);
	else:
		instr += '000';

	return instr;

def str_is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def not_used(symbol):
    try: 
        symbols[symbol]
        return False
    except ValueError:
        return True
