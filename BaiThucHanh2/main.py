import cv2
import numpy as np
from matplotlib import pyplot as plt


class template:
    def __init__(self, image_path="girl.jpg"):
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
        return cdf_normalized.flatten()


if __name__ == '__main__':
    tmp = template()

    # get all
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].imshow(tmp.original())
    axs[0, 0].set_title("Original image")

    axs[0, 1].imshow(tmp.gray())
    axs[0, 1].set_title("Gray image")

    axs[1, 0].hist(tmp.histogram(), color='b', bins=20)
    axs[1, 0].set_title("Histogram")

    axs[1, 1].hist(tmp.equalization_histogram_chart(), color='g', bins=20)
    axs[1, 1].set_title("Equalization histogram chart")

    fig.tight_layout()
    plt.show()
    plt.waitforbuttonpress(0)
    plt.close()
