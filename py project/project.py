import numpy as np 
import imageio
import scipy.ndimage
import cv2

img="wp2752039.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
    #it is 2-dimensional array formula to convert image to gray scale

def dodge(front,back):
    final_sketch = front*255/(255-back)
    #if image is greater than 255 which i don't think is posssible but still if it is there will convert it to 255
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    #to convert any suitable existing column to categorical type we will use aspect function
    #and unit8 is for 8-bit signed integer
    return final_sketch.astype('uint8')

ss = imageio.imread(img)  #to read the given image
gray = rgb2gray(ss)   #first we will image to black and white that means gray scale

i = 255-gray  #0,0,0 is for darkest color and 255,255,255 is for brighest color which is probably white color

#to convert it into blur image
blur = scipy.ndimage.gaussian_filter(i,sigma =15)
#sigma is the intensity of blurness of image
r=dodge(blur,gray) #this function will convert our image to sketch by taking two parameter as blur and gray

cv2.imwrite('wp2752039-sketch.jpg',r)















