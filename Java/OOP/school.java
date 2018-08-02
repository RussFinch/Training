
public class school {
	
   public static void main (String [] args) {
   
      student sally = new student("Sally", 15, 8, 'D');
      student sipho = new student("Sipho", 17 , 11, 'A');
      student rajesh = new student("Rajesh", 19, 12, 'B');
      
      teacher russell = new teacher("Russell", "Computer Science", "Full Time", 40, "ACH14526");
      teacher heather = new teacher("Heather", "Maths", "Part Time", 36, "THSO79302");
      teacher mark = new teacher("Mark", "Electronics", "Contractor", 40, "KVUR098235");
      
      secretary ralph = new secretary("Ralph", "Heather", "Part Time", 28, "KFOT23409");
      
      System.out.println("Students:\n");
      System.out.println(sally.toString() + "\n");
      System.out.println(sipho.toString() + "\n");
      System.out.println(rajesh.toString());
      
      System.out.println("\nTeachers:\n");
      System.out.println(russell.toString() + "\n");
      System.out.println(heather.toString() + "\n");
      System.out.println(mark.toString());
      
      System.out.println("\nSecretaries:\n");
      System.out.println(ralph.toString() + "\n");
  
   }
}