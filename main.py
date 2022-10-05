import pygame
import random
import math
from pygame import mixer

tp = 1
a = 0
flag = 0
pygame.init()
lives = 6
screen = pygame.display.set_mode((800, 600))
# gameover
score = pygame.font.Font('freesansbold.ttf', 64)
# background
background = pygame.image.load('2.jpg')
explosion_Sound = mixer.Sound('1.wav')

# caption and icon
pygame.display.set_caption("BOUNCE")
icon = pygame.image.load('sphere.png')
pygame.display.set_icon(icon)
# crystal
crystalImg = pygame.image.load('crystal.png')
crystalX = random.randint(200, 600)
crystalY = random.randint(100, 500)

# player
playerImg = pygame.image.load('sphere.png')
playerX = random.randint(300, 500)
playerY = random.randint(200, 400)
p = random.randint(1, 100)
if p % 2 == 0:
    playerX_change = random.uniform(0.1, 0.2)
else:
    playerX_change = random.uniform(-0.2, -0.1)
if p % 5 == 0:
    playerY_change = random.uniform(-0.2, -0.1)
else:
    playerY_change = random.uniform(0.1, 0.2)

# BAR 1
barImg1 = pygame.image.load('rectangle.png')
bar1X = 0
bar1Y = 300
bar1X_change = 0
bar1Y_change = 0

# BAR 2
barImg2 = pygame.image.load('rectangle.png')
bar2X = 729
bar2Y = 100
bar2X_change = 0
bar2Y_change = 0

# BAR 3
barImg3 = pygame.image.load('rectangle1.png')
bar3X = 400
bar3Y = 0
bar3X_change = 0
bar3Y_change = 0

# BAR 4
barImg4 = pygame.image.load('rectangle1.png')
bar4X = 400
bar4Y = 540
bar4X_change = 0
bar4Y_change = 0
# score
score_value = 10
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
varr = 0
count = 1
t = 10
f = 0


def show_congo():
    con = font.render("   STEADY STATE REACHED", True, (220, 220, 255))
    screen.blit(con, (180, 270))


def show_lives():
    liv = font.render("lives :" + str(lives), True, (220, 220, 255))
    screen.blit(liv, (650, 10))


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (220, 220, 255))
    screen.blit(score, (x, y))


def show_result(tt):
    if tt > 0:
        result = font.render("Seady State in " + str(tt), True, (220, 220, 255))
        screen.blit(result, (275, 270))


def player(x5, y5):
    screen.blit(playerImg, (x5, y5))


def crystal(x6, y6):
    screen.blit(crystalImg, (x6, y6))


def bar1(x1, y1):
    screen.blit(barImg1, (x1, y1))


def bar2(x2, y2):
    screen.blit(barImg2, (x2, y2))


def bar3(x3, y3):
    screen.blit(barImg3, (x3, y3))


def bar4(x4, y4):
    screen.blit(barImg4, (x4, y4))


def game_over_text():
    score = font.render("GAME OVER ", True, (220, 220, 255))
    screen.blit(score, (315, 265))
    retry = font.render("Press r for retry", True, (220, 220, 255))
    screen.blit(retry,(300,300))


def iscollision(x, y):
    distance = math.sqrt(math.pow((playerX - crystalX), 2) + (math.pow((playerY - crystalY), 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and flag == 1:
            if event.key == pygame.K_r:
                flag = 0
                lives = 6
                score_value = 10
                playerX = random.randint(300, 500)
                playerY = random.randint(200, 400)
                p = random.randint(1, 100)
                if p % 2 == 0:
                    playerX_change = random.uniform(0.1, 0.2)
                else:
                    playerX_change = random.uniform(-0.2, -0.1)
                if p % 3 == 0:
                    playerY_change = random.uniform(-0.2, -0.1)
                else:
                    playerY_change = random.uniform(0.1, 0.2)

        if event.type == pygame.KEYDOWN and flag == 0:
            if event.key == pygame.K_a:
                bar4X_change = 0.35

            if event.key == pygame.K_LEFT:
                bar3X_change = 0.35

            if event.key == pygame.K_d:
                bar4X_change = -0.35

            if event.key == pygame.K_RIGHT:
                bar3X_change = -0.35

            if event.key == pygame.K_UP:
                bar2Y_change = 0.35

            if event.key == pygame.K_w:
                bar1Y_change = 0.35

            if event.key == pygame.K_DOWN:
                bar2Y_change = -0.35

            if event.key == pygame.K_s:
                bar1Y_change = -0.35

        if event.type == pygame.KEYUP and flag == 0:
            bar1Y_change = 0
            bar1X_change = 0
            bar2Y_change = 0
            bar2X_change = 0
            bar3Y_change = 0
            bar3X_change = 0
            bar4Y_change = 0
            bar4X_change = 0

    bar1Y -= bar1Y_change
    bar2Y -= bar2Y_change
    bar3X -= bar3X_change
    bar4X -= bar4X_change

    if bar1Y < 0:
        bar1Y = 0
    if bar1Y > 537:
        bar1Y = 537
    if bar2Y < 0:
        bar2Y = 0
    if bar2Y > 537:
        bar2Y = 537

    if bar3X < 0:
        bar3X = 0
    if bar3X > 727:
        bar3X = 727
    if bar4X < 0:
        bar4X = 0
    if bar4X > 727:
        bar4X = 727

    playerX += playerX_change
    playerY += playerY_change
    if playerY > 542:
        if playerX > bar4X - 4 and playerX < bar4X + 68:
            playerY_change *= -1
            playerX_change -= (bar4X_change / 4)
            score_value += 1
            count += 1
            explosion_Sound.play()
            lives = lives + 2

        else:
            if flag == 0:
                lives -= 1
            playerY_change *= -1

            if flag == 0:
                score_value -= 1
                count = 0

    if playerY < 41:
        if playerX > bar3X - 4 and playerX < bar3X + 68:
            playerX_change -= (bar3X_change / 4)
            playerY_change *= -1
            score_value += 1
            count += 1
            lives = lives + 2
            explosion_Sound.play()
        else:
            if flag == 0:
                lives -= 1
            playerY_change *= -1

            if flag == 0:
                score_value -= 1
                count = 0

    if playerX > 724:
        if playerY > bar2Y - 4 and playerY < bar2Y + 68:
            playerY_change -= (bar2Y_change / 4)
            playerX_change *= -1
            score_value += 1
            count += 1
            lives = lives + 2

            explosion_Sound.play()
        else:
            if flag == 0:
                lives -= 1
            playerX_change *= -1
            if flag == 0:
                score_value -= 1
                count = 0

    if playerX < 41:
        if playerY > bar1Y - 4 and playerY < bar1Y + 68:
            playerY_change -= (bar1Y_change / 4)
            playerX_change *= -1
            score_value += 1
            count += 1
            lives = lives + 2
            explosion_Sound.play()
        else:
            if flag == 0:
                lives -= 1
            playerX_change *= -1
            if flag == 0:
                score_value -= 1
                count = 0

    if count > 6 and bar1Y_change == 0 and bar2Y_change == 0 and bar3X_change == 0 and bar4X_change == 0:
        if f == 0:
            show_result(round(t, 0))
            t = t - 0.001
            if t < 0:
                score_value += 100
                f = 1

    if f == 1:
        show_congo()
        if a == 0:
            playerX_change += random.uniform(0.6, 0.8)
            playerY_change += random.uniform(0.6, 0.8)
            a = 1
        t = 10
        count = 0

    if bar1Y_change != 0 or bar2Y_change != 0 or bar3X_change != 0 or bar4X_change != 0:
        count = 0
        t = 10
    if score_value < -10 or lives < 1:
        game_over_text()
        flag = 1
        playerX_change = 0
        playerY_change = 0
        bar1Y_change = 0
        bar3X_change = 0
        bar2Y_change = 0
        bar4X_change = 0

    if playerX_change < 0:
        playerX_change -= varr
    else:
        playerX_change += varr
    if playerY_change < 0:
        playerY_change -= varr
    else:
        playerY_change += varr
    collision = iscollision(playerX, playerY)
    if collision:
        lives = lives + 6
        Bonus_Sound = mixer.Sound('2.wav')
        Bonus_Sound.play()
        score_value += 10
        crystalX = random.randint(200, 600)
        crystalY = random.randint(100, 500)
        playerX_change *= 1.4
        playerY_change *= 1.4

    crystal(crystalX, crystalY)
    player(playerX, playerY)
    show_score(textX, textY)
    show_lives()
    bar1(bar1X, bar1Y)
    bar2(bar2X, bar2Y)
    bar3(bar3X, bar3Y)
    bar4(bar4X, bar4Y)

    pygame.display.update()
