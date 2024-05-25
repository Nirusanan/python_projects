import qrcode
import cv2
from PIL import Image


# Decode QR code using OpenCV
def decode_qr_code(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Initialize the QRCode detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    data, points, _ = detector.detectAndDecode(image)

    if data:
        print("Decode the QR Code:", data)
    else:
        print("No QR code found")

# Decode the QR code from the saved image
decode_qr_code("myqr.png")
