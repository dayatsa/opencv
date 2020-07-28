import cv2
#import dateTime

cap = cv2.VideoCapture(0);
print("Width : ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height : ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(cap.isOpened()) :
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width : ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Height : ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.putText(frame, text, (10,50), font, 0.5, (0,255,255), 1, cv2.LINE_AA)

        cv2.imshow('gray', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()  
cv2.destroyAllWindows()