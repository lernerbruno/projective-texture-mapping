import cv2
import numpy as np
import matplotlib.pyplot as plt

baseImg = cv2.imread("base.jpg")
textureImg = cv2.imread("texture.png")
bRows,bCols,ch = baseImg.shape
tRows,tCols,ch = textureImg.shape
print ch
print bRows, bCols
bImgPts = np.float32([[696.78,615.42],[696.78,1008.342],[1640.04,984.672],[1630.56,577.548]])
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
            
        
plt.imshow(baseImg),plt.title('Texture in base image')
plt.show()