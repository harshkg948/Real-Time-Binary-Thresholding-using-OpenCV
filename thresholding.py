import cv2 
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    _,thresh = cv2.threshold(src = frame,thresh=120,maxval=255,type=cv2.THRESH_BINARY)
    cv2.imshow('thresh',thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()     