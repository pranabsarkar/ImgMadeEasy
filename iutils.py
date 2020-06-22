# Importing all necessary libraries 
import cv2 
import os
import numpy as np
from os.path import isfile, join

def video_photo(FILENAME,FOLDER_NAME):
    # Read the video from specified path 
    cam = cv2.VideoCapture(FILENAME)
    try: 
        # creating a folder named data 
        if not os.path.exists(FOLDER_NAME): 
            os.makedirs(FOLDER_NAME) 

    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 

    # frame 
    currentframe = 0
    while(True): 

        # reading from frame 
        ret,frame = cam.read() 

        if ret:
            # if video is still left continue creating images 
            name = './'+FOLDER_NAME+'/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name) 

            # writing the extracted images 
            cv2.imwrite(name, frame) 

            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
        else: 
            break

    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows() 

"""
pathIn = The path which contains all the images.
pathOut= The output file name in .avi format.
fps = Define the Frames Per Second.

""" 

def convert_frames_to_video(pathIn,pathOut,fps):
    pathIn='./'+pathIn
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
 
