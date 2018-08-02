
public class Lion extends Animal {
	
	private boolean mane = false;
	private String type = "";
			
	public Lion(int numTeeth, boolean spots, int weight) {
		super (numTeeth, spots, weight);	
			if (super.getWeight() <= 80) {
				type = "Cub";
			}
			else if (super.getWeight() >= 120) {
				type = "Male";
				mane = true;
			}
			else {
				type = "Female";
			}
	}
	public String toString() {
		System.out.println("----Lion----");
		String output = "Number of Teeth: " + getNumTeeth();
		output += "\nSpots:" + getSpots();
		output += "\nWeight:" + getWeight();
		output += "\nType:" + type;
		output += "\nMane:" + mane;
		   
		return output;
	}
}
