import cv2 as cv

# img = cv.imread("Photos/cat_large.jpg")

# cv.imshow('Cat', img)
# cv.waitKey(0)
# reading video
capture = cv.VideoCapture('Videos/dog.mp4') #pass 0 for webcam instead of video path

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #means if letter  D is pressed end video
        break

capture.release()
cv.destroyAllWindows()

