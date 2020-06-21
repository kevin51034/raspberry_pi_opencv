import cv2

cap = cv2.VideoCapture(0)

human_cascade = cv2.CascadeClassifier('998_763_14_35.xml') 

while(cap.isOpened()):
    ret, frame = cap.read()
    #reframe = cv2.resize(frame, (320,240))
    
    #cv2.rectangle(reframe, (100,80), (200,180), (0,0,255), 2)
    gframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    humans = human_cascade.detectMultiScale(gframe, 1.3, 3)

    for(x,y,w,h) in humans:
        frame = cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break


cap.release()
cv2.destroyAllWindows()
