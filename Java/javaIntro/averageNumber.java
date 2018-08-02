/*
Follow these steps:
● Create a new file called averageNumber.java
● Write a program that determines how many positive and negative integers have been
entered and calculates the total and average of all the entered numbers.
● Firstly ask the user to enter any number of integers. The user should enter 0 to indicate
the end of their input.
● The program should then determine the number of positive and negative integers
entered by the user, and print out the result.
● The total of all integers entered as well as the average should then be calculated and
displayed.
*/



import java.util.Scanner;

public class averageNumber {

	public static void main(String[] args) {
		int total = 0;
		int integerCounter = 0;
		
		System.out.println("0 to quit.\n" + "Please enter a integer number:");
		
		Scanner input = new Scanner(System.in);
		while (true) {
			int userInput = input.nextInt();
			if (userInput == 0){
				System.out.println("User terminated integer input.\n\n");
				System.out.println("The number of integers entered:\t"
									+ integerCounter);
				System.out.println("The total of all integers is:\t"
									+ total);
				float average = (total / integerCounter);
				System.out.println("The average of all integers is:\t" 
									+ average);
				input.close();
				System.exit(0);
			}
			else if (userInput >= 1) {
				total += userInput;
				integerCounter += 1;			
			}
			else if (userInput <= 1) {
				total += userInput;
				integerCounter += 1;
			}
		}
		
	}
}
