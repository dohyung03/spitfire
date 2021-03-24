import pygame
import sys
from time import sleep
from random import *

pygame.init() # 초기화 시키기

screen_width = 600
screen_height = 450

screen = pygame.display.set_mode((screen_width,screen_height))
SURFACE = pygame.display.set_mode((400,500))
FPSCLOCK = pygame.time.Clock()
#세부 내용
Round = 0
goal = 10
gsx = screen_width / 2
gsy = screen_height - 20
cloud_img = pygame.image.load("/home/hcl/dohyung/python/Ptgame_basic/cloud.png")
cloudPosX = (int(random()* 400) + 0)
cloudPosY = -50
cloud_width = 120
cloud_height = 100
cloud_img = pygame.transform.scale(cloud_img, (cloud_width, cloud_height))

aircraft_img = pygame.image.load("/home/hcl/dohyung/python/Ptgame_basic/aircraft.png")
aircraftPosX = 70
aircraftPosY = 400
aircraft_width = 100
aircraft_height = 100
aircraft_img = pygame.transform.scale(aircraft_img, (aircraft_width, aircraft_height))

Text_img = pygame.image.load("/home/hcl/dohyung/python/Ptgame_basic/Text1.png")
TextPosX = 30
TextPosY = 20
Text_width = 300
Text_height = 60
Text_img = pygame.transform.scale(Text_img, (Text_width, Text_height))

cloud2_img = pygame.image.load("/home/hcl/dohyung/python/Ptgame_basic/__pycache__/airplane-1295845.png")
cloud2PosX = 350
cloud2PosY = -70
cloud2_width = 50
cloud2_height = 50
cloud2_img = pygame.transform.scale(cloud2_img, (cloud2_width, cloud2_height))

cloud2_img = pygame.image.load("/home/hcl/dohyung/python/Ptgame_basic/cloud.png")
cloud2PosX = 30
cloud2PosY = 0
cloud2_width = 70
cloud2_height = 70
cloud2_img = pygame.transform.scale(cloud2_img, (cloud2_width, cloud2_height))

#Spitfire(스핏파이어 전투기)
Spitfire_img = pygame.image.load("/home/hcl/dohyung/python/Ptgame_basic/pngwing.com.png")
Spitfire_width = 70
Spitfire_height = 70
Spitfire_img = pygame.transform.scale(Spitfire_img, (Spitfire_width, Spitfire_height))
px = 180
py = 180
pw = 15
ph = 50
bslist = []
bsV = 5
bsw = 5
bsh = 5
#Abro Lancaster I(아브로 랭커스터 폭격기)
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
bf_img = pygame.image.load("/home/hcl/dohyung/python/Ptgame_basic/__pycache__/pngegg.png")
bf_width = 70
bf_height = 70
bf_img = pygame.transform.scale(bf_img, (bf_width, bf_height))
bx = 210
by = 0
bw = 15
bh = 40
bx2 = 210
by2 = -200
bw2= 15
bh2 = 40
bx3 = 210
by3 = -500
bw3 = 15
bh3 = 40
bfLEFT = 1
bfLEFTAD = 1
bflist = []
bfV = 7
bfw = 5
bfh = 5
pygame.display.set_caption("Mission Spitfire")

# FPS 설정
clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(100) # 프래임
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            #BF109 좌우 이동
        if bfLEFT == 1 :
            if bx > 10 :
                bx -= (int(random() * 30) + 5)
            bfLEFT -= 1
        if bfLEFT == 0 :
            if bx < 390 :
                bx += (int(random() * 30) + 5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            bfLEFT += 1
        if 500 < by :
            by = 0
            bx = (int(random()* 300) + 0)

        if bfLEFT == 1 :
            if bx2 > 10 :
                bx2 -= (int(random() * 30) + 5)
            bfLEFT -= 1
        if bfLEFT == 0 :
            if bx2 < 390 :
                bx2 += (int(random() * 30) + 5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            bfLEFT += 1
        if 500 < by2 :
            by2 = 0
            bx2 = (int(random()* 300) + 0)

        if bfLEFTAD == 1 :
            if bx3 > 10 :
                bx3 -= (int(random() * 30) + 5)
            bfLEFTAD -= 1
        if bfLEFTAD == 0 :
            if bx3 < 390 :
                bx3 += (int(random() * 30) + 5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            bfLEFTAD += 1
        if 500 < by3 :
            by3 = 0
            bx3 = (int(random()* 300) + 0)

    if Round > 0: #적기 총 발사
        bflist.append ([bx+29,by+20])

    for i in range(len(bflist)):
        bflist [i][1] += bfV
    
    #if 500 > bflist[0][1]: 이 부분에서 맵을 나가면 먼저 발사된 총알을 삭제해야 하기에 [i]가 아니라 처음 발사된 [0]
    #으로 해야한다
    for i in range (len(bflist)):
        if 500 > bflist[0][1]:
            del bflist[0]

        #구름이 만약 맵 밖으로 나갔다면...
        if 500 < cloudPosY :
            cloudPosY = 0
            cloudPosX = (int(random()* 400) + 0)
            cloud_height = (int(random()* 200) + 80)
            cloud_width = (int(random()* 210) + 90)

        if 500 < cloud2PosY :
            cloud2PosY = 0
            cloud2PosX = (int(random()* 400) + 0)
            cloud2_height = (int(random()* 200) + 80)
            cloud2_width = (int(random()* 210) + 90)

    # 키보드를 누르고 있는지를 알려주는 함수
    keys = pygame.key.get_pressed()
    #랭커스터,스핏파이어 관련 키보드 이벤트
    if keys[pygame.K_LEFT]: #왼쪽으로 이동
        if Round > 0:
            if px > 10:
                px -= 3
            if lx > 10:
                lx -= 2
    elif keys[pygame.K_RIGHT]:#오른쪽으로 이동
        if Round > 0:
            if px < 390:
                px += 3
            if lx < 390:
                lx += 2
    
    elif keys[pygame.K_DOWN]:#뒤로 이동
        if Round > 0:
            py += 4
    elif keys[pygame.K_UP]:#앞로 이동
        if Round > 0:
            if py > 30:
                py -= 4


    elif keys[pygame.K_SPACE]:#총 발사
        bslist.append ([px+29,py])

    for i in range(len(bslist)):
        bslist [i][1] -= bsV
    
    for i in range (len(bslist)):
        if 0 > bslist[0][1]:
            del bslist[0]
    

    #배경
    screen.fill((0,0,255))
    #랭커스터
    pygame.draw.rect(SURFACE, (255,0,0),(lx,ly,lw,lh))
    #구름
    screen.blit(cloud_img, (cloudPosX,cloudPosY))
    screen.blit(cloud2_img, (cloud2PosX,cloud2PosY))
    #스핏파이어
    screen.blit(Spitfire_img, (px,py))
    for b in bslist:
        bRect = pygame.Rect(b[0]+5,b[1],bsw,bsh)
        pygame.draw.rect(SURFACE, (255,120,120),bRect, 0)
    #독일 전투기
    if Round > 0:
        screen.blit(bf_img, (bx,by))
        for b in bflist:
                bfRect = pygame.Rect(b[0]+5,b[1],bfw,bfh)
                pygame.draw.rect(SURFACE, (255,0,0),bfRect, 0)
    if Round > 1:
        pygame.draw.rect(SURFACE, (0,255,255),(bx2,by2,bw2,bh2))
    if Round > 2:
        pygame.draw.rect(SURFACE, (0,255,255),(bx3,by3,bw3,bh3))
    #디테일

    screen.blit(aircraft_img, (aircraftPosX,aircraftPosY))
    pygame.draw.rect(SURFACE, (0,0,0),(0,410,80,80))
    pygame.draw.rect(SURFACE, (0,255,0),(Hx,Hy,Hw,Hh))
    
    if Round == 0: screen.blit(Text_img, (TextPosX,TextPosY))
    if Round == 0: screen.blit(cloud_img, (cloudPosX,cloudPosY))
    pygame.display.update()
    if Round > 0:py-= 1
    if Round > 0:by+= 1
    if Round > 1:by2+= 1
    if Round > 2:by3+= 1
    if Round > 0:cloudPosY += 0.4
    if Round > 0:cloud2PosY += 0.4

    if Round == 0:
        sleep(3.5)
        Round = 1
pygame.quit()