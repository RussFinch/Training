
public class secretary {

	// Attributes
   String name;
   String secretaryFor;
   String employmentType;
   int age;
   String idNumber;
	
	// Methods
   public secretary(String name, String secretaryFor, String employmentType, int age, String idNumber) {
      this.name = name;
      this.secretaryFor = secretaryFor;
      this.employmentType = employmentType;
      this.age = age;
      this.idNumber = idNumber;
   }

   public String getName() {
      return name;
   }
	
   public String getSecretaryFor() {
      return secretaryFor;
   }
   
   public String toString() {
      String output = "Name: " + name;
      output += "\nAge:" + age;
      output += "\nSecretary For:" + secretaryFor;
      output += "\nEmployment Type:" + employmentType;
      output += "\nID Number:" + idNumber;
   
      return output;
   }

}
