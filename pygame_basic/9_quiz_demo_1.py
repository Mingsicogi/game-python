# 똥 피하기 게임

import pygame
import random

############################# 기본 초기화 값 ###############################################
pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# 반복적으로 key event를 발생시킬지 설정. 인자값은 얼마를 주기로 반복시킬지 설정.
pygame.key.set_repeat(10)

# FPS
clock = pygame.time.Clock()
frames = 30
########################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# images
character = pygame.image.load("/Users/minseok/pythonProject/pygame_basic/character.png")
ddong = pygame.image.load("/Users/minseok/pythonProject/pygame_basic/ddong.png")

# size of images
character_width = character.get_width()
character_height = character.get_height()
ddong_width = ddong.get_width()
ddong_height = ddong.get_height()

# position
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
ddong_x_pos = random.randrange(0, screen_width - ddong_width)
ddong_y_pos = 0

# speed
character_speed = 2.5
ddong_speed = 5

# font
score_font = pygame.font.Font(None, 80)
game_over_font = pygame.font.Font(None, 100)

# text data
score = 0
reward_basic_score = 100
game_over_text = "GAME OVER"
game_start = True
running = True

# 화면에 그리기
def game_start_draw_screen(character_x_pos, character_y_pos ,ddong_x_pos, ddong_y_pos):
    screen.fill((0, 0, 255)) # 흰색 배경
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    screen.blit(score_font.render(str(score), True, (0,0,0)), (screen_width - 100, 20))

while game_start:
    while running:
        dt = clock.tick(frames)

        # 이벤트 처리(키보드)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_start = False
            
            # 게임 캐릭터 위치 정의
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_x_pos -= character_speed
                if event.key == pygame.K_RIGHT:
                    character_x_pos += character_speed
                else:
                    pass

            # 게임 캐릭터의 경계 처리
            if character_x_pos < 0:
                character_x_pos = 0
            elif character_x_pos > screen_width - character_width:
                character_x_pos = screen_width - character_width

        # 매 루프마다 똥을 이동시킴
        ddong_y_pos += ddong_speed
        if ddong_y_pos > screen_height: # 똥피하기 성공(똥 위치 초기화, 점수 획득)
            ddong_x_pos = random.randrange(0, screen_width - ddong_width)
            ddong_y_pos = 0
            score += reward_basic_score

        # 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        ddong_rect = ddong.get_rect()
        ddong_rect.left = ddong_x_pos
        ddong_rect.top = ddong_y_pos

        if character_rect.colliderect(ddong_rect): # game over
            screen.fill((0, 0, 0))
            screen.blit(game_over_font.render(game_over_text, True, (255, 0, 0)), (screen_width * 0.05, screen_height * 0.4))
            score = 0
            running = False
        else:
            game_start_draw_screen(character_x_pos, character_y_pos, ddong_x_pos, ddong_y_pos)

        pygame.display.update() # 화면 업데이트
    
    
    event = pygame.event.wait(1000)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            character_x_pos = (screen_width / 2) - (character_width / 2)
            character_y_pos = screen_height - character_height
            ddong_x_pos = random.randrange(0, screen_width - ddong_width)
            ddong_y_pos = 0
            
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos

            ddong_rect = ddong.get_rect()
            ddong_rect.left = ddong_x_pos
            ddong_rect.top = ddong_y_pos

            game_start_draw_screen((screen_width / 2) - (character_width / 2), screen_height - character_height, ddong_rect.left, ddong_rect.top)
            running = True
            game_start = True
            
        elif event.key == pygame.K_ESCAPE:
            game_start = False
            running = False

    elif event.type == pygame.QUIT:
        running = False
        game_start = False

# pygame 종료
pygame.quit()



