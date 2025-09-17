import pygame

### คำสั่งเริ่มการทำงาน pygame
pygame.init()

### กำหนดข้อความที่ Titlebar
pygame.display.set_caption("just game")

### สร้างหน้าจอเกม กว้าง สูง
screen = pygame.display.set_mode((640,360))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit() ### ออกเกม