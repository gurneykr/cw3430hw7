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

def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def grayscale(i, imglst):
    cv2.imshow(imglst[i][0], imglst[i][1])

    for row in (imglst[i][1]):
        for col in row:
            lum = luminosity(col)
            col[0] = col[1] = col[2] = lum

    cv2.imshow("Grayscaled", imglst[i][1])

def split_merge(i, imglst):
    cv2.imshow(imglst[i][0], imglst[i][1])

    B, G, R = cv2.split(imglst[i][1])

    zeros = np.zeros(imglst[i][1].shape[:2], dtype='uint8')

    cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
    cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
    cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))

def amplify(i, imglst, c, amount):
    cv2.imshow(imglst[i][0], imglst[i][1])

    ## split the image into 3 channels
    B, G, R = cv2.split(imglst[i][1])

    if c == "b":
        amplified_blue = cv2.merge([B + amount, G, R])
        cv2.imshow('Amplified Blue', amplified_blue)
    elif c == "g":
        amplified_green = cv2.merge([B, G + amount, R])
        cv2.imshow('Amplified Green', amplified_green)
    elif c == "r":
        amplified_red = cv2.merge([B, G, R + amount])
        cv2.imshow('Amplified Red', amplified_red)

## here is main for you to test your implementations.
## remember to destroy all windows after you are done.
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--type', required=True, help='Type of image')
    ap.add_argument('-p', '--path', required=True, help='Path to image directory')
    args = vars(ap.parse_args())

    il = read_img_dir(args['type'], args['path'])

    grayscale(0, il)
    split_merge(0, il)
    amplify(0, il, 'b', 100)

    amplify(0, il, 'r', 200)
    cv2.waitKey()
    cv2.destroyAllWindows()