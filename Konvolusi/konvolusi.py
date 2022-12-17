import cv2
import numpy as np
import matplotlib.pyplot as plt

#gunakan gambar milik Anda pribadi, jangan terlalu besar
gambar = cv2.imread('Konvolusi/person.jpg')

gambar = cv2.resize(gambar, (480,640))

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

#pilih salah satu kernel
kernel = np.array([[1,2,1],[1,4,1],[1,2,1]])       #blur
#kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])    #sharp

#konversi ke grayscale
gambar_gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

matriks_baru = np.zeros((jml_baris, jml_kolom))

#loop mulai dari pixel (1,1)
for brs in range(1,jml_baris-1):
    for klm in range(1,jml_kolom-1):
        #baca dan kalikan matriks 3x3 dari gambar awal dengan kernel 3x3
        a = gambar_gray[brs-1,klm-1] * kernel[0,0]   #kiri atas
        b = gambar_gray[brs-1,klm] * kernel[0,1]     #tengah atas
        c = gambar_gray[brs-1,klm+1] * kernel[0,2]   #kanan atas
        d = gambar_gray[brs,klm-1] * kernel[1,0]     #kiri
        e = gambar_gray[brs,klm] * kernel[1,1]       #tengah matriks
        f = gambar_gray[brs,klm+1] * kernel[1,2]     #kanan
        g = gambar_gray[brs+1,klm-1] * kernel[2,0]   #kiri bawah
        h = gambar_gray[brs+1,klm] * kernel[2,1]     #tengah bawah
        i = gambar_gray[brs+1,klm+1] * kernel[2,2]   #kanan bawah

        #hitung total nilai dalam kernel
        jum_kernel = np.sum(kernel)
        if (jum_kernel == 0):
            jum_kernel = 1

        #hitung hasil konvolusi
        konvolusi = np.round((a + b + c + d + e + f + g + h + i) / jum_kernel)

        #perbaiki hasil konvolusi jika di luar rentang 0-255
        if (konvolusi < 0):
            konvolusi = 0
        
        if (konvolusi > 255):
            konvolusi = 255

        #isikan hasil konvolusi ke matriks_baru
        matriks_baru[brs, klm] = konvolusi

#konversi citra_translasi menjadi uint8
matriks_baru = matriks_baru.astype(np.uint8)

cv2.imshow('gambar', gambar)
cv2.imshow('konvolusi', matriks_baru)
cv2.waitKey()



