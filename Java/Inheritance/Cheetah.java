
public class Cheetah extends Animal {

	public Cheetah(int numTeeth, boolean spots, int weight) {
		super(numTeeth, spots, weight);
	}
	
	public String toString() {
		System.out.println("----Cheetah----");
		String output = "Number of Teeth: " + getNumTeeth();
		output += "\nSpots:" + getSpots();
		output += "\nWeight:" + getWeight();
		
	return output;
	}
}
