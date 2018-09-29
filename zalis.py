import cv2
import numpy as np
import matplotlib.pyplot as plt

zalisMetro = cv2.imread("zalisMetro.png")
zalisTextura1 = cv2.imread("zalisTextura1.png")
zalisTextura2 = cv2.imread("zalisTextura2.png")

bRows,bCols,ch = zalisMetro.shape
t1Rows,t1Cols,ch = zalisTextura1.shape
t2Rows,t2Cols,ch = zalisTextura2.shape
print bRows, bCols
b1ImgPts = np.float32([[170.64,467.478],[170.64,708.3],[876.9,665.802],[872.16,434.424]])
b2ImgPts = np.float32([[170.64,769.686],[175.38,987],[886.38,939.678],[881.64,708.3]])
t1ImgPts = np.float32([[0,0],[0,t1Cols],[t1Rows,t1Cols],[t1Rows,0]])
t2ImgPts = np.float32([[0,0],[0,t2Cols],[t2Rows,t2Cols],[t2Rows,0]])

M1 = cv2.getPerspectiveTransform(b1ImgPts,t1ImgPts)
print "Transformation Matrix"
print M1

M2 = cv2.getPerspectiveTransform(b2ImgPts,t2ImgPts)
print "Transformation Matrix"
print M2

# Para cada ponto da imagem base, verificar se a transformada dele pertence ao suporte da textura
for i in range(bRows):
    for j in range(bCols):
        xT = (M1[0][0]*i + M1[0][1]*j + M1[0][2])/(M1[2][0]*i + M1[2][1]*j + M1[2][2]) 
        yT = (M1[1][0]*i + M1[1][1]*j + M1[1][2])/ (M1[2][0]*i + M1[2][1]*j + M1[2][2]) 
        if (xT > 0 and xT < t1Rows) and (yT > 0 and yT < t1Cols):
            zalisMetro[i][j] = zalisTextura1[int(xT)][int(yT)]
         
# Para cada ponto da imagem base, verificar se a transformada dele pertence ao suporte da textura
for i in range(bRows):
    for j in range(bCols):
        xT = (M2[0][0]*i + M2[0][1]*j + M2[0][2])/(M2[2][0]*i + M2[2][1]*j + M2[2][2]) 
        yT = (M2[1][0]*i + M2[1][1]*j + M2[1][2])/ (M2[2][0]*i + M2[2][1]*j + M2[2][2]) 
        if (xT > 0 and xT < t2Rows) and (yT > 0 and yT < t2Cols):
            zalisMetro[i][j] = zalisTextura2[int(xT)][int(yT)]
         
RGB_img = cv2.cvtColor(zalisMetro, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img),plt.title('Zalis no metro')
plt.show()