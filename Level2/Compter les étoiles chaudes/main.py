from PIL import Image
import numpy as np

image = Image.open("ciel.png")


pixels = np.array(image)


R = pixels[:, :, 0]
G = pixels[:, :, 1]
B = pixels[:, :, 2]

etoilesChaudes = np.sum((B > R) & (B > G))

print(etoilesChaudes)
