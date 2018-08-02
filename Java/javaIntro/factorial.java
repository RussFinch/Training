/*
● Create a new file called factorial.java
● Write a program that determines the factorial of a number entered by a user.
● Prompt the user to enter a positive integer.
● Then calculate the factorial of the given number. For any positive integer n, it’s factorial
is given by:
○ factorial = 1*2*3…*n
● Finally, print out the factorial.
*/

import java.util.Scanner;

public class factorial {

	public static void main(String[] args) {
				
		System.out.println("Please enter a positive Integer:");
		Scanner positiveInt = new Scanner(System.in);
		int integerInput = positiveInt.nextInt();
		
		int total = 1;
		
			for (int i = 1; i<=integerInput; i++) {
				total = total * i;
			}	
			
		positiveInt.close();	
		System.out.println("The factorial of " + integerInput + " is " + total);					
	}
}
