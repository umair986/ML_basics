import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #works for images , videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA)

def captureRes(width , height):
    #works only for live videos
    capture.set(3,width)
    capture.set(4,height)

img_resized = rescaleFrame(img)
cv.imshow('Image Resized' , img_resized)
capture = cv.VideoCapture('Videos/dog.mp4') #pass 0 for webcam instead of video path

while True:
    isTrue, frame = capture.read()
    frame_resized= rescaleFrame(frame, scale=0.2)

    cv.imshow("Video", frame)
    cv.imshow('Video Resized' , frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): #means if letter  D is pressed end video
        break

capture.release()
cv.destroyAllWindows()