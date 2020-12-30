package vn.com.nns.traceability.controller;

public class RunLength {
//    public static void runLengthEx(String str)
//    {
//        for (int i = 0; i < str.length(); i++) {
//            int count = 1;
//            while (i < str.length() - 1 && str.charAt(i) == str.charAt(i + 1)) {
//                count+=1;
//                i+=1;
//            }
//            System.out.print(str.charAt(i));
//            System.out.print(count);
//        }
//    }
//
    public static void main(String[] args)
    {
//        String str = "hhhhuuuuunnnnngggggvvvvvv";
//        runLengthEx(str);

    }

    private void printHistogram(int[] array) {
        for (int range = 0; range < array.length; range++) {
            String label = range + " : ";
            System.out.println(label + convertToStars(array[range]));
        }
    }

    private String convertToStars(int num) {
        StringBuilder builder = new StringBuilder();
        for (int j = 0; j < num; j++) {
            builder.append('*');
        }
        return builder.toString();
    }
}
