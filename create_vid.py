import os
import cv2
import time

# providing the path
path = 'ghost_frnds'
# creating an empty list to store the file names 
images = [] 

# adding the file names to the `images` list only if the extentions are the ones mentioned
for file in os.listdir(path):

    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path + '/' + file
        print(file_name)
        images.append(file_name)
        time.sleep(0.3)

# counting total images
count = len(images)
print('total images: ', count)

# reading only one frame of only one image to get the size
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

# creating a new video in the given format, fps and size
out = cv2.VideoWriter('friends.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.9, size)

for i in images:
    frame = cv2.imread(i)
    cv2.imshow('friends', frame)
    out.write(frame)
    if cv2.waitKey(900)==32:
        break

    
out.release()

print('DONE!')
