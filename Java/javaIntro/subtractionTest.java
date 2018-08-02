/*
● Look the poorly written, difficult to read program below:

	import java . util . Scanner;
	public class WhatDoesThisAppDo {
	public static void main ( String [] args ) {
	final int NUMBER = 5;
	int int2 = 0 ; int int1 = 0 ; long startTime =
	System . currentTimeMillis ();
	String string1 = " " ; Scanner string2 = new
	Scanner ( System . in );
	while ( int1 < NUMBER ) {
	int number1 = ( int )( Math . random () * 10 );
	int number2 = ( int )( Math . random () * 10 );
	if ( number1 < number2 ) {
	int temp = number1 ; number1 = number2 ; number2 = temp;
	}
	System . out . print(
	"What is " + number1 + " - " + number2 + "? " );
	int answer = string2 . nextInt ();
	if ( number1 - number2 == answer ) { System . out . println ( "You
	are correct!" ); int2 ++; // Increase the correct answer count
	}
	else
	System . out . println ( "Your answer is wrong.\n" + number1
	+ " - " + number2 + " should be " + ( number1 - number2 ));
	int1 ++;
	string1 += "\n" + number1 + "-" + number2 + "=" + answer +
	(( number1 - number2 == answer ) ? " correct" : " wrong" );
	}
	long endTime = System . currentTimeMillis ();
	long testTime = endTime - startTime;
	System . out . println ( "Correct count is " + int2 +
	"\nTest time is " + testTime / 1000 + " seconds\n" +
	string1 );
	}
	}
	
● Firstly, without running the program, determine what the the above code does. Write
	your answer in a text file called answers.txt.
● What is the output of this programme? (Provide your own input data if necessary)
	Write your answer in the answers.txt file.
● Rewrite this programme so that it is easier to read. Make sure your code has:

		○ descriptive variable names
		○ descriptive class names
		○ at least 3 comments
		○ consistent indentation
		○ code Grouping
*/


import java.util.Scanner;
		
public class subtractionTest {

	public static void main(String[] args) {
		
		final int endGame = 5;  // end game either 5 right or wrong.
		int rightCount = 0;
		int wrongCount = 0;
		long startTime = System.currentTimeMillis();
		String resultsOverview = " ";
		Scanner userInput = new Scanner(System.in);
		
		//Generate 2 random numbers from which to create question.
		while (wrongCount < endGame) {
			int randomNum1 = (int)(Math.random() * 10);
			int randomNum2 = (int)(Math.random() * 10);
			
			//Switch the numbers round so smallest subtracted from largest
			if (randomNum1 < randomNum2) { 
				int temp = randomNum1;
				randomNum1 = randomNum2;
				randomNum2 = temp;
				}
			
			// Output user questions
			System.out.print("What is " + randomNum1 + " - " + randomNum2 + "? ");
			
			int answer = userInput.nextInt();
			
			// Verify answer
			if (randomNum1 - randomNum2 == answer) { 
				System.out.println("You are correct!");
				rightCount ++;
				}
			else 
				System.out.println("Your answer is wrong.\n" + randomNum1 + " - "
									+ randomNum2 + " should be " 
									+ ( randomNum1 - randomNum2));
				wrongCount ++;
				
			//Appends results to resultsOverview string
			resultsOverview += "\n" + randomNum1 + "-" + randomNum2 + "=" + answer +  
								((randomNum1 - randomNum2 == answer) ? " correct" : " wrong"); 
			}
		// Output results
		long endTime = System.currentTimeMillis ();
		long testTime = endTime - startTime;
		
		System.out.println("Correct count is " + rightCount + "\nTest time is " 
							+ testTime / 1000 + " seconds\n" + resultsOverview);
		
		// Close userInput scanner to stop leaks.
		userInput.close();
		}

}

