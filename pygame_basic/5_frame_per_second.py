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

    screen.blit(background,(0,0)) #배경 그리기
    
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    
    pygame.display.update() #게임 화면을 다시 그리기 계속 반복
#pygame 종료
pygame.quit()