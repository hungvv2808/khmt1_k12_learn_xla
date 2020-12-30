import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Histogram {
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        Integer[] intArr = input();
        printHistogram(intArr);
    }

    private static Integer[] input() {
        List<Integer> integerList = new ArrayList<>();
        System.out.print("Enter size array: ");
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("array[" + i + "] = ");
            Integer tmp = scanner.nextInt();
            integerList.add(tmp);
        }

        Object[] objects = integerList.toArray();
        Integer[] intArr = new Integer[objects.length];

        for (int i = 0; i < objects.length; i++) {
            intArr[i] = (Integer) objects[i];
        }
        return intArr;
    }

    private static void printHistogram(Integer[] array) {
        for (int range = 0; range < array.length; range++) {
            String label = range + " : ";
            System.out.println(label + convertToStars(array[range]));
        }
    }

    private static String convertToStars(int num) {
        StringBuilder builder = new StringBuilder();
        for (int j = 0; j < num; j++) {
            builder.append('*');
        }
        return builder.toString();
    }
}
