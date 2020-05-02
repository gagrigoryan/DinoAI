import time
import mss
import numpy as np
import cv2
import pyautogui as pg


BOX_COORD = {'left': 260, 'top': 280, 'width': 50, 'height': 35}


def processing_img(src_img):
    processed_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=200)
    return processed_img


def screen_record():
    sct = mss.mss()
    last_time = time.time()

    while True:
        img = np.array(sct.grab(BOX_COORD))
        processed_img = processing_img(img)
        mean = np.mean(processed_img)
        print('mean =', mean)

        if mean != float(0):
            pg.press('space')
            continue
        print('screen processed for {} sec'.format(time.time() - last_time))
        last_time = time.time()


if __name__ == '__main__':
    screen_record()