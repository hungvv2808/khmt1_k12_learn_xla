import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.WritableRaster;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;

public class ConvertImageToByte {
    public static byte[] getByteImg(BufferedImage src) throws IOException {
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ImageIO.write(src, "jpg", bos );
        return bos.toByteArray();
    }

    public static BufferedImage getGrayscaleImage(BufferedImage src) {
        BufferedImage gImg = new BufferedImage(src.getWidth(), src.getHeight(),
                BufferedImage.TYPE_BYTE_GRAY);
        WritableRaster wr = src.getRaster();
        WritableRaster gr = gImg.getRaster();
        for(int i=0;i<wr.getWidth();i++){
            for(int j=0;j<wr.getHeight();j++){
                gr.setSample(i, j, 0, wr.getSample(i, j, 0));
            }
        }
        gImg.setData(gr);
        return gImg;
    }

    public static BufferedImage equalize(BufferedImage src){
        BufferedImage nImg = new BufferedImage(src.getWidth(), src.getHeight(),
                BufferedImage.TYPE_BYTE_GRAY);
        WritableRaster wr = src.getRaster();
        WritableRaster er = nImg.getRaster();
        int totpix= wr.getWidth()*wr.getHeight();
        int[] histogram = new int[256];

        for (int x = 0; x < wr.getWidth(); x++) {
            for (int y = 0; y < wr.getHeight(); y++) {
                histogram[wr.getSample(x, y, 0)]++;
            }
        }

        int[] chistogram = new int[256];
        chistogram[0] = histogram[0];
        for(int i=1;i<256;i++){
            chistogram[i] = chistogram[i-1] + histogram[i];
        }

        float[] arr = new float[256];
        for(int i=0;i<256;i++){
            arr[i] =  (float)((chistogram[i]*255.0)/(float)totpix);
        }

        for (int x = 0; x < wr.getWidth(); x++) {
            for (int y = 0; y < wr.getHeight(); y++) {
                int nVal = (int) arr[wr.getSample(x, y, 0)];
                er.setSample(x, y, 0, nVal);
            }
        }
        nImg.setData(er);
        return nImg;
    }

    public static void draw(ImageIcon imageIconInsert, String name) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                JFrame editorFrame = new JFrame(name);
                editorFrame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
                JLabel jLabel = new JLabel();
                jLabel.setIcon(imageIconInsert);
                editorFrame.getContentPane().add(jLabel, BorderLayout.CENTER);

                editorFrame.pack();
                editorFrame.setLocationRelativeTo(null);
                editorFrame.setVisible(true);
            }
        });
    }

    public static void sleep() {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException ie) {
            System.out.println(ie);
        }
    }

    private static void printHistogram(byte[] array, String name) {
        System.out.println(name);
        for (int range = 0; range < array.length; range++) {
            String label = range + " : ";
            System.out.println(label + convertToStars(array[range]));
        }
        System.out.println();
    }

    private static String convertToStars(int num) {
        StringBuilder builder = new StringBuilder();
        for (int j = 0; j < num; j++) {
            builder.append('*');
        }
        return builder.toString();
    }

    public static byte[] brightness(BufferedImage src, byte[] defaultList, int value) {
        WritableRaster wr = src.getRaster();
        byte[] newList = new byte[defaultList.length];
        for (int x = 0; x < wr.getWidth(); x++) {
            for (int y = 0; y < wr.getHeight(); y++) {
                newList[wr.getSample(x, y, 0)] += value;
            }
        }
        return newList;
    }

    public static byte[] contrast(BufferedImage src, byte[] defaultList, int brightness, int contrasts) {
        WritableRaster wr = src.getRaster();
        byte[] newList = new byte[defaultList.length];
        for (int x = 0; x < wr.getWidth(); x++) {
            for (int y = 0; y < wr.getHeight(); y++) {
                newList[wr.getSample(x, y, 0)] = (byte) (defaultList[wr.getSample(x, y, 0)] * contrasts + brightness);
            }
        }
        return newList;
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        String path = "/Users/vuhung/Documents/XuLyAnh/Histogram/src/girl.jpg";
        BufferedImage beforeImg = ImageIO.read(new File(path));

        /* Exercise 2 */
        // first image
        byte[] dataBefore = getByteImg(beforeImg);
        ImageIcon imageBefore = new ImageIcon(dataBefore);
        draw(imageBefore, "Exercise 2: Before image");
        printHistogram(dataBefore, "Before byte:");
        sleep();

        // grey image
        BufferedImage greyImg = getGrayscaleImage(beforeImg);
        byte[] dataGrey = getByteImg(greyImg);
        ImageIcon imageGrey = new ImageIcon(dataGrey);
        draw(imageGrey, "Exercise 2: Grey image");
        printHistogram(dataGrey, "Grey byte:");
        sleep();

        // equalize image
        BufferedImage equalizeImg = equalize(beforeImg);
        byte[] dataEqualize = getByteImg(equalizeImg);
        ImageIcon imageEqualize = new ImageIcon(dataEqualize);
        draw(imageEqualize, "Exercise 2: Equalize image");
        printHistogram(dataBefore, "Equalize byte:");
        sleep();

        /* Exercise 3 */
        byte[] brightnessPlus = brightness(beforeImg, dataBefore, 10);
        ImageIcon brightness = new ImageIcon(brightnessPlus);
        draw(brightness, "Exercise 3: Brightness change plus 10");
        sleep();

        byte[] brightnessMinus = brightness(beforeImg, dataBefore, -10);
        ImageIcon brightnessMinuss = new ImageIcon(brightnessMinus);
        draw(brightnessMinuss, "Exercise 3: Brightness change minus 10");
        sleep();

        /* Exercise 4 */
        byte[] contrasts = contrast(beforeImg, dataBefore, 10, 20);
        ImageIcon brightnessContrasts = new ImageIcon(contrasts);
        draw(brightness, "Exercise 4: Brightness contrasts");
        sleep();
    }
}
