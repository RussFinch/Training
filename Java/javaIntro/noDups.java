/*
 ● Create a new file called NoDups.java
● Create a method that takes an integer array argument and removes all duplicates from
	the array.
● Test your method by calling it from the class main method with an array argument
	comprising the following elements:
	○ 20,100,10,80,70,1,0,-1,2,10,15,300,7,6,2,18,19,21,9,0.
● Print the array before and after calling the method.
● Compile, save and run your file.

*/
import java.util.Arrays;

public class noDups {

	 public static void main(String[] args) {        
	        
	    	removeDuplicates(new int[] {20, 100, 10, 80, 70, 1, 0, -1, 2, 10, 15, 300, 7, 6, 2, 18, 19, 21, 9, 0});
	    }
	    
		static void removeDuplicates(int[] arrayWithDuplicates) {
			
			System.out.println("Array With Duplicates: ");
	 
	        for (int i = 0; i < arrayWithDuplicates.length; i++) {  
	            System.out.print(arrayWithDuplicates[i]+", ");
	        	}
	        
	        int noOfUniqueElements = arrayWithDuplicates.length;
	        
	        for (int i = 0; i < noOfUniqueElements; i++) {
	            for (int j = i+1; j < noOfUniqueElements; j++) {
	                if(arrayWithDuplicates[i] == arrayWithDuplicates[j]) {
	                    arrayWithDuplicates[j] = arrayWithDuplicates[noOfUniqueElements-1];
	                    noOfUniqueElements--;
	                }
	            }
	        }

	        int[] arrayWithoutDuplicates = Arrays.copyOf(arrayWithDuplicates, noOfUniqueElements);
	        
	        System.out.println();
	        System.out.println("\nArray Without Duplicates : ");
	        System.out.println(Arrays.toString(arrayWithoutDuplicates));
	   } 
}