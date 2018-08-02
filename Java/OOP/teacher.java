
public class teacher {

	// Attributes
   String name;
   String subject;
   String employmentType;
   int age;
   String idNumber;
	
	// Methods
   public teacher(String name, String subject, String employmentType, int age, String idNumber) {
      this.name = name;
      this.subject = subject;
      this.employmentType = employmentType;
      this.age = age;
      this.idNumber = idNumber;
   }

   public String getName() {
      return name;
   }

   public String toString() {
      String output = "Name: " + name;
      output += "\nAge:" + age;
      output += "\nSubject:" + subject;
      output += "\nEmployment Type:" + employmentType;
      output += "\nID Number:" + idNumber;
   
      return output;
   }

}