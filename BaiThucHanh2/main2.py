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

    def gaussian(self):
        gray = template.gray(self)
        img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
        return img_gaussian

    def sobel(self):
        img_gaussian = template.gaussian(self)
        img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
        img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
        return np.abs(img_sobelx) + np.abs(img_sobely)


if __name__ == '__main__':
    tmp = template()

    # get all
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].imshow(tmp.original())
    axs[0, 0].set_title("Original image")

    axs[0, 1].imshow(tmp.gray())
    axs[0, 1].set_title("Gray image")

    axs[1, 0].imshow(tmp.gaussian())
    axs[1, 0].set_title("Gaussian image")

    axs[1, 1].imshow(tmp.sobel())
    axs[1, 1].set_title("Sobel image")

    fig.tight_layout()
    plt.show()
    plt.waitforbuttonpress(0)
    plt.close()
