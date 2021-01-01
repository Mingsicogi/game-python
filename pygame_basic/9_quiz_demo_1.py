# 똥 피하기 게임

import pygame
import schedule
import random

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

# speed
character_speed = 2.5
ddong_speed = 5

class Ddong:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.image_width = image.get_width()
        self.image_height = image.get_height()
        self.random_drop_speed = random.randrange(1, ddong_speed)

# images
character = pygame.image.load("/Users/minseok/pythonProject/pygame_basic/character.png")
ddong_image = pygame.image.load("/Users/minseok/pythonProject/pygame_basic/ddong.png")

# size of images
character_width = character.get_width()
character_height = character.get_height()

# position
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
ddong = Ddong(ddong_image, random.randrange(0, screen_width - ddong_image.get_width()), 0)
ddong_list = [ddong]

# font
score_font = pygame.font.Font(None, 80)
game_over_font = pygame.font.Font(None, 100)

# text data
score = 0
reward_basic_score = 100
game_over_text = "GAME OVER"
game_start = True
running = True

# level
level = 1 # 초기 난이도 셋팅. time ticker가 발동되는 간격임(2^11)
level_increase_interval = 10 # 10번 피하면 레벨업이 됨
ddong_count_by_level = 5

# 화면에 그리기
def game_start_draw_screen(character_x_pos, character_y_pos):
    screen.fill((0, 0, 255)) # 흰색 배경
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터
    screen.blit(score_font.render(str(score), True, (0,0,0)), (screen_width - 100, 20)) # 점수표
    
    for d in ddong_list: # 똥 리스트
        screen.blit(d.image, (d.x, d.y))

# 레벨 난이도에 따라 똥 갯수를 검사하고 생성함
def check_ddong_count(score, level):
    if score > 0 and score % (reward_basic_score * level_increase_interval * level) == 0: # 레벨 마다 지정된 횟수를 피하면 레벨업.
        for i in range((ddong_count_by_level * (level + 1)) - len(ddong_list)):
            new_ddong =  Ddong(ddong_image, random.randrange(0, screen_width - ddong_image.get_width()), 0)
            ddong_list.append(new_ddong)
        
        print("level up", str(level + 1))
        return level + 1
    
    return level

# 현재 케릭터 위치와 똥의 충돌체크
def check_collision(character, ddong_list):
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for d in ddong_list:
        d_rect = d.image.get_rect()
        d_rect.left = d.x
        d_rect.top = d.y
        if character_rect.colliderect(d_rect):
            return True

    return False

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
        for d in ddong_list:
            d.y += d.random_drop_speed
            if d.y > screen_height: # 똥피하기 성공(똥 위치 초기화, 점수 획득)
                d.x = random.randrange(0, screen_width - d.image_width)
                d.y = 0
                d.random_drop_speed = random.randrange(1, ddong_speed)
                score += reward_basic_score

        # 레벨 마다 사용되는 똥의 갯수 확인 후 생성
        level = check_ddong_count(score, level)

        # 충돌 처리
        if check_collision(character, ddong_list):
            screen.fill((0, 0, 0))
            screen.blit(game_over_font.render(game_over_text, True, (255, 0, 0)), (screen_width * 0.05, screen_height * 0.4))
            score = 0
            running = False
        else:
            game_start_draw_screen(character_x_pos, character_y_pos)

        pygame.display.update() # 화면 업데이트
    
    # Game Over 화면에서 핸들링을 위한 처리
    event = pygame.event.wait(1000)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            character_x_pos = (screen_width / 2) - (character_width / 2)
            character_y_pos = screen_height - character_height
            
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos

            ddong = Ddong(ddong_image, random.randrange(0, screen_width - ddong_image.get_width()), 0)
            ddong_rect = ddong_image.get_rect()
            ddong_rect.left = ddong.x
            ddong_rect.top = ddong.y
            ddong_list = [ddong]

            game_start_draw_screen((screen_width / 2) - (character_width / 2), screen_height - character_height)
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