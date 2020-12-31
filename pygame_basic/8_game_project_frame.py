import pygame

############################# 기본 초기화 값 ###############################################
pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Mins Game")

# 반복적으로 key event를 발생시킬지 설정. 인자값은 얼마를 주기로 반복시킬지 설정.
pygame.key.set_repeat(10)

# FPS
clock = pygame.time.Clock()
########################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)


running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        # 3. 게임 캐릭터 위치 정의

        # 4. 충돌 처리

        # 5. 화면에 그리기

        pygame.display.update() # 화면 업데이트

# pygame 종료
pygame.quit()