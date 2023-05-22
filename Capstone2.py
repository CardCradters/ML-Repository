# Optical Character Recognition (OCR) 
import cv2
import easyocr
import matplotlib.pyplot as plt 
import numpy as np
import re

# Lokasi Foto
lokasi_foto = 'namecard1.jpg'

foto = cv2.imread(lokasi_foto)

## Deteksi Text
deteksi = easyocr.Reader(['id'], gpu=False)
kata = deteksi.readtext(foto)

## Membuat Kotak pada Text di Image
for a in kata:
    bbox, text, score = a
    cv2.rectangle(foto, bbox[0], bbox[2], (0, 255, 0), 5)

plt.imshow(cv2.cvtColor(foto, cv2.COLOR_BGR2RGB))
plt.show()

# Klasifikasi
nama_katakunci = ['MUHAMMAD']
email_katakunci = ['@','.com', '.']
nomorhp_katakunci = ['+62', '08']
kantor_katakunci = ['PT.','CV']

nama = ''
email = ''
nomor_hp = ''
kantor = ''

for bbox, text, score in kata:
    # Mengubah teks menjadi huruf kecil untuk pencocokan yang tidak case-sensitive
    lowercase_text = text.lower()
    # Menghapus spasi, tanda baca, dan karakter non-digit dari teks
    cleaned_text = re.sub(r'\D', '', '-', lowercase_text)

    # Mencari kata kunci dalam teks dan mengklasifikasikannya
    if any(keyword in lowercase_text for keyword in nama_katakunci):
        nama = text
    elif any(keyword in lowercase_text for keyword in email_katakunci):
        email = text
    elif any(keyword in lowercase_text for keyword in kantor_katakunci):
        kantor = cleaned_text
    elif any(keyword in lowercase_text for keyword in nomorhp_katakunci):
        nomor_hp = cleaned_text

## Mengatasi jika tidak ada yang terklasifikasi
if not nama:
    nama = '-'
if not email:
    email = '-'
if not kantor:
    kantor = '-'
if not nomor_hp:
    nomor_hp = '-'
    
## Menampilkan hasil dan informasi yang terklasifikasi
print('Nama:', nama)
print('Email:', email)
print('Kantor:', kantor)
print('Nomor HP:', nomor_hp)
