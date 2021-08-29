import os
import cv2
mode = "jpg"
folder = "image"
files = os.listdir(folder)
print(files)
for i in range(len(files)):
    files[i] = f"{folder}/{files[i]}"
for i in files:
    print(''.join(i.split('.')[:-1]))
    cv2.imwrite(f"output/{''.join(i.split('.')[:-1])}.{mode}", cv2.imread(i))
