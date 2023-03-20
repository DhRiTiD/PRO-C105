import cv2

# capturing the vid through webcam
video = cv2.VideoCapture(0)

# checking if the video is being captured
if video.isOpened()==False:
    print('Video capturing failed!')

# print height , width , fps
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('(', height, end= ', ')
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width, end=', ' )
fps = int(video.get(cv2.CAP_PROP_FPS))
print(fps, ')')

# creating a new video in the given format, fps and size
out = cv2.VideoWriter('newVideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# capturing t he video frame by frame inside the new vid file
while(True):

    # reading the frames of the video
    ret, frame = video.read()

    # displaying the captured video frame by frame
    cv2.imshow('Webcam', frame)

    # writing the captured vid frame by frame
    out.write(frame)

    # stopping the program
    if cv2.waitKey(30) == 32:
        print('STOPPED!')
        break

# destroying the windows
video.release()
out.release()

cv2.destroyAllWindows()