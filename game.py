import pygame

### คำสั่งเริ่มการทำงาน pygame
pygame.init()

### กำหนดข้อความที่ Titlebar
pygame.display.set_caption("just game")

### ตั้งสี RGB
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
Blue = (0,0,255)

### กำหนดหน้าจอ
SCREEN_W = 600
SCREEN_H = 300 
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

### แสดงหน้าจอ
screen.fill(WHITE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit() ### ออกเกม