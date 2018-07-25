from PIL import Image
import pytesseract
image = Image.open('d:/pic/test.png')

tessdata_dir_config = '--tessdata-dir "C:/Program Files/VietOCR.NET/tessdata"'
imtext = pytesseract.image_to_string(image,lang='chi_sim',config=tessdata_dir_config)
print (type(imtext))
f = open('d:/pic/a.txt', 'w')
f.write(imtext)
f.close()


