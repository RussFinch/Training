import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class ReorderAscending {
  /**
   * Takes input from an file and outputs every word in
   * ascending alpabetical order 
   */
  public static void main(String[] args) throws FileNotFoundException {
    
	  try {
      Scanner fileInput = new Scanner(new File("/Users/russellfincham/gitprojects/introduction to software engineering/task 20/input.txt"));
      ArrayList<String> wordArrayList = new ArrayList<String>();
      while (fileInput.hasNext()) {
        wordArrayList.add(fileInput.next());
        wordArrayList.sort(String::compareToIgnoreCase);
      }
      System.out.println(wordArrayList);
      fileInput.close();
    }
	  catch (FileNotFoundException exception) {
      System.out.println("File cannot be found...");
    }
  }
}
