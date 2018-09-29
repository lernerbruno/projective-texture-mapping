import cv2
import numpy as np
import matplotlib.pyplot as plt

baseImg = cv2.imread("base.jpg")
textureImg = cv2.imread("texture.png")

bRows,bCols,ch = baseImg.shape
tRows,tCols,ch = textureImg.shape
print bRows, bCols
bImgPts = np.float32([[517,585],[1029,685],[1000,1600],[588,1600]])
tImgPts = np.float32([[0,0],[tCols,0],[tCols,tRows],[0,tRows]])
M = cv2.getPerspectiveTransform(bImgPts,tImgPts)
print "Transformation Matrix"
print M
print bImgPts[0][0]
# Para cada ponto da imagem base, verificar se a transformada dele pertence ao suporte da textura
for i in range(bRows):
    for j in range(bCols):
        xT = M[0][0]*i + M[0][1]*j + M[0][2]
        yT = M[1][0]*i + M[1][1]*j + M[1][2]
        if (xT > 0 and xT < tRows) and (yT > 0 and yT < tCols):
            print i,j
            print baseImg[i][j], textureImg[int(xT)][int(yT)]
            baseImg[i][j] = textureImg[int(xT)][int(yT)]
            
        

# Caso pertenca, substituir os pixels


# dst = cv2.warpPerspective(bImgPts,M,(tCols,tRows))

plt.subplot(121),plt.imshow(baseImg),plt.title('Texture')
# plt.subplot(122),plt.imshow(dst),plt.title('Base image')
plt.show()