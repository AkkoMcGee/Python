import cv2
from matplotlib import pyplot as plt

BASIC = True
MEDIUM = False
ADVANCED = False

img = cv2.imread('Korsica.PNG', 1)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

for i in range(row):
    for j in range(col):
        if (img[i][j] < 10):
            img2[i][j] = 10
        if (img[i][j] > 240):
            img2[i][j] = 240

f_max = img2.max()
f_min = img2.min()

img3 = img2.copy()
for i in range(row):
    for j in range(col):
        img3[i][j] = ( (img2[i][j] - f_min)/(f_max - f_min) ) * 256


fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize =(8,8))

axs[0][0].imshow(img, cmap="gray")
axs[0][0].axis("off")

axs[0][1].imshow(img2, cmap="gray")
axs[0][1].axis("off")

axs[0][2].imshow(img3, cmap="gray")
axs[0][2].axis("off")

axs[1][0].hist(img.ravel(), 256, [0, 256], color="gray")
axs[1][1].hist(img2.ravel(), 256, [0, 256], color="gray")
axs[1][2].hist(img3.ravel(), 256, [0, 256], color="gray")

plt.show()

if (BASIC):
    plt.imshow(img_rgb)
    plt.colorbar()
    plt.show()

    plt.hist(img_rgb.ravel(), 256, [0, 256])
    plt.show()

if (MEDIUM):
    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    im = ax1.imshow(img_rgb[:, :, 0], cmap="Greys")
    ax1.set_title("Rojo")
    plt.colorbar(im, ticks=[10, 120, 200], orientation='horizontal')

    ax2 = fig.add_subplot(1, 2, 2)
    im = ax2.imshow(img_rgb)
    ax2.set_title("RGB")

    plt.colorbar(im, ticks=[10, 120, 200], orientation='horizontal')
    plt.show()

if (ADVANCED):
    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    im = ax1.imshow(img_rgb)
    ax1.set_title("RGB")
    plt.colorbar(im, ticks=[10, 120, 200], orientation='horizontal')

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.hist(img_rgb.ravel(), 256, [0, 256])
    ax2.set_title("Histograma")

    plt.show()
