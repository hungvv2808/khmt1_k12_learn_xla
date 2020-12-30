import cv2
import numpy as np
from matplotlib import pyplot as plt


class template:
    def __init__(self, image_path="img/girl.jpg"):
        self.image_path = image_path
        self.img = cv2.imread(self.image_path)

    def original(self):
        return self.img

    def gray(self):
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def histogram(self):
        """
        .flatten(): Trả về một bản sao của mảng được thu gọn thành một chiều.
        """
        return self.img.flatten()

    def equalization_histogram_chart(self):
        img = self.img
        hist, bins = np.histogram(img.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()
        return cdf_normalized

    def equalization_histogram_image(self):
        img = template.gray(self)
        return cv2.equalizeHist(img)

    def gaussian(self):
        gray = template.gray(self)
        img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
        return img_gaussian

    def sobel(self):
        img_gaussian = template.gaussian(self)
        img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
        img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
        return np.abs(img_sobelx) + np.abs(img_sobely)

    def prewitt(self):
        img_gaussian = template.gaussian(self)
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
        img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
        return np.abs(img_prewittx) + np.abs(img_prewitty)

    def laplacien(self):
        img_gaussian = template.gaussian(self)
        k_lap_positif = np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0]), np.float32)
        k_lap_negatif = np.array(([0, -1, 0], [-1, 4, -1], [0, -1, 0]), np.float32)
        output_k_lap_positif = cv2.filter2D(img_gaussian, -1, k_lap_positif)
        output_k_lap_negatif = cv2.filter2D(img_gaussian, -1, k_lap_negatif)
        return np.abs(output_k_lap_positif) + np.abs(output_k_lap_negatif)


if __name__ == '__main__':
    tmp = template()

    cv2.imshow('Original image', tmp.original())
    cv2.waitKey(0)
    cv2.imshow('Gray image', tmp.gray())
    cv2.waitKey(0)
    cv2.imshow('Gauss', tmp.gaussian())
    cv2.waitKey(0)
    cv2.imshow('Sobel', tmp.sobel())
    cv2.waitKey(0)
    cv2.imshow('Prewitt', tmp.prewitt())
    cv2.waitKey(0)
    cv2.imshow('Laplacien', tmp.laplacien())
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plt.hist(tmp.histogram(), 256, [0, 256], color='r')
    plt.waitforbuttonpress(0)
    plt.close()
    plt.plot(tmp.equalization_histogram_chart())
    plt.waitforbuttonpress(0)
    plt.close()
    cv2.imshow('Histogram equalization', tmp.equalization_histogram_image())
    cv2.waitKey(0)

    # get all
    fig, axs = plt.subplots(3, 3)
    fig.suptitle('Group 3 - Research OpenCV', fontsize=16)

    axs[0, 0].imshow(tmp.original())
    axs[0, 0].set_title("Original image")

    axs[0, 1].imshow(tmp.gray())
    axs[0, 1].set_title("Gray image")

    axs[0, 2].imshow(tmp.gaussian())
    axs[0, 2].set_title("Gaussian image")

    axs[1, 0].imshow(tmp.sobel())
    axs[1, 0].set_title("Sobel image")

    axs[1, 1].imshow(tmp.prewitt())
    axs[1, 1].set_title("Prewitt image")

    axs[1, 2].imshow(tmp.laplacien())
    axs[1, 2].set_title("Laplacien image")

    axs[2, 0].hist(tmp.histogram(), 256, [0, 256], color='r')
    axs[2, 0].set_title("Histogram")

    axs[2, 1].plot(tmp.equalization_histogram_chart())
    axs[2, 1].set_title("Equalization histogram chart")

    axs[2, 2].imshow(tmp.equalization_histogram_image())
    axs[2, 2].set_title("Equalization histogram image")

    fig.tight_layout()
    plt.show()
    plt.waitforbuttonpress(0)
    plt.close()
