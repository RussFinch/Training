/*
● 	Create a new java file called MyFile.java
 
● 	Write code to read the content of the text file input.txt. For each line in input.txt, write a
	new line in the new text file output.txt that computes the answer to some operation on
	a list of numbers.
	
● 	If the input.txt has the following:
		Min: 1,2,3,5,6
		Max: 1,2,3,5,6
		Avg: 1,2,3,5,6
	Your program should generate output.txt as follows:
		The min of [1, 2, 3, 5, 6] is 1.
		The max of [1, 2, 3, 5, 6] is 6.
		The avg of [1, 2, 3, 5, 6] is 3.4.
		
● 	Assume that the only operations given in the input file are min, max and avg, and that
	the operation is always followed by a list of comma separated integers. You should
	define the functions min, max and avg that take in a list of integers and return the min,
	max or avg of the list.
	
● 	Your program should handle any combination of operations and any length of input
	numbers. You can assume that the list of input numbers are always valid integers and
	that the list is never empty.
	
● 	Compile, save and run your file.
*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class MyFile {

	public static void main(String args[]) throws FileNotFoundException {
		  
		File inputFile = new File("/Users/russellfincham/documents/temp/input.txt");     
		Scanner fileScanner = new Scanner(inputFile);
		      
		while (fileScanner.hasNextLine()){
			
			String line = fileScanner.nextLine();
			String operation = line.substring(0, 3);
			String intString = line.substring(4, line.length());
			String[] strArray = intString.split(",");
			int[] intArray = new int[strArray.length];
				for (int i=0; i<intArray.length; i++){
					intArray[i] = Integer.parseInt(strArray[i]);
				}
				
				if (operation.equals("min")) {
					System.out.println("The min of " + Arrays.toString(strArray) + " is " + calculateMin(intArray) + ".");
				}
				if (operation.equals("max")) {
					System.out.println("The max of " + Arrays.toString(strArray) + " is " + calculateMax(intArray) + ".");
				}	
				if (operation.equals("avg")) {
					System.out.println("The avg of " + Arrays.toString(strArray) + " is " + calculateAvg(intArray) + ".");
				}
				if (operation.equals("Sum")) {
					System.out.println("The sum of " + Arrays.toString(strArray) + " is " + calculateSum(intArray) + ".");
				}
				if (operation.substring(0, 1).equals("P")) {
					System.out.println("The " + line.substring(1, 3) + "th percentile of " + Arrays.toString(strArray)
										+ " is " + calculatePercentile(operation, intArray) + ".");
				}
		}
		fileScanner.close();
	}
	
	public static int calculateMin(int[] intArray) {

			int min = intArray[0];
			
			for (int j=1; j<=intArray.length; j++) {
				if (j <= min) {
					min = j;
				}
			}
			return min;
	}
	
	public static int calculateMax(int[] intArray) {
		
			int max = intArray[0];
			
			for (int j=1; j<=intArray.length; j++) {
				if (j >= max) {
					max = j;
				}
			}
			return max;
	}	
	
	public static float calculateAvg(int[] intArray) {
		
			float sum = 0;
			float avg = 0;
			
			for (int j=0; j<=intArray.length; j++) {
				sum += j;
			}
			avg = sum / intArray.length;
			
			return avg;
	}
	public static int calculateSum(int[] intArray) {
		
			int sum = 0;
			
			for (int j=0; j<=intArray.length; j++) {
				sum += j;
			}
			return sum;
	}
	public static int calculatePercentile(String operation, int[] intArray) {
			
			String percent = operation.substring(1, 3);
			int percentInt = Integer.parseInt(percent);
			
			int length = -1;
			
			for (int j=0; j<=intArray.length; j++) {
				length ++;
			}
			float percentile = (((float)percentInt / 100) * length);
			int result = intArray[(int)percentile - 1];
			
			return result;
	}
}

	
	

