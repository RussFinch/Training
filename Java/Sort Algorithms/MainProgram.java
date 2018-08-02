
public class MainProgram {

	public static void main(String[] args) {
		
		int[] testIntArray = {5, 2, 9, 3, 8, 4, 0, 1, 6, 7};
		
//		int[] result = SelectionSort.selectionSort(testIntArray);
//		System.out.println("End of Selection Sort");
		
//		InsertionSort.insertionSort(testIntArray);
//		System.out.println("End of Insertion Sort");

//		BubbleSort.bubbleSort(testIntArray);
//		System.out.println("End of Bubble Sort");
		
//		MergeSort.mergeSort(testIntArray);
//		System.out.println("End of Merge Sort");
		
//		QuickSort.quickSort(testIntArray);
//		System.out.println("End of Quick Sort");
		
		QuickSortTemp.quickSort(testIntArray);
		System.out.println("End of Quick Sort");
	}

}
