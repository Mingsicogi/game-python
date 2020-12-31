import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Mins Game")

# 배경화면 이미지 가져오기
background = pygame.image.load("/Users/minseok/pythonProject/pygame_basic/background.jpg")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/minseok/pythonProject/pygame_basic/character.jpg")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면의 가로 중앙에서 캐릭터의 절반 만큼을 빼서 가운데에 위치 시킴
character_y_pos = screen_height - character_height # 화면의 세로 사이즈에서 캐릭터 이미지 만큼 올라 오게 위치 셋팅

# 캐릭터가 이동하는 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중인지 여부
while running:
    for event in pygame.event.get(): # 사용자의 이벤트를 계속 얻어옴
        print(event)

        if event.type == pygame.QUIT:
            print("게임을 종료합니다.")
            running = False

        if event.type == pygame.KEYDOWN: # 키보드 이벤트인지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

        character_x_pos += to_x # 이동이 있으면 이동한 만큼 케릭터 x좌표를 움직임
        if character_x_pos < 0: # x가 0 보다 작은 위치면 0으로 돌림. 경계값 처리
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        character_y_pos += to_y # 이동이 있으면 이동한 만큼 케릭터 y좌표를 움직임
        if character_y_pos < 0: # y가 0 보다 작은 위치면 0으로 돌림. 경계값 처리
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

        screen.blit(background, (0, 0)) # 배경 그리기
        # screen.fill((0,0,255)) # r g b 로 채우기

        screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

        pygame.display.update() # 화면 업데이트


# pygame 종료
pygame.quit()