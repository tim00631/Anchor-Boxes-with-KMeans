import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
class_list = {'aquarium': 0, 'bottle': 0, 'bowl': 0, 'box': 0, 'bucket':0, 'plastic_bag':0, 'plate':0, 'styrofoam':0,
 'tire':0, 'toilet':0, 'tub':0, 'washing_machine':0, 'water_tower':0}
def counting(path):
    obj_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            obj_list.append(member.find('name').text)
    for name in class_list:
        class_list[name] = obj_list.count(name)
        print(name, class_list[name])
    
    #print(class_list)
    #print(pd.DataFrame(data=class_list, columns=['name', 'count']))
    plt.barh(range(len(class_list)), list(class_list.values()))
    plt.xlabel('Count')
    plt.ylabel('Name') 
    plt.yticks(range(len(class_list)), list(class_list.keys()), fontsize=8)
    # i = -0.2
    # for name in class_list:
    #     plt.text(x=class_list[name] + 5, y=i,s = class_list[name], color='black')
    #     i = i+1
    plt.show()
    
def main():
    dir_name = 'modified/'  
    sub_folder_name = ''  # if >2 folder, add name here
    for folder in [sub_folder_name]:
        image_path = os.path.join(os.getcwd(), (dir_name + folder))
        counting(image_path)  # update new image's xml file
        print('Counting finished.')

main()
