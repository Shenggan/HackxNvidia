import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fps = cap.get(cv2.CAP_PROP_FPS)

    print("FPS",fps)
    cv2.putText(frame, str(fps), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.imwrite('cap.png', frame)
    #time.sleep(10)

# When everything done, release the capture

