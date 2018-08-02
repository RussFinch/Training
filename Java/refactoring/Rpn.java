public class Rpn {

  public String calculationString;
  
  public Rpn(String userCalculation) {
	    RpnStack.top = null;   //required to run second calculation with program restart.
	    this.calculationString = userCalculation;
	  }
  
  public double answer() {
    double a;
    double b;
    int j;

    for (int i = 0; i < calculationString.length(); i++) {
      // if character of calculationString is numeric
      if (Character.isDigit(calculationString.charAt(i))) {   
    	String digitStringVar = "";
    	double digitDoubleVar;
    	// create a string of the first number in the calculation
    	for (j = 0; (j < 100) && (Character.isDigit(calculationString.charAt(i))
                             || (calculationString.charAt(i) == '.')); j++, i++) {
          digitStringVar = digitStringVar + String.valueOf(calculationString.charAt(i));
        }
        // convert to double and add to the stack
        digitDoubleVar = Double.parseDouble(digitStringVar);
        RpnStack.intoRpnStack(digitDoubleVar);
      } else if (calculationString.charAt(i) == '+') {
        b = RpnStack.outOfRpnStack();
        a = RpnStack.outOfRpnStack();
        RpnStack.intoRpnStack(a + b);
      } else if (calculationString.charAt(i) == '-') {
        b = RpnStack.outOfRpnStack();
        a = RpnStack.outOfRpnStack();
        RpnStack.intoRpnStack(a - b);
      } else if (calculationString.charAt(i) == '*') {
        b = RpnStack.outOfRpnStack();
        a = RpnStack.outOfRpnStack();
        RpnStack.intoRpnStack(a * b);
      } else if (calculationString.charAt(i) == '/') {
        b = RpnStack.outOfRpnStack();
        a = RpnStack.outOfRpnStack();
        RpnStack.intoRpnStack(a / b);
      } else if (calculationString.charAt(i) == '^') {
        b = RpnStack.outOfRpnStack();
        a = RpnStack.outOfRpnStack();
        RpnStack.intoRpnStack(Math.pow(a, b));
      } else if (calculationString.charAt(i) != ' ') {
        throw new IllegalArgumentException("Illegal character");
      }
    }
    return RpnStack.outOfRpnStack();
  }
}