import pygame
import sys
from time import sleep
from random import *
from pygame import Rect

# 충돌 감지 함수 정의
# 입력 매개변수로 Rect형 변수 두개를 넣는다
def collide(rect1, rect2):
    # x축에서 충돌을 감지했다면
    if (rect1.right >= rect2.left and rect1.left <= rect2.right) \
        or (rect2.right >= rect1.left and rect2.left <= rect1.right):
        if (rect1.bottom >= rect2.top and rect1.top <= rect2.bottom) \
            or (rect2.bottom >= rect1.top and rect2.top <= rect1.bottom):
            return True
    return False


pygame.init() # 초기화 시키기


screen_width = 600
screen_height = 450

screen = pygame.display.set_mode((screen_width,screen_height))
SURFACE = pygame.display.set_mode((400,500))
FPSCLOCK = pygame.time.Clock()
#세부 내용
Round = 4
goal = 10
gsx = screen_width / 2
gsy = screen_height - 20
cloud_img = pygame.image.load("./cloud.png")
cloudPosX = (int(random()* 400) + 0)
cloudPosY = -50
cloud_width = 120
cloud_height = 100
cloud_img = pygame.transform.scale(cloud_img, (cloud_width, cloud_height))

aircraft_img = pygame.image.load("./aircraft.png")
aircraftPosX = 70
aircraftPosY = 400
aircraft_width = 100
aircraft_height = 100
aircraft_img = pygame.transform.scale(aircraft_img, (aircraft_width, aircraft_height))

Text_img = pygame.image.load("./Text1.png")
TextPosX = 30
TextPosY = 20
Text_width = 300
Text_height = 60
Text_img = pygame.transform.scale(Text_img, (Text_width, Text_height))

cloud2_img = pygame.image.load("./airplane-1295845.png")
cloud2PosX = 350
cloud2PosY = -70
cloud2_width = 50
cloud2_height = 50
cloud2_img = pygame.transform.scale(cloud2_img, (cloud2_width, cloud2_height))

cloud2_img = pygame.image.load("./cloud.png")
cloud2PosX = 30
cloud2PosY = 0
cloud2_width = 70
cloud2_height = 70
cloud2_img = pygame.transform.scale(cloud2_img, (cloud2_width, cloud2_height))

#Spitfire(스핏파이어 전투기)
Spitfire_img = pygame.image.load("./pngwing.com.png")
spitfire_width = 70
spitfire_height = 70
Spitfire_img = pygame.transform.scale(Spitfire_img, (spitfire_width, spitfire_height))
spitfire_pos_x = 180
spitfire_pos_y = 180
bslist = []
bsV = 5
bsw = 5
bsh = 5
#Abro Lancaster I(아브로 랭커스터 폭격기)
Lancaster_img = pygame.image.load("./pngegg (1).png")
LancasterPosX = 350
LancasterPosY = -70
Lancaster_width = 100
Lancaster_height = 100
Lancaster_img = pygame.transform.scale(Lancaster_img, (Lancaster_width, Lancaster_height))
lx = 180
ly = 210
lw = 40
lh = 80
LHP = 100
Hx = 170
Hy = 460
Hw = 200
Hh = 35
#BF109((독일)전투기)
enemy_img = pygame.image.load("./pngegg.png")
enemy_width = 70
enemy_height = 70
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))
fw_img = pygame.image.load("./pngegg (3).png")
fw_width = 70
fw_height = 70
fw_img = pygame.transform.scale(fw_img, (fw_width, fw_height))
bs_img = pygame.image.load("./pngegg (3).png")
bs_width = 80
bs_height = 80
bs_img = pygame.transform.scale(bs_img, (bs_width, bs_height))
bx = 210
by = 0
bw = 70
bh = 70

bx2 = 210
by2 = -200
bw2= 70
bh2 = 70
bx3 = 210
by3 = -500
bw3 = 70
bh3 = 70
bsx = 190
bsy = 20
enemy_dirAD = 1
bflist = []
bullet_speed = 2

bfw = 10
bfh = 10


# 적기 왼쪽 위치 최소값, 적기 오른쪽 위치 최대값
EPOSX = (10, 390) 

ep1 = [randint(EPOSX[0],EPOSX[1]), randint(-250, -50)]
ep2 = [randint(EPOSX[0],EPOSX[1]), randint(-500, -250)]
ep3 = [randint(EPOSX[0],EPOSX[1]), randint(-750, -500)]
ep4 = [randint(EPOSX[0],EPOSX[1]), randint(-1000, -750)]
bullets = []
start_time = 0
rx = 0
enemy_speed = [1, 1]
enemy_dir = 0
enemy_list = [
[ep1, enemy_dir, bullets, start_time, rx], 
[ep2, enemy_dir, bullets, start_time, rx],
[ep3, enemy_dir, bullets, start_time, rx],
[ep4, enemy_dir, bullets, start_time, rx]
]



pygame.display.set_caption("Mission Spitfire")
#변수 이후...

# FPS 설정
clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(100) # 프래임
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    #BF109 좌우 이동
        # 시작위치및 이동
        for i in range(len(enemy_list)):
            # 방향이 결정되지 않았을때(0)만 주사위를 던져 방향을 정한다
            if enemy_list[i][1] == 0:
                # 최소 위치~최대 위치값 사이에 주사위를 던진다
                rx = randint(EPOSX[0], EPOSX[1])
                #만약 내 전투기가 적기랑 충돌했다면
                
                # 만약 주사위값이 현재 적기 위치보다 왼쪽이라면
                # 방향을 왼쪽(-1)으로 설정해준다
                if rx < enemy_list[i][0][0]:
                    enemy_list[i][1] = -1
                elif rx > enemy_list[i][0][0]:
                    enemy_list[i][1] = 1
            # 만약 갈 방향이 왼쪽이라면
            # 적기의 이동 속도만큼 빼준다
            if enemy_list[i][1] == -1:
                enemy_list[i][0][0] -= enemy_speed[0]
            # 만약 갈 방향이 오른쪽이라면
            # 적기의 이동 속도만큼 더해준다
            elif enemy_list[i][1] == 1:
                enemy_list[i][0][0] += enemy_speed[0]

            spitfireRect = Rect(spitfire_pos_x, spitfire_pos_y, spitfire_width, spitfire_height)
            enemyRect = Rect(enemy_list[i][0][0], enemy_list[i][0][1], enemy_width, enemy_height) 
            print(spitfireRect, enemyRect)
            if collide(spitfireRect, enemyRect):
                running = False


            # 만약 적기가 이동 방향에 대해 목적지에 이르렀다면,
            # 적기의 이동방향을 초기화해준다
            if abs(enemy_list[i][0][0] - rx) < 1:
                enemy_list[i][1] = 0


        # 적기 리스폰
        for i in range(len(enemy_list)):
            if 500 < enemy_list[i][0][1] :
                enemy_list[i][0][1] = 0
                enemy_list[i][0][0] = randint(0, 300)
    if Round > 0: #적기 총 발사
        for i in range(len(enemy_list)):
            if pygame.time.get_ticks() - enemy_list[i][3] > 1000:
                enemy_list[i][2].append ([enemy_list[i][0][0]+29,enemy_list[i][0][1]+50])
                enemy_list[i][3] = pygame.time.get_ticks()

    # 각 적기의 움직임 
    for i in range(len(enemy_list)):
        enemy_list[i][0][1] += enemy_speed[1]

    # 각 적기에 대하여 총알 움직임 
    for i in range(len(enemy_list)):
        for j in range(len(enemy_list[i][2])):
            enemy_list[i][2][j][1] += bullet_speed

    # 각 적기에 대하여 화면 넘어간 총알 리스트에서 제거
    for i in range(len(enemy_list)):
        for j in range(len(enemy_list[i][2])):
            if 500 > enemy_list[i][2][0][1]:
                del enemy_list[i][2][0]

        #구름이 만약 맵 밖으로 나갔다면...
        if 500 < cloudPosY :
            cloudPosY = 0
            cloudPosX = randint(0,400)
            cloud_height = randint(80,280)
            cloud_width = randint(90,300)

        if 500 < cloud2PosY :
            cloud2PosY = 0
            cloud2PosX = randint(0,400)
            cloud2_height = randint(80,280)
            cloud2_width = randint(90,300)

    # 키보드를 누르고 있는지를 알려주는 함수
    keys = pygame.key.get_pressed()
    #랭커스터,스핏파이어 관련 키보드 이벤트
    if keys[pygame.K_LEFT]: #왼쪽으로 이동
        if Round > 0:
            if spitfire_pos_x > 10:
                spitfire_pos_x -= 6
            if lx > 10:
                lx -= 4
    elif keys[pygame.K_RIGHT]:#오른쪽으로 이동
        if Round > 0:
            if spitfire_pos_x < 390:
                spitfire_pos_x += 6
            if lx < 390:
                lx += 4
    
    elif keys[pygame.K_DOWN]:#뒤로 이동
        if Round > 0:
            spitfire_pos_y += 4
            ly += 4
    elif keys[pygame.K_UP]:#앞로 이동
        if Round > 0:
            if spitfire_pos_y > 30:
                spitfire_pos_y -= 4
                ly -= 4


    elif keys[pygame.K_SPACE]:#총 발사
        bslist.append ([spitfire_pos_x+29,spitfire_pos_y])

    for i in range(len(bslist)):
        bslist [i][1] -= bsV
    
    for i in range (len(bslist)):
        if 0 > bslist[0][1]:
            del bslist[0]
    

    #배경
    screen.fill((0,0,255))
    #랭커스터
    screen.blit(Lancaster_img, (lx,ly))
    #구름
    screen.blit(cloud_img, (cloudPosX,cloudPosY))
    screen.blit(cloud2_img, (cloud2PosX,cloud2PosY))
    screen.blit(cloud_img, (cloudPosX,cloudPosY))
    screen.blit(cloud2_img, (cloud2PosX,cloud2PosY))
    #스핏파이어
    screen.blit(Spitfire_img, (spitfire_pos_x,spitfire_pos_y))
    for b in bslist:
        bRect = pygame.Rect(b[0]+5,b[1],bsw,bsh)
        pygame.draw.rect(SURFACE, (255,120,120),bRect, 0)
        
    
    #독일 전투기
    for enemy in enemy_list:
        screen.blit(enemy_img, enemy[0])
        for bullet in enemy[2]:
            bfRect = pygame.Rect(bullet[0]+5,bullet[1],bfw,bfh)
            pygame.draw.rect(SURFACE, (255,0,0),bfRect, 0)
        
    #디테일
    screen.blit(aircraft_img, (aircraftPosX,aircraftPosY))
    pygame.draw.rect(SURFACE, (0,0,0),(0,410,80,80))
    pygame.draw.rect(SURFACE, (0,255,0),(Hx,Hy,Hw,Hh))
    
    if Round == 0: screen.blit(Text_img, (TextPosX,TextPosY))
    if Round == 0: screen.blit(cloud_img, (cloudPosX,cloudPosY))
    pygame.display.update()

    if Round > 0:cloudPosY += 0.4
    if Round > 0:cloud2PosY += 0.4

    if Round == 0:
        sleep(3.5)
        Round = 1
    FPSCLOCK.tick(80)
pygame.quit()