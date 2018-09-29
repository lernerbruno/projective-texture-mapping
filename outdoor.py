import cv2
import numpy as np
import matplotlib.pyplot as plt

baseImg = cv2.imread("outdoor.png")
textureImg = cv2.imread("compfrio.png")
bRows,bCols,ch = baseImg.shape
tRows,tCols,ch = textureImg.shape
print ch
print bRows, bCols
bImgPts = np.float32([[224.673,204.76],[58.882,750.896],[322.197,768.234],[389.381,199.342]])
tImgPts = np.float32([[0,0],[0,tCols],[tRows,tCols],[tRows,0]])
M = cv2.getPerspectiveTransform(bImgPts,tImgPts)
print "Transformation Matrix"
print M

# Para cada ponto da imagem base, verificar se a transformada dele pertence ao suporte da textura
for i in range(bRows):
    for j in range(bCols):
        xT = (M[0][0]*i + M[0][1]*j + M[0][2])/(M[2][0]*i + M[2][1]*j + M[2][2]) 
        yT = (M[1][0]*i + M[1][1]*j + M[1][2])/ (M[2][0]*i + M[2][1]*j + M[2][2]) 
        if (xT > 0 and xT < tRows) and (yT > 0 and yT < tCols):
            baseImg[i][j] = textureImg[int(xT)][int(yT)]
            

RGB_img = cv2.cvtColor(baseImg, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img),plt.title('Texture in base image')
plt.show()

