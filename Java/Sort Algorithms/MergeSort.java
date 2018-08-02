
public class MergeSort {

	public static void mergeSort (int[]list) {

		if (list.length > 1) {
			// Sort the first half of the list
			int[] firstHalf = new int [list.length / 2];
			System.arraycopy(list, 0 ,firstHalf ,0 ,list.length / 2);
			mergeSort(firstHalf);
			// Sort the second half of the list
			int secondHalfLength = list.length - list.length / 2;
			int[] secondHalf = new int [secondHalfLength];
			System.arraycopy(list, list.length / 2, secondHalf, 0,
					secondHalfLength);
			// Merge the first half of the list with the second half of the list
			merge(firstHalf, secondHalf, list);
		}
	}
	// Merge two lists that have been sorted
	public static void merge (int[] list1, int[] list2, int[] temp) {
		int current1 = 0; // Current index in list1
		int current2 = 0; // Current index in list2
		int current3 = 0; // Current index in temp
		while (current1 < list1.length && current2 < list2.length) {
			if (list1[current1] < list2[current2])
				temp[current3++] = list1[current1++];
			else
				temp[current3++] = list2[current2++];
		}
		while (current1 < list1.length)
			temp[current3++] = list1[current1++];
		while (current2 < list2.length)
			temp[current3++] = list2[current2++];
	}
}
