// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//KBD refers to RAM[24576], in wich the last digit is stored
// if no digit was pressed, its = 0.


// SCREEN refers to RAM[16384] = 16bits
// a pixel is located in RAM[16384 + 32 * row + col / 16]
//  and is the col % 16 th bit... a %b (remainder of a/b)

@SCREEN
D=A

@pos
M=D

@8192
D=D+A

@max
M=D	//max = screen_initial_pos + 8192


(START)

	@KBD
	D=M
	
	@BLACK
	D;JNE
	//can't implement this as "equal" or "not equal", because, if
	//someone could press in one cycle and in the next unpress, none of the
	//conditions would be satisfied
	@WHITE
	0;JMP

(BLACK)

	@pos
	A=M	// address = current_position
	M=-1	//in the position address, M=1111...1111
	
	@INCR
	0;JMP

(WHITE)
	
	@pos
	A=M
	M=0	//same as before, but now M=0000...0000
	
	@INCR
	0;JMP

(INCR)

	@pos
	MD=M+1

	@max
	D=D-M	//D = pos-max

	@START
	D;JLT	//if {(pos-max) < 0} -> {pos < max}, goto START
	
	@SCREEN
	D=A
	@pos
	M=D
	
	@START
	0;JMP	


//this implementation doesn't check if the key still pressed while painting
//the screen in black or white

