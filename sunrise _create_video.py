import os
import cv2

# provin the path
path = "images"

# creating an empty list to store the file names 
images = []

# adding the file names to the `images` list only if the extentions are the ones mentioned
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
# counting total images
print(len(images))
count = len(images)

# reading only one frame of only one image to get the sze
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('sunrise.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5.2, size)

#sunrise
for i in range(count-1, 0, -1):
    frame=cv2.imread(images[i]) 
    out.write(frame)
    cv2.imshow('sunrise ', frame)
    if cv2.waitKey(25) == 32:
        break

# for sunset
# for i in range(0, count):
#     frame=cv2.imread(images[i]) ##
#     out.write(frame)

out.release()

print('DONE!')