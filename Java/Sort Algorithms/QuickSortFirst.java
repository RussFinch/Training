
public class QuickSort {

	public static void quickSort (int[] list) {

		quickSort(list, 0, list.length-1);
	}

	public static void quickSort (int[] list, int first, int last) {

		if (last > first) {
			int pivotIndex = partition(list, first, last);
			quickSort(list, first, pivotIndex-1);
			quickSort(list, pivotIndex+1, last);
		}
	}

	public static int partition (int[]list, int first, int last) {

		int middle = first + (last - first) / 2;//Calculate position of middle element.
		int pivot = list[middle]; // Choose the middle element as the pivot.
//		int pivot = list[first]; // Choose the first element as the pivot int
		int low = first; // Index for forward search
		int high = last; // Index for backward search
		while (high > low) {
			// Search forward from left
			while (list[low] <= pivot)
				low++;
			// Search backward from right
			while (list[high] > pivot)
				high--;
			// Swap two elements in the list
			if (high > low) {
				int temp = list[high];
				list[high] = list[low];
				list[low] = temp;
			}
		}
		
		while (high > first && list[high] >= pivot)
			high--;
		// Swap pivot with list[high]
		if (pivot > list[high]) {
			list[first] = list[high];
			list[high] = pivot;
			return high;
		}
		else {
			return first;
		}
	}
}
