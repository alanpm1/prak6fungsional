# TODO 0: Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open(r"C:\Users\alan\Documents\prakfungsional\latihanmodul6\b2.png")

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
direktoriFont = r"C:\Users\alan\Documents\prakfungsional\latihanmodul6\RED BURGER.otf"  # Ganti dengan direktori font yang sudah kamu unduh
size = 24
font = ImageFont.truetype(direktoriFont, size)
text = "Noordin Prasetyo Maulana\nNIM: 202110370311382"

# Use getsize directly on the draw object
text_width, text_height = draw.textsize(text, font)
text_x = (gambarBW.width - text_width) // 2
text_y = (gambarBW.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("percobaan_satu.png")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
