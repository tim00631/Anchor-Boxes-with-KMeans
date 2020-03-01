import os
import glob
from random import random
from random import seed
import cv2
import numpy as np
import xml.etree.ElementTree as ET

def random_increase_brightness(path,min,max):
    img_list = []
    for img_file in glob.glob(path + '/*.jpg'):
        img = cv2.imread(img_file)
        print(img_file)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        factor = (min + (random() * (max - min)))
        print(factor)
        h, s, v = cv2.split(hsv)
        height, width = v.shape
        if factor > 1:
            for i in range(height):
                for j in range(width):
                    if hsv[:,:,2][i][j]*factor > 255: #if overflow occurs
                        hsv[:,:,2][i][j] = 255  
                    else:
                        hsv[:,:,2][i][j] = hsv[:, :, 2][i][j] * factor
                        # here won't underflow
        else:
            weight_arr = np.ones(v.shape) * factor
            hsv[:, :, 2] = (hsv[:, :, 2] * weight_arr)

        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        file_name = "new_" + os.path.basename(img_file) # "new_123.jpg"
        cv2.imwrite(os.path.join(path, file_name), img)
        # return

def modify_xml_file_name(path):
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        file_name_tag = root.find('filename')
        #file_name_tag.text = "new_" + os.path.basename(xml_file) # update new xml's file name
        file_name_tag.text = os.path.basename(xml_file) # update original xml's file name
        print(file_name_tag.text)
        path_tag = root.find('path')
        if path_tag != None:
            path_tag.text = path + file_name_tag.text
            print(path_tag.text)
        else:
            print("XML file no pathname tag")
        tree.write(path + file_name_tag.text)
        # return
def main():
    dir_name = 'modified/'  
    sub_folder_name = ''  # if >2 folder, add name here
    for folder in [sub_folder_name]:
        image_path = os.path.join(os.getcwd(), (dir_name + folder))
        #random_increase_brightness(image_path, 0.9, 1.1) # brightness *=rand(min,max) 
        #print('Successfully adjustified image\'s brightness.')
        modify_xml_file_name(image_path)  # update new image's xml file
        print('Successfully modified image\'s xml file.')

seed()
main()
