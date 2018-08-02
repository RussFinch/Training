
import java.util.Scanner;

public class hexToDecimalException {
	
	public static void main (String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		// Prompt the user to enter a string
		System.out.print("Enter a hex number: ");
		String hex = input.nextLine();
		
		try {
			System.out.println("The decimal value for hex number " + hex +
									" is " + hexToDecimal(hex.toUpperCase()));
		}
		catch (IllegalArgumentException exception) {
			System.out.println("Hex input improperly formatted 0-9, A-F. Input character Out of Bounds: ");
		}
		
		System.out.println("Please try again...");
		input.close();
	}

	public static int hexToDecimal(String hex) {

		int decimalValue = 0;
		
		for (int i = 0; i < hex.length(); i ++) {
			char hexChar = hex.charAt(i);
				if (hexChar >= 'A' && hexChar <= 'F' || hexChar >= '0' && hexChar <= '9')
					decimalValue = decimalValue * 16 + hexCharToDecimal(hexChar);
				else
					throw new IllegalArgumentException("input character Out of Bounds: ");
		}
		return decimalValue ;
	}

	public static int hexCharToDecimal(char ch) {

		if (ch >= 'A' && ch <= 'F')
			return 10 + ch - 'A' ;
		else // ch is '0', '1', ..., or '9'
			return ch - '0' ;			
	}
}