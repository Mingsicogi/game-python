import pygame

pygame.init()

width = 480
height = 640

screen = pygame.display.set_mode(((width, height)))

pygame.display.set_caption("Mins game")

# 이미지 가져오기
background = pygame.image.load("/Users/minseok/pythonProject/pygame_basic/background.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("게임을 종료합니다.")

    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0,0,255)) # r g b 로 채우기

    pygame.display.update() # 화면 업데이트