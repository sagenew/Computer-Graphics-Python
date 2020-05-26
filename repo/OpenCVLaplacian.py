import cv2
import numpy as np
from matplotlib import pyplot as plt

img  = cv2.imread('images/profile.jpg')

output = cv2.Laplacian(img,-1)

plt.imshow(output)
plt.show()
