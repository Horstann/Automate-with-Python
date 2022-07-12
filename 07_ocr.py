import cv2
import pytesseract

def img_to_str(img):
    # convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # remove noise
    img = cv2.medianBlur(img, 5)
    # thresholding to determine if pixel is black or white
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread()