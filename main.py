
# author: Kudratov Iskandar
# guruh: 403-21 TI

from PIL import  Image, ImageFont, ImageDraw
import string, random
from pytesseract import pytesseract

# Textni rasmga qo'yish generatori
def text_to_image():
    for i in range(30):
        # Oldindan rasm bor ya'ni orqadagi fon deb olamiz
        my_image = Image.open("original.png")
        # Rasm ichiga qo'yiladigan textni fontini o'rnatish
        # ya'ni 'Roboto-Regular.ttf
        title_font = ImageFont.truetype('fonts/Roboto-Regular.ttf', 60)
        # Text Uppercase ko'rinishini belgilaymiz
        letters = string.ascii_uppercase
        # Text random ko'rinishida bo'ladi
        title_text = ''.join(random.choice(letters) for i in range(6))
        # Textni rasmga qo'shish uchun orqadagi fon olamiz ya'ni 'original.png'
        image_editable = ImageDraw.Draw(my_image)
        # Textni rasmga qo'shish
        # (x=20, y=25) Textni joylashish kordinatalari
        # (237, 230, 211) Text rangi
        # title_font font ya'ni 'Roboto-Regular.ttf'
        image_editable.text((20,25), title_text, (237, 230, 211), font=title_font)
        # rasmni saqlash
        my_image.save(f"data_store/result{i}.jpg")

# Textni rasmdan o'qib olish generatori
def text_from_image():
    for i in range(30):
        #Rasmlarni data_store papkasidan o'qib olish
        path_to_image = f'data_store/result{i}.jpg'
        #Rasmni PIL kutubxona orqali ochish
        img = Image.open(path_to_image)
        #Textni rasmdan o'qib olish
        text = pytesseract.image_to_string(img)
        print(text)


#text_to_image()
text_from_image()