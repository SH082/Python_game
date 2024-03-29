import pygame
import random

pygame.init() #초기화 

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Quiz") #게임 이름

#FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 죄표, 속도, 폰트 등 설정)

#배경 이미지 불러오기
background = pygame.image.load("/Users/ksh/Desktop/python/pygame/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/ksh/Desktop/python/pygame/character.png")
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = screen_width/2- character_width/2 #화면 가로 절반 크기 아래
character_y_pos = screen_height - character_height #화면 세로 절반 크기 아래

#이동할 좌표
to_x = 0

#이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/ksh/Desktop/python/pygame/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기 구해옴
enemy_width = enemy_size[0] #캐릭터 가로 크기
enemy_height = enemy_size[1] #캐릭터 세로 크기

# 무작위로 적의 초기 위치 설정
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

# 이벤트 루프
running = True #게임이 진행중인가?

while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #게임 진행중이 아님
            running = False
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x-= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터를 위로
                to_x+= character_speed

        if event.type ==pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    character_x_pos += to_x * dt

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

    #요소 그리기
    screen.blit(background,(0,0)) #배경 그리기
    
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기

     # 적의 위치 업데이트
    enemy_y_pos += 10  # 적의 속도를 조절할 수 있습니다.

    # 적이 화면 아래로 사라지면 새로운 적 생성
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0

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

    pygame.display.update() #게임 화면을 다시 그리기 계속 반복

#잠시 대기
pygame.time.delay(500) #2초 정도 대기 (ms)

#pygame 종료
pygame.quit()