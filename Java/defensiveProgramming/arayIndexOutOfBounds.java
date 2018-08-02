
import java.util.Scanner;
import java.util.Random;

public class arayIndexOutOfBounds {

	public static void main(String[] args) {
	
		Scanner userInput = new Scanner(System.in);
		
		System.out.println("Please enter the number of Array Element:");
		int arrayElementNo = userInput.nextInt();
		
		try {
			int result = integerArray(arrayElementNo);
			System.out.println("The requested array element contains:  " + result + "\n");
		}
		
		catch (IndexOutOfBoundsException exception) {
			System.out.println("Exception:  Out of Bounds:  Please enter a number between 0 and 99.\n");	
		}
		
		userInput.close();
		System.out.println("Please make another request....");
	}
	
	private static int integerArray (int arrayElement) {

		Random random = new Random();
		
		if (arrayElement >= 100)
			throw new IndexOutOfBoundsException ("Array element out of bounds");
		
		int[] intArray = new int[100];
		for (int i = 0; i < intArray.length; i++) {
			intArray[i] = random.nextInt();
		}
		
		return intArray[arrayElement];
		
	}	
}
