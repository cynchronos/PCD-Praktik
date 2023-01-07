import cv2
import numpy as np

#gunakan gambar milik Anda pribadi, jangan terlalu besar
gambar = cv2.imread('Deteksi Tepi/person.jpg')

gambar = cv2.resize(gambar, (240,320))

#konversi ke grayscale
gambar_gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

jml_baris = len(gambar_gray)
jml_kolom = len(gambar_gray[0])

#pilih salah satu kernel
# kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]]) #laplace 1
kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]]) #laplace 2


zero_padding = np.zeros((jml_baris + 2, jml_kolom + 2))

matriks_baru = np.zeros((jml_baris, jml_kolom))

# memasukkan citra awal ke matriks_baru
for brs in range(jml_baris):
    for klm in range(jml_kolom):
            zero_padding[brs + 1, klm + 1] = gambar_gray[brs, klm]

#loop mulai dari pixel (1,1)
for brs in range(1,jml_baris-1):
    for klm in range(1,jml_kolom-1):
        #baca dan kalikan matriks 3x3 dari gambar awal dengan kernel 3x3
        a = zero_padding[brs-1,klm-1] * kernel[0,0]   #kiri atas (Baris sebelum titik tengah dan kolom sebelum titik tengah)
        b = zero_padding[brs-1,klm] * kernel[0,1]     #tengah atas (Baris sebelum titik tengah dan kolom sama dengan titik tengah)
        c = zero_padding[brs-1,klm+1] * kernel[0,2]   #kanan atas
        d = zero_padding[brs,klm-1] * kernel[1,0]     #kiri
        e = zero_padding[brs,klm] * kernel[1,1]       #tengah matriks
        f = zero_padding[brs,klm+1] * kernel[1,2]     #kanan
        g = zero_padding[brs+1,klm-1] * kernel[2,0]   #kiri bawah
        h = zero_padding[brs+1,klm] * kernel[2,1]     #tengah bawah
        i = zero_padding[brs+1,klm+1] * kernel[2,2]   #kanan bawah

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

cv2.imshow('gambar', gambar_gray)
cv2.imshow('deteksi tepi', matriks_baru)
cv2.waitKey()



