#!/usr/bin/python

#########################################
# module: hw07_s19.py
# Krista Gurney
# A01671888
#########################################

import math
import numpy as np
import argparse
import cv2
import sys
import os
import re
import argparse
## uses these command line options if you want to run your program
## in a command window.
#ap = argparse.ArgumentParser()
#ap.add_argument('-id', '--imgdir', required = True, help = 'image directory')
#ap.add_argument('-ft', '--ftype', required = True, help = 'file type (e.g., .png)')
#args = vars(ap.parse_args())

def generate_file_names(ftype, rootdir):
    '''
    recursively walk dir tree beginning from rootdir
    and generate full paths to all files that end with ftype.
    sample call: generate_file_names('.jpg', /home/pi/images/')
    '''
    for path, dirlist, filelist in os.walk(rootdir):
        for file_name in filelist:
            if not file_name.startswith('.') and \
               file_name.endswith(ftype):
                yield os.path.join(path, file_name)
        for d in dirlist:
            generate_file_names(ftype, d)

def read_img_dir(ftype, imgdir):
    images_array = []
    for file in generate_file_names(ftype,imgdir):
        images_array.append((file, cv2.imread(file)))
    return images_array

def grayscale(i, imglst):
    cv2.imshow(imglst[i][0], imglst[i][1])
    cv2.waitKey(0)

def split_merge(i, imglst):
    ## your code here
    pass

def amplify(i, imglst, c, amount):
    ## your code here
    pass

## here is main for you to test your implementations.
## remember to destroy all windows after you are done.
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--type', required=True, help='Type of image')
    ap.add_argument('-p', '--path', required=True, help='Path to image directory')
    args = vars(ap.parse_args())

    il = read_img_dir(args['type'], args['path'])

    grayscale(0, il)
    # print(il[0][0])#path
    # print(il[0][1])#matrix

    # print(il[0][1].shape)
    # # image = cv2.imread(il[0])
    # cv2.imshow("image", image)
    # cv2.waitKey(0)

    # print(il[0][1])
    #verify_img_list(il)
    #grayscale(0, il)
    #split_merge(0, il)
    #amplify(0, il, 'b', 200)
    #cv2.waitKey()
    #cv2.destroyAllWindows()


 
