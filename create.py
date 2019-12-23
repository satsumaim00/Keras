import cv2, numpy as np

image = np.full((480, 640, 3),(0,0,255), np.uint8)    #값들이 반대로 들어가네요 640 가로  480 세로  rgb값또한 반대로
cv2.imshow('red', image)
cv2.waitKey()
cv2.destroyAllWindows()

image[240, 160] = image[240, 320] = image[240, 480] = (255, 255, 255)
cv2.imshow('black with white pixels', image)
cv2.waitKey()
cv2.destroyAllWindows()

image = cv2.imread('C:\PythonProjects/lena.png')
image = image.astype(np.float32) / 255
print('Shape',image.shape)
print('Data type',image.shape)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',gray)
cv2.waitKey()
cv2.destroyAllWindows()

gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image',gray1)
cv2.waitKey()
cv2.destroyAllWindows()



