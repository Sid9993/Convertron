import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
#img=Image.open('index.jpg')
#text=tess.image_to_string(img)

#print(text)


def image_ocr(image_path, output_txt_file_name):
  image_text = tess.image_to_string(image_path, lang='eng+ces', config='--psm 1')
  with open(output_txt_file_name, 'w+', encoding='utf-8') as f:
    f.write(image_text)
image_path='index.jpg'
output_txt_file_name='file.docx'
image_ocr(image_path,output_txt_file_name)
