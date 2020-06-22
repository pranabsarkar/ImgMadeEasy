# Importing all necessary libraries 
import cv2 
import os

def photo(FILENAME,FOLDER_NAME):
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


