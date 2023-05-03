import pyautogui
import keyboard

from skimage.color import rgb2gray, gray2rgb, rgb2hsv, rgb2lab, lab2rgb
from matplotlib.pyplot import imshow, show, subplot, title, get_cmap
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage import data, io
import numpy as np

def auto():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'PIC_original.jpg')

    img = imread("PIC_original.jpg")

    img[:200,:] = 0
    img[880:1080,:] = 0
    img[:,:477] = 0
    img[:,1543:] = 0

    imsave('PIC_proccessed.jpg', img)

while True:
    if keyboard.read_key() == "a":
        auto()
        break