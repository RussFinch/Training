		
public class SelectionSort {
	
	public static int[] selectionSort (int[] list) {
						
		for (int i = 0; i < list.length - 1; i++) {
			// Find the minimum number in the list
			double currentMin = list[i];
			int currentMinIndex = i;
				for (int j = i+1; j < list.length; j++){
					if (currentMin > list[j]) {
						currentMin = list[j];
						currentMinIndex = j;
					}
				}
			// Swap the minimum number with the next unsorted number
			if (currentMinIndex != i) {
				list[currentMinIndex] = list[i];
				list[i] = (int)currentMin;
			}
		}
		return list;
	}
}
