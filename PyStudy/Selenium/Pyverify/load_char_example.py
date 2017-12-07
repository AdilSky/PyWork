#-*-coding:utf-8-*-
# Time:2017/9/29 16:19
# Author:YangYangJun



# load_char_example.py
# 注意:二值图像0/1统一转化为0/255
from PIL import Image,ImageDraw,ImageChops
import os

# 遍历指定目录,显示目录下的所有文件名
def eachfile(filepath):
    dir_list =  os.listdir(filepath)
    all_dir = []
    for dir in dir_list:
        child = '%s%s' % (filepath, dir)
        all_dir.append(child)
    return all_dir

# 共31个字符
char_set = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 加载字符图片样本
# 将对应字符的样本按照上述 char_set 的顺序加载
def load_char_example():
    global char_set

    char_example = []
    for char in char_set:

        char_example.append([])

        folder_path = 'captcha_char/%c/'%char
        image_name_list = eachfile(folder_path)
        for image_name in image_name_list:
            image = Image.open(image_name)
            # 注意这里读取的数据为灰度图像,像素值为0,255
            # 为此将其他地方出现的0/1二值图像统一处理成0/255二值图像
            char_example[-1].append(image)
    return char_example

if __name__ == '__main__':
    pass

