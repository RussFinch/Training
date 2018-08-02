
public class errors {

	public static void main (String[] args) {
	
		System.out.println("Welcome to my first program!\n");  //Compile error "insert ';'.
		
		String ageStr = "24";  //Runtime Exception.  cannot parse string "years" into integer.
		int age = Integer.parseInt(ageStr);
		System.out.println("I'm " + age + " years old.");
      
		int three = 3;  //Compile error. integer variable value does not require " ".
	    int answerYears = age + three;
		System.out.println("Toal number of years: " + answerYears);
		
		int answerMonths = answerYears * 12; 
		// Logical error.  6 months not included in calculation.
		System.out.println("In 3 years and 6 months, I'll be " + (answerMonths + 6) + " months old");
		
		//Once you've corrected all the errors, the answer should be 330.
	}

}