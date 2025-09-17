import pygame

### คำสั่งเริ่มการทำงาน pygame
pygame.init()

### กำหนดข้อความที่ Titlebar
pygame.display.set_caption("test beta")

### ตั้งสี RGB
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
Blue = (0,0,255)

### กำหนดหน้าจอ
SCREEN_W = 1280
SCREEN_H = 700
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

### img back
imgfirst = pygame.image.load("img/back.png")
imgfirst = pygame.transform.scale(imgfirst,(SCREEN_W,SCREEN_H))
### ปุ่มcontinew
continewbottom = pygame.image.load("img/continew.png")
### ทำให้อยู่กึ่งกลางแนวแกน x 
continewbottom_rect = continewbottom.get_rect()
continewbottom_rect.centerx = SCREEN_W // 2
continewbottom_rect.centery = SCREEN_H // 2
### ปุ่ม new
new = pygame.image.load("img/new.png")
### ทำให้อยู่กึ่งกลางแนวแกน x และใต้ continew
new_rect = new.get_rect()
new_rect.centerx = SCREEN_W // 2
new_rect.top = continewbottom_rect.bottom + 10
### ปุ่ม save
save = pygame.image.load("img/save.png")
### ทำให้อยู่กึ่งกลางแนวแกน x และใต้ continew
save_rect = save.get_rect()
save_rect.centerx = SCREEN_W // 2
save_rect.top = new_rect.bottom + 10

### แสดงหน้าจอ
screen.fill(WHITE) ###เปลี่ยนสีพื้นหลังตามตัวแปล RGB ข้างบน
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(imgfirst,(0,0))
    screen.blit(continewbottom, continewbottom_rect)
    screen.blit(new,new_rect)
    screen.blit(save,save_rect)
    pygame.display.update() ### อัพเดตสีพื้นหลัง
pygame.quit() ### ออกเกม