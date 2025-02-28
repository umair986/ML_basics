import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA)

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