import numpy as np
import imageio.v3 as img

image_path1 = "Daunpepaya.jpg"
image1 = img.imread(image_path1)
image_path2 = "singkong.jpg"
image2 = img.imread(image_path2)
image_path3 = "Kenikir.jpg"
image3 = img.imread(image_path3)

red1 = image1[:,:,0]
Green1 = image1[:,:,1]
Blue1 = image1[:,:,2]

red2 = image2[:,:,0]
Green2 = image2[:,:,1]
Blue2 = image2[:,:,2]

red3 = image3[:,:,0]
Green3 = image3[:,:,1]
Blue3 = image3[:,:,2]

image_red1 = np.zeros_like(image1)
image_red1[:,:,0] = red1
image_red2 = np.zeros_like(image2)
image_red2[:,:,0] = red2
image_red3 = np.zeros_like(image3)
image_red3[:,:,0] = red3

image_Blue1 = np.zeros_like(image1)
image_Blue1[:,:,2] = Blue1
image_Blue2 = np.zeros_like(image2)
image_Blue2[:,:,2] = Blue2
image_Blue3 = np.zeros_like(image3)
image_Blue3[:,:,2] = Blue3

image_Green1 = np.zeros_like(image1)
image_Green1[:,:,1] = Green1
image_Green2 = np.zeros_like(image2)
image_Green2[:,:,1] = Green2
image_Green3 = np.zeros_like(image3)
image_Green3[:,:,1] = Green3

gray1 = 0.2 * red1 + 0.5 * Green1 + 0.3 *Blue1
image_gray1 = np.zeros_like(image1)
image_gray1[:,:,0] = gray1
image_gray1[:,:,1] = gray1
image_gray1[:,:,2] = gray1

gray2 = 0.2 * red2 + 0.5 * Green2 + 0.3 *Blue2
image_gray2 = np.zeros_like(image2)
image_gray2[:,:,0] = gray2
image_gray2[:,:,1] = gray2
image_gray2[:,:,2] = gray2

gray3 = 0.2 * red3 + 0.5 * Green3 + 0.3 *Blue3
image_gray3 = np.zeros_like(image3)
image_gray3[:,:,0] = gray3
image_gray3[:,:,1] = gray3
image_gray3[:,:,2] = gray3

threshold = 100
image_bw1 = np.zeros_like(image1)
threshold = 100
image_bw2 = np.zeros_like(image2)
threshold = 100
image_bw3 = np.zeros_like(image3)

for i in range (0, len(gray1)) :
    for j in range(0, len(gray1[i])) :
        if (gray1[i,j] > threshold) :
            image_bw1[1,j] = 255
        else :
            image_bw1[i,j] = 0

for i in range (0, len(gray2)) :
    for j in range(0, len(gray2[i])) :
        if (gray2[i,j] > threshold) :
            image_bw2[1,j] = 255
        else :
            image_bw2[i,j] = 0

for i in range (0, len(gray3)) :
    for j in range(0, len(gray3[i])) :
        if (gray3[i,j] > threshold) :
            image_bw3[1,j] = 255
        else :
            image_bw3[i,j] = 0

while True :
    print ("pilih foto :")
    print ("1. Daun pepaya")
    print ("2. Singkong")
    print ("3. kenikir")
    print ("4. exit")
    a = int(input("masukan pilihan : "))
    if (a == 1) :
        print("ubah foto Daun pepaya ke warna :")
        print("1. merah")
        print("2. biru")
        print("3. hijau")
        print("4. abu-abu")
        print("5. Bw")
        b = int(input("masukan pilihan : "))
        if (b == 1) :
            image1 = img.imwrite("image_red_DaunPepaya.jpeg", image_red1)
            print ("process berhasil!")
        if (b == 2) :
            image1 = img.imwrite("image_Blue_DaunPepaya.jpeg", image_Blue1)
            print ("process berhasil!")
        if (b == 3) :
            image1 = img.imwrite("image_Hijau_DaunPepaya.jpeg", image_Green1)
            print ("process berhasil!")
        if (b == 4) :
            image1 = img.imwrite("image_Grey_DaunPepaya.jpeg", image_gray1)
            print ("process berhasil!")
        if (b == 5) :
            image1 = img.imwrite("image_Bw_DaunPepaya.jpeg", image_bw1)
            print ("process berhasil!")

    if (a == 2) :
        print("ubah foto Singkong ke warna :")
        print("1. merah")
        print("2. biru")
        print("3. hijau")
        print("4. abu-abu")
        print("5. Bw")
        c = int(input("masukan pilihan : "))
        if (c == 1) :
            image2 = img.imwrite("image_red_Singkong.jpeg", image_red2)
            print ("process berhasil!")
        if (c == 2) :
            image2 = img.imwrite("image_Blue_Singkong.jpeg", image_Blue2)
            print ("process berhasil!")
        if (c == 3) :
            image2 = img.imwrite("image_Hijau_Singkong.jpeg", image_Green2)
            print ("process berhasil!")
        if (c == 4) :
            image2 = img.imwrite("image_Grey_Singkong.jpeg", image_gray2)
            print ("process berhasil!")
        if (c == 5) :
            image2 = img.imwrite("image_Bw_Singkong.jpeg", image_bw2)
            print ("process berhasil!")

    if (a == 3) :
        print("ubah foto Kenikir ke warna :")
        print("1. merah")
        print("2. biru")
        print("3. hijau")
        print("4. abu-abu")
        print("5. Bw")
        d = int(input("masukan pilihan : "))
        if (d == 1) :
            image3 = img.imwrite("image_red_Kenikir.jpeg", image_red3)
            print ("process berhasil!")
        if (d == 2) :
            image3 = img.imwrite("image_Blue_Kenikir.jpeg", image_Blue3)
            print ("process berhasil!")
        if (d == 3) :
            image3 = img.imwrite("image_Hijau_Kenikir.jpeg", image_Green3)
            print ("process berhasil!")
        if (d == 4) :
            image3 = img.imwrite("image_Grey_Kenikir.jpeg", image_gray3)
            print ("process berhasil!")
        if (d == 5) :
            image3 = img.imwrite("image_Bw_Kenikir.jpeg", image_bw3)
            print ("process berhasil!")

    if (a == 4) :
        break





