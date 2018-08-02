/*
● Create a new file called identicalArrays.java
● Write a program that determines whether two arrays are identical.
● Ask the user to enter a number of integer values and store them in an array
● Then ask the user to enter a second set of integer values and store them in a different
	array.
● Now determine whether the two arrays are identical.
● If they are identical print out, “The two arrays are identical”
● If they are not identical print out, “The two arrays are not identical”
*/

import java.util.Scanner;

public class identicalArrays {

	public static void main(String[] args) {
		
		int[] array0 = new int[4];
		Scanner input0 = new Scanner(System.in);
		System.out.println("Please enter " + array0.length + " values for Array 0.");
		for (int i=0; i<array0.length; i++)
			array0[i] = input0.nextInt();
		
		int[] array1 = new int[4];
		Scanner input1 = new Scanner(System.in);
		System.out.println("Please enter " + array1.length + " values for Array 1.");
		for (int i=0; i<array1.length; i++)
			array1[i] = input1.nextInt();

		
		for (int i=0; i<array0.length; i++) {
			if (array0[i] == array1[i]) {
				System.out.println("Integers " + i + " match!");
				}
			else {
				System.out.println("\nIntegers " + i + " don't match."
						+ " the arrays AREN'T identical.");
				input0.close();
				input1.close();
				System.exit(0);
				}
		}
		System.out.println("\nThe Integer Arrays match.");
		input0.close();
		input1.close();
	}

}
