import math
import cv2
import numpy as np
from skimage.feature import local_binary_pattern  # # pip install scikit-image

KERNEL_WIDTH = 7
KERNEL_HEIGHT = 7
SIGMA_X = 3
SIGMA_Y = 3


def main():
    img = cv2.imread('img/girl.jpg', cv2.IMREAD_GRAYSCALE)

    # LBP
    out = local_binary_pattern(image=img, P=8, R=1, method='default')
    cv2.imwrite('lbp.jpg', out)
    cv2.imshow('lbp image', out)
    cv2.waitKey(0)
    print("Saved image @ lbp.jpg")

    # Gaussian blur + LBP
    blur_img = cv2.GaussianBlur(img, ksize=(KERNEL_WIDTH, KERNEL_HEIGHT), sigmaX=SIGMA_X, sigmaY=SIGMA_Y)
    blur_out = local_binary_pattern(image=blur_img, P=8, R=1, method='default')
    cv2.imwrite('blur.jpg', blur_img)
    cv2.imshow('blur image', blur_img)
    cv2.waitKey(0)

    cv2.imwrite('blur_lbp.jpg', blur_out)
    cv2.imshow('blur lbp image', blur_out)
    cv2.waitKey(0)
    print("Saved image @ blur.jpg")
    print("Saved image @ blur_lbp.jpg")
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
