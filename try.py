import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("assets/mikasa.jpg")
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()


# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
#     print("exit without saving.")
# if k == ord('s'):
#     cv2.imwrite('mikasa_saved.jpg', img)
#     cv2.destroyAllWindows()
#     print("saved new image.")
