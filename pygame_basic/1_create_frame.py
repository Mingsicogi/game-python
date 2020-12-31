import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Mins Game")


# 이벤트 루프
running = True # 게임이 진행중인지 여부
while running:
    for event in pygame.event.get(): # 사용자의 이벤트를 계속 얻어옴
        if event.type == pygame.QUIT:
            print("게임을 종료합니다.")
            running = False



# pygame 종료
pygame.quit()