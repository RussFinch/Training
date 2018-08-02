

public class QuickSortMedian {

    public static void quickSort (int[] list) {

        quickSort(list,0,list.length - 1);
    }

    public static void quickSort (int[] list, int first, int last) {

        if (last > first) {
            int median = medianCalc(list, first, last);
            int pivotIndex = partition(list, first, last, median);
            quickSort(list, first, pivotIndex - 1);
            quickSort(list ,pivotIndex + 1 ,last);
        }
    }

    public static int partition (int[] list, int first, int last, int pivot) {

        int low = first;
        int high = last - 1;

        while (low < high) {
            while (low <= high && list[low] < pivot)
                low++;
            while (low <= high && list[high] >= pivot)
                high--;
            if (low < high) {
                swap(list, low, high);
            }
        }
        swap(list, low, last - 1);
        return low;
    }

    public static int medianCalc (int[] list, int first, int last) {

        int middle = (first + last) /2;

        if (list[first] > list[middle]) {
            swap(list, first, middle);
        }
        if (list[first] > list[last]) {
            swap(list, first, last);
        }
        if (list[middle] > list[last]) {
            swap(list, middle, last);
        }
        swap(list, middle, last -1);
        return list[last - 1];
    }

    public static void swap(int[] list, int index1, int index2) {

        int temp = list[index1];
        list[index1] = list[index2];
        list[index2] = temp;
    }
}