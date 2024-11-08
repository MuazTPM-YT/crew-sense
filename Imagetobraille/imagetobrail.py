import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR'  # Adjust path if necessary

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    text = pytesseract.image_to_string(thresh_image)
    print("Extracted Text:\n", text)

    d = pytesseract.image_to_data(thresh_image, output_type=Output.DICT)

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:  
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, d['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow("OCR Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return text

image_path = 'text.jpg' 

extracted_text = extract_text_from_image(image_path)
print("\nFinal Extracted Text:\n", extracted_text)