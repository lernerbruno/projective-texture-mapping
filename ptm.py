import cv2
import numpy as np
import matplotlib.pyplot as plt

baseImg = cv2.imread("base.jpg")
textureImg = cv2.imread("texture.png")

bRows,bCols,ch = baseImg.shape
tRows,tCols,ch = textureImg.shape

bImgPts = np.float32([[617,685],[1029,685],[1000,1600],[588,1600]])
tImgPts = np.float32([[0,0],[tCols,0],[tCols,tRows],[0,tRows]])

M = cv2.getPerspectiveTransform(tImgPts, bImgPts)
dst = cv2.warpPerspective(textureImg,M,(bRows,bCols))

plt.subplot(121),plt.imshow(textureImg),plt.title('Texture')
plt.subplot(122),plt.imshow(dst),plt.title('Base image')
plt.show()