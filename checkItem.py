from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open("zzz.png"), lang = "kor"))
# img = cv2.imread('image.JPG')
# text = pytesseract.image_to_string(img)

# print(text)