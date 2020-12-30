import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_pyplot(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(img, (3, 3), 0)

    image_arr = [img, gray, gauss]
    for i in range(len(image_arr)):
        plt.subplot(2, 2, i + 1)
        plt.imshow(image_arr[i])

    plt.subplot(2, 2, len(image_arr) + 1)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')

    plt.show()
    cv2.destroyWindow()


if __name__ == '__main__':
    display_pyplot('girl.jpg')
