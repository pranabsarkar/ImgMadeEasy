# ImgMadeEasy - A collection of functions for our daily life Computer Vision tasks.

  

In this Repository you will find functions for the following tasks -
1. Video to batch of images.
2. Images to video.

## Usage

 First of all you have to clone this repository.

    git clone https://github.com/pranabsarkar/ImgMadeEasy.git

Then you can follow the given code snippet's for the implementation.

When we have a video and want to convert it into the batch of images then we can use this function -

 

    from iutils import video_photo
    
    FILENAME='pranab.mp4'
    FOLDER_NAME='output'
    
    video_photo(FILENAME,FOLDER_NAME)

When we have batch of images and want to convert the same a video then we can use this function - 


    from iutils import video_photo
    
    pathIn='source/'
    pathOut='output.avi'
    fps=28
    
    convert_frames_to_video(pathIn,pathOut,fps)

## Reference

I have gone through various online resources and built this repository for our ease. 

