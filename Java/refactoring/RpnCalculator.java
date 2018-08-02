import java.util.Scanner;

class RpnCalculator {	

  public static void main(String[] args) {
    
    Scanner input = new Scanner(System.in);

    while (true) {
      System.out.println("Enter RPN expression or \"quit\".");
      String userCalculation = input.nextLine();
      if ((userCalculation.equals("quit")) || (userCalculation.equals(""))) {
        input.close();
        break;
        
      } else {
        try {
          Rpn calculation = new Rpn(userCalculation);
          System.out.printf("Answer is %f\n", calculation.answer());
        } catch (IllegalArgumentException exception) {
          System.out.println("An illegal charater has been input");
        }
      }
    }
    input.close();  
  }
}