import cv2
import numpy as np
import matplotlib.pyplot as plt

# Codeblock 2
SCALE = 3
PAPER_W = 210 * SCALE
PAPER_H = 297 * SCALE

# Codeblock 3
def load_image(path, scale=0.7):
    img = cv2.imread(path)
    img_resized = cv2.resize(img, (0,0), None, scale, scale)
    return img_resized

def show_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(6,8))
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img)
    plt.show()

# Codeblock 4
img_original = load_image(path='1.jpg')
show_image(img_original)
print(img_original.shape)