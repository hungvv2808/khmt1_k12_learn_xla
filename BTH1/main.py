# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import cv2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = cv2.imread('./image.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('./image.jpg', 'photo')
    print(img)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
