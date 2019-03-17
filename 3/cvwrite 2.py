import numpy as np
import cv2
import base64

f = open("text.txt",'w')


cap = cv2.VideoCapture(0)


for i in range (1,500):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame= cv2.resize(frame, (130, 100))
    if i>0:
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = np.array(imgencode)
        stringData = data.tostring()
        stringData64=base64.encodestring(stringData) 
        print(type(stringData64))
        print stringData64
        f.write(stringData64)
        f.seek(0,0)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()