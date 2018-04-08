// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1
D=M		//D = RAM[1]

@limit
M=D		//setting limit for counter

@i
M=1		//counter

@sum
M=0		//setting sum=0 in some rand mem.location

(LOOP)
	@i
	D=M	//D = i

	@limit
	D=D-M	//D = i-limit

	@END
	D;JGT	//if (i-limit)>0 goto END
	
	@R0
	D=M

	@sum
	MD=M+D	//sum = sum + r1
	
	@R2
	M=D	//saving sum in RAM[2]

	@i
	M=M+1	//i = i + 1
	
	@LOOP
	0;JMP	//goto LOOP

(END)
	@END
	0;JMP	//infinite LOOP to avoid attacks

// changed the R2 to be updated in the looping instead
// of in the (END), because if @sum gets lost
// while (END) is running, the R2 would turn to a wrong value
// creating a @sum to store the sum is not necessary
// in this case, but maybe in other kind of
// multiplications it would be a good way to do.