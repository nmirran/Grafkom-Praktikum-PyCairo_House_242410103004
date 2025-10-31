import cairo
import numpy as np

width, height = 900, 900
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Latar Langit
ctx.rectangle(0, 0, width, height)
ctx.set_source_rgb(0.5, 0.8, 1)  
ctx.fill()

# Matahari 
ctx.set_line_width(5)
x = 700
y = 170
r = 40
radius_start = 0
radius_end =  2 * np.pi 
ctx.arc(x,y,r, radius_start, radius_end)

ctx.set_source_rgb(1, 0.84, 0) 
ctx.fill_preserve()

# Garis Sinar Matahari (6 Garis)
# Garis 1 dari kiri
ctx.move_to(585, 160) # Kiri atas 
ctx.line_to(625, 165) # Kanan Bawah

# Garis 2 dari kiri
ctx.move_to(590, 230) # Kiri Bawah
ctx.line_to(625, 210) # Kanan Atas

# Garis 3 dari kiri
ctx.move_to(640, 270) # Kiri Bawah
ctx.line_to(660, 240) # Kanan Atas

# Garis 4 dari kiri
ctx.move_to(702, 280) # Kanan Bawah
ctx.line_to(700, 250) # Kiri Atas 

# Garis 5 dari kiri
ctx.move_to(758, 270) # Kanan Bawah
ctx.line_to(746, 245) # Kiri Atas 

# Garis 6 dari kiri
ctx.move_to(800, 230) # Kanan Bawah
ctx.line_to(775, 210) # Kiri Atas

ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Tanah
ctx.rectangle(0, 780, width, height-780) # x = 0, y = 780, w = 900, h = 120 

ctx.set_source_rgb(0.6, 0.4, 0.2)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Rumah (Dinding)
ctx.rectangle(150, 450, 550, 330) # x = 150, y = 450, w = 550, h = 330
ctx.set_source_rgb(0.9, 0.6, 0.3)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Atap Segitiga
ctx.move_to(130, 450) # Titik awal -> x = 130, y = 450
ctx.line_to(420, 250) # Titik puncak -> x = 420, y = 250
ctx.line_to(720, 450) # Titik akhir -> x = 720, y = 450
ctx.close_path()
ctx.set_source_rgb(0.7, 0.2, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Cerobong asap
ctx.move_to(240, 298)  # Titik awal -> x = 240, y = 298
ctx.line_to(240, 240)  # Dari titik awal garis ke atas ke y = 240
ctx.line_to(271, 240)  # Dari garis dengan y = 240 sblmnya digambar garis horizontal ke x = 271
ctx.line_to(271, 288)  # Dari garis dengan x = 271 sblmnya digambar garis vertikal ke y = 288 
ctx.line_to(320, 317)  # Lalu, digambar garis lagi ke x = 320 dan y = 317
ctx.line_to(300, 334)  # Terakhir, digambar garis ke x = 300 dan y = 334
ctx.close_path()  

ctx.set_source_rgb(0.5, 0.2, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Pintu
ctx.move_to(375, 780)
ctx.line_to(375, 640)
ctx.arc(435, 640, 60, np.pi, 0) # Membuat setengah lingkaran di atas dengan titik pusat x = 435, y = 640, dan r = 60
ctx.line_to(495, 780)
ctx.close_path()

ctx.set_source_rgb(0.5, 0.2, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Pembuka Pintu (Garis Vertikal Pintu)
ctx.move_to(435, 780)
ctx.line_to(435, 580)

# Jendela Kiri
ctx.rectangle(200, 490, 120, 100) # x = 200, y = 490, w = 120, h = 100
ctx.set_source_rgb(0, 0.8, 1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()
# Garis Horizontal Jendela Kiri
ctx.move_to(200, 540)
ctx.line_to(320, 540)
# Garis Vertikal Jendela Kiri
ctx.move_to(260, 490)
ctx.line_to(260, 590)

# Jendela Kanan
ctx.rectangle(540, 490, 120, 100) # x = 540, 490, 120, 100
ctx.set_source_rgb(0, 0.8, 1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()
# Garis Horizontal Jendela Kanan
ctx.move_to(540, 540)
ctx.line_to(660, 540)
# Garis Vertikal Jendela Kanan
ctx.move_to(600, 490)
ctx.line_to(600, 590)

ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Kenop Pintu
ctx.arc(420, 700, 5, 0, 2 * np.pi) # Membuat lingkaran penuh dengan titik pusat x = 420, y = 700, dan r = 5 
ctx.stroke()

ctx.arc(450, 700, 5, 0, 2 * np.pi) # Membuat lingkaran penuh dengan titik pusat x = 450, y = 700, dan r = 5
ctx.stroke()

# Semak-semak
def semak_semak(x, y):
    ctx.move_to(x, y) 
    # Membuat 4 garis yang membentuk semak-semak
    ctx.curve_to(x-50, y-50, x+20, y-40, x+25, y-30) # Garis 1 dari kiri
    ctx.curve_to(x+25, y-30, x+20, y-80, x+50, y-30) # Garis 2 dari kiri
    ctx.curve_to(x+50, y-30, x+70, y-100, x+80, y-30) # Garis 3 dari kiri
    ctx.curve_to(x+80, y-30, x+130, y-60, x+100, y) # Garis 4 dari kiri
    ctx.close_path()

    ctx.set_source_rgb(0.1, 0.8, 0.2) # Warna semak-semak
    ctx.fill_preserve()

    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()
    
# Memanggil fungsi semak_semak untuk membuat semak-semak dengan 2 parameter x dan y
semak_semak(50, 780) 
semak_semak(120, 780)
semak_semak(650, 780)
semak_semak(720, 780)

# Awan
def awan(x, y, scale=1):
    ctx.move_to(x, y)  
    # Membuat 4 garis yang membentuk awan 
    ctx.curve_to(x - 20*scale, y - 30*scale, x + 30*scale, y - 50*scale, x + 60*scale, y - 20*scale) # Garis / Lengkungan 1 dari kiri
    ctx.curve_to(x + 90*scale, y - 50*scale, x + 130*scale, y - 20*scale, x + 120*scale, y + 10*scale) # Garis / Lengkungan 2 dari kiri
    ctx.curve_to(x + 150*scale, y + 20*scale, x + 130*scale, y + 50*scale, x + 90*scale, y + 40*scale) # Garis / Lengkungan 3 dari kiri
    ctx.curve_to(x + 60*scale, y + 60*scale, x + 20*scale, y + 40*scale, x, y) # Garis / Lengkungan 4 dari kiri
    ctx.close_path()
    
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill_preserve()
    
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2)
    ctx.stroke()

# Memanggil fungsi awan untuk membuat awan dengan 3 parameter x, y, dan scale untuk mengatur besar kecil awannya
awan(70, 80, 1.5)
awan(680, 70, 0.8)
awan(630, 80, 0.6)
awan(380, 150, 1.2)

surface.write_to_png("duplikatimage.png")