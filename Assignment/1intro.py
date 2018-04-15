import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv

file =open('saved_data.csv','w')
writer = csv.writer(file)

writer.writerow(["File_Name","Location"])


ls = ['DSC01713.JPG','DSC01798.JPG','DSC01836.JPG','DSC01886.JPG','DSC01916.JPG','DSC02013.JPG','DSC02209.JPG','DSC02252.JPG','DSC02407.JPG','DSC02426.JPG']
for i in range(len(ls)):
    img = cv2.imread(ls[i])
    
    File = ls[i]
    img_gry =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    for angle in np.arange(0, 360,18.0):

        print('img'+str(angle)+'.jpg')
        temp = cv2.imread('img'+str(angle)+'.jpg',0)
        
        w,h = temp.shape[::-1]

        res = cv2.matchTemplate(img_gry,temp,cv2.TM_CCOEFF_NORMED)

        thresh = 0.85
        arr=[]
        loc = np.where(res>=thresh)
        for pt in zip(*loc[::-1]):
            arr.append([pt[0]+w/2,pt[1]+h/2])
    writer.writerow([File,arr])


