import cv2
import matplotlib.pyplot as plt
import numpy as np
from sys import getsizeof
from math import log

# IMAGEM ORIGINAL
img = cv2.imread('landscape.png', cv2.IMREAD_GRAYSCALE)

#img_th = img = np.array([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]])


# LIMIARIZAÇÃO
ret, img_th = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)

# EXIBIÇÃO DAS IMAGENS
cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Imagem Limiarizada', cv2.WINDOW_NORMAL)
cv2.imshow('Imagem Limiarizada', img_th)
cv2.imshow('Imagem Original', img)
cv2.waitKey()

"""
file = open('IMG.txt', 'w')

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		file.write("%d " % img_th[i, j])
		#file.write("%d" % img[i, j])
	file.write('\n')
file.close()

plt.hist(img.ravel(),256,[0,256]);
plt.show()

img_list = img.tolist()
histograma = [0] * 256

for x in range(img.shape[0]):
	for num in range(256):
		histograma[num] += img_list[x].count(num)

prob = []
for i in range(256):
	prob.append(histograma[i] / (img.shape[0] * img.shape[1]))

entropy = 0
for i in range(256):
	entropy -= (prob[i] * log(prob[i], 2))

comp_medio = 0
for i in range(256):
	comp_medio += (prob[i] * 8)

print("\nLm =  %f bits/símbolo" % comp_medio)
print("H(X) = %f bits/símbolo" % entropy)
print("Eficiência = %.2f %%" % (entropy / comp_medio * 100))
print()
"""

RLE = []
RLE_TH = []

# APLICANDO O RLE NA IMAGEM ORIGINAL
j = 0

for i in range(img.shape[0]):
	j = 0
	while(j < img.shape[1]):
		qtd = 0
		pixel = img[i, j]
		while(j < img.shape[1] and pixel == img[i, j]):
			qtd += 1
			j += 1
			#print(j)

		RLE.append(qtd)
		RLE.append(pixel)
	# Indicador de fim da i-ésima linha da imagem
	RLE.append(0)
	RLE.append(0)

# Indicador de fim da imagem
RLE.append(0)
RLE.append(1)

# APLICANDO O RLE NA IMAGEM LIMIARIZADA
j = 0
qtd = 0

for i in range(img_th.shape[0]):
	j = 0
	while(j < img_th.shape[1]):
		qtd = 0
		pixel = img_th[i, j]
		while(j < img_th.shape[1] and pixel == img_th[i, j]):
			qtd += 1
			j += 1
			#print(j)

		RLE_TH.append(qtd)
		RLE_TH.append(pixel)
	# Indicador de fim da i-ésima linha da imagem
	RLE_TH.append(0)
	RLE_TH.append(0)


# Indicador de fim da imagem
RLE_TH.append(0)
RLE_TH.append(1)

RLE_NP = np.asarray(RLE)
RLE_TH_NP = np.asarray(RLE_TH)

print("\n########### IMAGEM ORIGINAL #############")
print("Tamanho da imagem original: %d bytes" % (img.shape[0] * img.shape[1]))
print("Tamanho após a codificação: %d bytes" % len(RLE_NP))
print("\n########### IMAGEM LIMIARIZADA #############")
print("Tamanho da imagem limiarizada: %d bytes" % (img_th.shape[0] * img_th.shape[1]))
print("Tamanho após a codificação: %d bytes" % len(RLE_TH_NP))
