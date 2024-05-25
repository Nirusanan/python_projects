import cv2
from PIL import Image
import time

cam = cv2.VideoCapture(0)
cam.set(5,640)
cam.set(6, 480)

detector = cv2.QRCodeDetector()

while True:
    success, frame = cam.read()
    if not success:
        break

    # Detect and decode the QR code
    data, points, _ = detector.detectAndDecode(frame)

    if data:
        print("QR Code data:", data)
        time.sleep(6)  

    # Display the frame
    cv2.imshow("QR_Code", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
