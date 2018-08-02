/*	Create a new file called rockPaperScissors.java
 * 
	Write a program that allows the user to play the rock, paper, scissors game.
	
	The program should randomly generate a number 0, 1, 2, which represents scissors,
	rock and paper respectively.
	
	The program should then prompt the user to enter a number 0, 1, 2.
	
	Once the user has entered their number the program should inform them whether they
	win, lose or draw.
	
	The rules of the game are as follows:
		○ Scissors beats paper
		○ Rock beats scissors
		○ Paper beats rock
*/

import java.util.Random;
import java.util.Scanner;

public class rockPaperScissors 
{
	public static void main(String[] args)
	{

		String userHand = "";           
	    String computerHand = "";   
	    int computerInt;           
	    
	    Random numberGenerator = new Random();
	    computerInt = numberGenerator.nextInt(3);
	    if (computerInt == 0) 
	       computerHand = "R"; 
	    else if (computerInt == 1) 
	       computerHand = "P"; 
	    else if (computerInt == 2) 
	       computerHand = "S"; 
	    
	    System.out.println("Rock = R\n" + "Paper = P\n" + "Scissors = S\n"
	    					+ "\n" + "\nShow your Hand:  ");
	    
	    Scanner userInput = new Scanner(System.in);
	    userHand = userInput.next();
	    userHand = userHand.toUpperCase(); 
	    userInput.close();

	    System.out.println("Computer play is: " + computerHand); 

	    if (userHand.equals(computerHand)) 
	    {
	       System.out.println("It's a Tie!"); 
	    }
	    else if (userHand.equals("R")) 
	    {
	        if (computerHand.equals("S")) 
	          System.out.println("Rock blunts scissors. You Win.");
	        if (computerHand.equals("P"))
	    	  System.out.println("Paper wraps Rock, You Lose.");
	    }
	    else if (userHand.equals("P")) 
	    {
	    	if (computerHand.equals("R"))
	    		System.out.println("Paper wraps Rock, You Win.");
	    	if (computerHand.equals("S"))
	    		System.out.println("Scissors cuts Paper, You Lose.");
	    }
	    else if (userHand.equals("S")) 
	    {
	    	if (computerHand.equals("P"))
	    		System.out.println("Scissors cuts Paper, You Win.");
	    	if (computerHand.equals("R"))
	    		System.out.println("Rock blunts scissors. You Lose.");
	    }
	}
}
