import pygame as pg

# Init 
pg.init()
# Variable Runing game
isRun = True

# Make surves object From Display
window_lebar =500
window_panjang = 500
window = pg.display.set_mode((window_lebar,window_panjang))

# Object game
#posisi
x = 250
y = 250

# Ukuran
panjang = 20
lebar = 20

# speed
speed = 1

while isRun:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRun = False
    
    # ambil Semua Keyboad Press
    keys = pg.key.get_pressed()

    # ambil ke kiri
    if keys[pg.K_LEFT] and x > 0: # x = 250 lebih dari 0 = true
        x -= speed
    elif keys[pg.K_RIGHT] and x < window_lebar-lebar:    # x:250 kurang dari (500-20) = 480 = true
        x += speed
    elif keys[pg.K_DOWN] and y < window_panjang - panjang : 
        y += speed
    elif keys[pg.K_UP] and y > 0:
        y -= speed
    # pertanyaan kenapa ini kotak terbatas kalau pake (lebar : si kotak) 
# Updaten Asset
    window.fill((255,255,255))
    pg.draw.rect(window,(255,0,0),(x,y,lebar,panjang))  
# Render ke display
    pg.display.update()

pg.quit()

# User Input / Database input


