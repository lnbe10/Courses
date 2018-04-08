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

@i
M=0	//setting counter to iterate in screen

(NULLINGCOUNTER)
	@i
	M=0

	@KBD
	D=M	

	@BLACKING
	D;JNE	//keyboard pressed -> go to BLACKENING

	@WHITENING
	D;JEQ	//keyboard not pressed -> go to WHITENING

	@NULLINGCOUNTER
	0;JMP	// if keyboard is killed, it works as and op. end.


(BLACKENING) // will paint it black row by row
	// routine to check if:
		// the keyboard still pressed
			@KBD
			D=M
			@NULLINGCOUNTER
			D;JEQ		//if keyboard not been pressed -> go to NULLINGCOUNTER

		// the screen is already black
			@i
			MD=M+1	//i=i+1, i=0::32
			@32	
			D=D-A	// D = i-32

			@NULLINGCOUNTER
			D;JGT		// if (i-32) > 0, jump off
	

	//if key is pressed and counter is not completed
	// do the routine to paint it black
	
	@SCREEN
	D=A-1	//D=16383
	
	@rownow
	M=M+D	// now = 16383+i, i=1::32

	@Rrownow
	M=-1	// set the Register (16383+i) to 111...111

	@BLACKENING
	0;JMP	//returns to the start of the looping	


(WHITENING)
	// routine to check if:
		// the keyboard still not pressed
			@KBD
			D=M
			@NULLINGCOUNTER
			D;JNE	//if keyboard pressed -> go to NULLINGCOUNTER


		// the screen is already white
			@i
			MD=M+1	// i = i+1, i=0::32
			@32	
			D=D-A	// D = i-32

			@NULLINGCOUNTER
			D;JGT	// if (i-32) > 0, jump off	

	// if key is pressed and counter is not completed
	// do the routine to turn it white
	
	@SCREEN
	D=A-1	//D=16383

	@rownow
	M=M+D	// now = 16383+i, i=1::32

	@Rrownow
	M=0	// set the Register (16383+i) to 000...000

	@WHITENING
	0;JMP	//returns to the start of the looping	




