
public class recursion {
			
	public static void main(String args[]) {
		
//		System.out.println(reverse("This is a test String using Recursion", ""));
		
//		System.out.println("\n" + factorial(9) + "\n");
		
//		System.out.println(fibonacci(7));
		
//		fibonacciSequence(7);
		
/*		String inputString = "hello world!";
	    String replace = "ll";
	    String replaceWith = "zz";

	    System.out.println(searchReplace(inputString, replace, replaceWith));
*/
	}
	
	
	private static String reverse(String inputString, String reverseString) {
		    
		if (inputString.length() == 0) {
			return reverseString;
		    }
		return reverse(inputString.substring(1), inputString.charAt(0) + reverseString);
	}
	
	
	public static long factorial(int n) { 
	    
		if (n == 1) {
			return 1;
			}
			long result = n * factorial(n-1);
		return result;
	} 
	
	
	private static int fibonacci(int n) {
		
	    if (n == 0) {
	        return 0;
	    	}
	    else if (n <= 2) {   // Fibonacci sequence numbers 1 and 2 both equal 1
	    	return 1;
	    	}
	    else {
	    	return fibonacci(n-1) + fibonacci(n-2);
	    	}
	}
	
	
	private static void fibonacciSequence(int n) {
		
		if (n == 0) {
			System.out.println(fibonacci(0));
			}
		else {
			System.out.println(fibonacci(n));
			fibonacciSequence(n-1);
			}
	}
	
/*	
	private static String searchReplace(String inputString, char replace, char replaceWith) {
		
		if (inputString.length() < 1) {
		      return inputString;
		}
		else {
		   char first = replace == inputString.charAt(0) ? replaceWith : inputString.charAt(0);
		   System.out.println(first);
		   return first + searchReplace(inputString.substring(1), replace, replaceWith);
		   
		} 
	}
*/	
	private static String searchReplace(String inputString, String replace, String replaceWith) {
		
		if (inputString.length() < replace.length()) {
		      return inputString;
		    }

		      String firstSubstring = replace == inputString.substring(0, replace.length()) ? replaceWith : inputString.substring(0, replace.length());
		      System.out.println(firstSubstring);
		      return firstSubstring + searchReplace(inputString.substring(1), replace, replaceWith);
	} 

}

