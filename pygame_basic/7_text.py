import pygame

pygame.init() #초기화 

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("/Users/ksh/Desktop/python/pygame/background.png")

#FPS
clock = pygame.time.Clock()

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/ksh/Desktop/python/pygame/character.png")
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = screen_width/2- character_width/2 #화면 가로 절반 크기 아래
character_y_pos = screen_height - character_height #화면 세로 절반 크기 아래

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/ksh/Desktop/python/pygame/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기 구해옴
enemy_width = enemy_size[0] #캐릭터 가로 크기
enemy_height = enemy_size[1] #캐릭터 세로 크기
enemy_x_pos = screen_width/2- enemy_width/2 #화면 가로 절반 크기 아래
enemy_y_pos = screen_height/2 - enemy_height/2 #화면 세로 절반 크기 아래

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

#총 시간
total_time = 10

#시작 시간 정보
start_ticks =pygame.time.get_ticks() #시작 tick을 받아옴

# 이벤트 루프
running = True #게임이 진행중인가?

while running:
    dt = clock.tick(60) #게임 화면의 초당 프레임 수 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #게임 진행중이 아님
            running = False
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x-= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터를 위로
                to_x+= character_speed
            elif event.key == pygame.K_UP: #캐릭터를 위로
                to_y-= character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로
                to_y+= character_speed

        if event.type ==pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos <0:
        character_y_pos =0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌 처리를 위한 rect 정보 update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    #타이머 넣기

    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과 시간을 초단위로 환산

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # 출력할 글자, True, 글자 색상

    if int(total_time - elapsed_time) == 0:
        print("시간 초과")
        running = False

    #요소 그리기
    screen.blit(background,(0,0)) #배경 그리기
    
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기

    screen.blit(timer, (10,10))

    pygame.display.update() #게임 화면을 다시 그리기 계속 반복

#잠시 대기
pygame.time.delay(2000) #2초 정도 대기 (ms)

#pygame 종료
pygame.quit()