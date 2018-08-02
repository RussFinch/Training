

/*
● Create a new file called sumElements.java
● Write a program that returns the sum of all elements in a specified column of a
	two-dimensional array.
● Firstly ask the user to enter a 3-by-4 array. The user should enter the array as follows:
	2.6 5.1 6 8
	5.4 4.4 7 1
	9.5 7.9 2 3
● The program should then calculate the sum of each column in the array.
*/

import java.util.Scanner;

public class sumElements {

	public static void main(String[] args) {
		
		int row = 3;
		int column = 4;
		float[][] array0 = new float[row][column];
		
		Scanner input0 = new Scanner(System.in);
		System.out.println("Enter elements for a 3-by-4 array:");
		for (row=0; row<3; row++) {
			for (column=0; column<4; column++) {
				array0[row][column] = input0.nextFloat();
				}
			}
		for (row=0; row<3; row++) {
			System.out.println();
			for (column=0; column<4; column++) {
				System.out.print(array0[row][column] + "\t");
			}
		}
		float total = 0;
		System.out.println("\nTotals:");
		for (column=0; column<4; column++) {
			for (row=0; row<3; row++) {
				if (row <2) {
					total += array0[row][column];
				}
				else {
					total += array0[row][column];
					System.out.print(total + "\t");
					total = 0;
				}
			}	
		}
		input0.close();
	}
}
