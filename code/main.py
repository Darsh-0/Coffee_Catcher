import pygame
import math
import time
import random
from pygame.locals import *
from pygame import mixer
import pickle
from os import path

pygame.init()

#colours

light_blue = 173, 216, 230
white = 255,255,255
black = 0,0,0
green = 0, 255, 0
blue = 0,0,255
brown = 103,71,54
red = 255,0,0
grey = 200,200,200
game_over = 0
clock = pygame.time.Clock()

#fonts


font = pygame.font.SysFont('Comic Sans MS', 50, 70)
beforefont = pygame.font.SysFont('Comic Sans MS', 200, 200)
smallfont = pygame.font.SysFont('Comic Sans MS', 30, 200)
supersmallfont = pygame.font.SysFont('Comic Sans MS', 20, 200)
bigfont = pygame.font.SysFont('Comic Sans MS', 100, 70)
mediumfont = pygame.font.SysFont('Comic Sans MS', 35, 70)

#screen
screen_width = 650
screen_height = 800
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Darsh's Game")
pygame.draw.rect(screen,white,(200,150,100,50))

#tips
tipslist = ["get better", "these tips aren't helpful", "don't die", "catch the coffee", "another one bites the dust", "HUH? LETS GO","I don't know what to put here","press space to jump", "these songs are pretty cool","YEA YEA","why are you reading this","George is bad", "Darsh is cool","how did you die?","press the top right corner in the menu", "3.14159265358979323", "move using wasd or arrow keys","my game is better than george's","E = mc^2","Also try Minecraft!","www.youtube.com/watch?v=dQw4w9WgXcQ"]

#player direction and skin
left = False
right = True
skin = 1
playerspeed = 6.5

#jumping
isJump = False
jumpCount = 10

#enemy
enemyx = 1000
enemyleftorright = random.randrange(1,3)
enemyspeedup = 0
enemyslowdown = 3
enemyspeed = 2
anvilturn = 0

#time
end_time = 0

#clouds
num_of_clouds = 10

#speed
jumpcoffeespeed = 1

#gamestart
splashscreen = True
menu = False
game_over = 2

#mute code
mutee = 1
song = 6



#coffee
coffeeaddspeed = 1


#powerup
xx = random.randrange(50, 600)
xy = random.randrange(-300, -100)

#function to draw text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#turns and draws character
def direction(left, right, skin): #changes player direction
    mainright = pygame.image.load(f'newgameimg/players/main{skin}.png')
    if left == True:
        mainleft = pygame.transform.flip(mainright, True, False)
        screen.blit(mainleft,(x, y))
    elif right == True:
        screen.blit(mainright,(x, y))


#draws the buttons on the start screen/menu
def start_buttons(presentskin):
    pygame.draw.rect(screen, light_blue, start_button)
    pygame.draw.rect(screen, brown, quit_button)
    screen.blit(muteorunmute,(65,735))
    draw_text("Start", font, white, 245, 260)
    draw_text("Quit", font, white, 490, 713)
    center_text("Coffee Catcher", brown, 120, font)
    draw_text("Music", font, white, 240, 720)
    screen.blit(presentskin, (270, 400))

#draws the power up buttons
def power_ups():
    screen.blit(button, (150,717))
    screen.blit(button, (315, 717))
    screen.blit(speedbutton, (295, 700))
    screen.blit(coffeebutton, (130, 700))
    screen.blit(coffeesplashscreen, (515, 745))

#draws the falling coffee
def coffee(x, y, i):
    screen.blit(coffeeimage[i], (x, y))

#draws the text centered
def center_text(text,colour, y,whichfont):
    x = whichfont.render(text, True, colour)
    text_rect = x.get_rect(center=(screen_width / 2, y))
    screen.blit(x, text_rect)

#draws the buttons in the end game menu
def endgamebuttons():
    screen.blit(bg, (0, 0))
    screen.blit(arrow_left, (170, 740))
    screen.blit(arrow_right, (360, 740))
    draw_text("You Died!", bigfont, light_blue, 55, 10)
    scoreasfloat = round(((coffees + speeds) * timer)*13,0)
    totalscore = int(scoreasfloat)
    center_text(f"Your Score: {totalscore}", white, 250, mediumfont)
    center_text(f"Time: {timer} seconds", white, 180, mediumfont)
    pygame.draw.rect(screen, light_blue, restart_button)
    draw_text("Restart", font, white, 215, 360)
    pygame.draw.rect(screen, light_blue, end_quit_button)
    draw_text("Menu", font, white, 250, 510)
    draw_text("Music", font, white, 240, 720)

def explosion(animation): #creates the explosion effect when you die
    time.sleep(0.075)
    explosion = pygame.image.load(f"newgameimg/explosion/explosion{animation}.png")
    screen.blit(explosion,(x,y +10))



# imports all the images from the folders

#arrors
arrow_right = pygame.image.load('newgameimg/bg/arrow.png')
arrow_left = pygame.transform.flip(arrow_right, True, False)

#enemys
enemyleft = pygame.image.load('newgameimg/players/enemy.png')
enemyright = pygame.transform.flip(enemyleft, True, False)

anvil = pygame.image.load('newgameimg/enemy/anvil.png')

#backgrounds
bg = pygame.image.load("newgameimg/bg/bg.png")
bgmenu = pygame.image.load("newgameimg/bg/bgmenu.jpeg")
cloud = pygame.image.load("newgameimg/bg/cloud.png")

#misc

mutepng = pygame.image.load("newgameimg/mute/mute.png")
unmutepng = pygame.image.load("newgameimg/mute/unmute.png")


#powerups

x_power_up = pygame.image.load("newgameimg/powerups/2xpowerup.png")
button = pygame.image.load("newgameimg/powerups/button.png")
speedbutton = pygame.image.load("newgameimg/powerups/speed_indicator.png")
coffeebutton = pygame.image.load("newgameimg/powerups/beanup_indicator.png")
coffee_bean = pygame.image.load(f"newgameimg/coffee/bean.png")


#easteregg
main17 = pygame.image.load("newgameimg/players/main17.png")
carspawn = -150


#for mute button
muteorunmute = unmutepng

#pre drawing the buttons
start_button = pygame.draw.rect(screen,(black),(225,250,200,100))
quit_button = pygame.draw.rect(screen,(black),(480,720,153,65))
restart_button = pygame.draw.rect(screen,(black),(200,350,250,100))
end_quit_button = pygame.draw.rect(screen,(black),(200,500,250,100))
random_button = pygame.draw.rect(screen,(black),(225,550,200,100))

#sound effects
effect = pygame.mixer.Sound('newgameimg/sounds/effect.wav')
death = pygame.mixer.Sound('newgameimg/sounds/deathsound.wav')
bonk = pygame.mixer.Sound('newgameimg/sounds/bonksound.wav')
powerupsound = pygame.mixer.Sound('newgameimg/sounds/powerup.wav')
loading = pygame.mixer.Sound('newgameimg/sounds/loading.wav')


coffeesplashscreen = pygame.image.load('newgameimg/coffee/bean.png')

presentskin = pygame.image.load(f'newgameimg/players/main{skin}.png')
pygame.display.set_icon(coffee_bean)
#game code

splashscreenxspeedup = 2

while splashscreen:
    clock.tick(60)
    skinrandom = random.randrange(1, 14)
    splashskin = pygame.image.load(f'newgameimg/players/main{skinrandom}.png')
    screen.fill((231, 205, 183))
    pygame.display.update()
    time.sleep(0.5)
    # fill the start message on the top of the game
    loading.play()
    startMessage = smallfont.render("Darsh Presents", True, (171, 145, 123))
    screen.blit(startMessage, (screen.get_width() / 2 - startMessage.get_width() / 2, 200))

    # update display
    pygame.display.update()
    # wait for 10 seconds
    time.sleep(1.5)
    loading.play()
    center_text("Coffee Catcher", brown, 120, font)
    pygame.display.update()

    time.sleep(1.5)

    splashscreenx = -40
    splashscreeny = 600

    for i in range(300):
        time.sleep(0.005)
        screen.fill((231, 205, 183))
        center_text("Coffee Catcher", brown, 120, font)
        screen.blit(startMessage, (screen.get_width() / 2 - startMessage.get_width() / 2, 200))
        splashscreenx += splashscreenxspeedup
        screen.blit(splashskin,(splashscreenx,splashscreeny))


        if i <= 130:
            screen.blit(coffeesplashscreen,(screen.get_width()/2 - coffeesplashscreen.get_width()/2, 360))

        if i == 130:
            effect.play()


        if i >= 120 and i <= 140:
            splashscreenxspeedup = 4
            if jumpCount >= -10:
                time.sleep(0.01)
                splashscreeny -= (jumpCount * abs(jumpCount)) * 0.75
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False  # jumping code
                splashscreenxspeedup = 2
        pygame.display.update()


    m = pygame.mixer.music.load(f'newgameimg/sounds/music{song}.wav')
    pygame.mixer.music.play(-1)
    menu = True
    splashscreen = False

while menu:
    clock.tick(60)
    if game_over == 2: #game menu
        start_time = pygame.time.get_ticks()
        screen.blit(bgmenu, (0, 0)) #draw background

        keys = pygame.key.get_pressed()
        start_buttons(presentskin)
        mx, my = pygame.mouse.get_pos() #gets the mouse postion
        screen.blit(arrow_left, (200, 440))
        screen.blit(arrow_right, (330, 440))
        screen.blit(arrow_left, (170, 740))
        screen.blit(arrow_right, (360, 740))

        if skin == 14:
            skin = 1
        if skin == 0:
            skin = 13
        if skin == 16 or skin == 18:
            skin = 1





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False


            if mx >= 600 and mx <= 850 and my >= 0 and my <= 20 and event.type == pygame.MOUSEBUTTONUP: #gets x and y of mouse to check if it is on the button
                skin = 17
                music = pygame.mixer.music.load(f'newgameimg/sounds/music10.wav')
                pygame.mixer.music.play(-1)
                if mutee == 1:
                    pygame.mixer.music.unpause()
                elif mutee == 0:
                    pygame.mixer.music.pause()







            if keys[pygame.K_ESCAPE]: #game quit
                menu = False
            if mx >= 225 and mx <= 445 and my >= 250 and my <= 350 and event.type == pygame.MOUSEBUTTONUP: #gets x and y of mouse to check if it is on the button

                #this code starts the game

                score = 0
                speedcost = 5
                speeds = 1
                coffeecost = 10
                coffees = 1
                coffeefallspeed = 2.5
                speed = playerspeed
                y = 595
                x = 25
                xx = random.randrange(50, 600)
                xy = random.randrange(-300, -100)
                anvilx = random.randrange(50, 600)
                anvily = random.randrange(-300, -100)
                coffeeaddspeed = 1
                jumpCount = 10

                #spawns the clouds

                cloudx = []
                cloudy = []
                cloudimage = []
                cloudx_change = []
                for i in range(num_of_clouds):
                    cloudimage.append(pygame.image.load("newgameimg/bg/cloud.png"))
                    cloudx.append(random.randrange(-200, 700))
                    cloudy.append(random.randrange(10, 300))
                    cloudx_change.append(1)



                game_over = 0
                enemyx = 998
                enemyspeedup = 0
                isJump = False
                coffeeimage = []
                coffeex = []
                coffeey = []
                coffeey_change = []
                num_of_coffee = 1
                for i in range(num_of_coffee):
                    turn = random.randrange(1, 361)
                    coffeeimage.append(pygame.transform.rotate(coffee_bean, turn))
                    coffeex.append(random.randrange(0, 600))
                    coffeey.append(random.randrange(-250, -45))
                    coffeey_change.append(coffeefallspeed)




            if mx >= 480 and mx <= 633 and my >= 720 and my <= 785 and event.type == pygame.MOUSEBUTTONUP: #quit button
                menu = False
            if mx >= 65 and mx <= 109 and my >= 739 and my <= 788 and event.type == pygame.MOUSEBUTTONUP or keys[pygame.K_m]: #this is for muting the game music
                if mutee == 1:
                    mutee = 0
                    muteorunmute = mutepng
                    pygame.mixer.music.pause()
                elif mutee == 0:
                    mutee = 1
                    muteorunmute = unmutepng
                    pygame.mixer.music.unpause()
            if mx >= 245 and mx <= 263 and my >= 442 and my <= 477 and event.type == pygame.MOUSEBUTTONUP or keys[pygame.K_LEFT] or keys[pygame.K_a]: #changes skin
                skin = skin - 1
            if skin < 1:
                skin = 13

            if mx >= 367 and mx <= 394 and my >= 442 and my <= 477 and event.type == pygame.MOUSEBUTTONUP or keys[pygame.K_RIGHT] or keys[pygame.K_d]: #changes skin
                skin = skin + 1
                if skin > 13:
                    skin = 1

                #song changer
            if mx >= 405 and mx <= 421 and my >= 742 and my <= 777 and event.type == pygame.MOUSEBUTTONUP: #music chooser
                song += 1
                if song == 7:
                    song = 1
                music = pygame.mixer.music.load(f'newgameimg/sounds/music{song}.wav')
                pygame.mixer.music.play(-1)

            if mx >= 215 and mx <= 234 and my >= 742 and my <= 777 and event.type == pygame.MOUSEBUTTONUP: #music chooser
                song -= 1
                if song == 0:
                    song = 6
                music = pygame.mixer.music.load(f'newgameimg/sounds/music{song}.wav')
                pygame.mixer.music.play(-1)

            if mx >= 325:
                presentskin = pygame.image.load(f'newgameimg/players/main{skin}.png')

            elif mx <= 326:
                leftskin = pygame.image.load(f'newgameimg/players/main{skin}.png')
                presentskin = pygame.transform.flip(leftskin, True, False)




        pygame.display.update()




    if game_over == 0: #actual game
        mx, my = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()


        playerhitboxleft = x - 30      #creating a player hitbox
        playerhitboxright = x + 100    #creating a player hitbox
        playerhitboxup = y - 22        #creating a player hitbox
        playerhitboxdown = y + 111     #creating a player hitbox



        #controls
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: #character go left
            x = x - speed
            left = True
            right = False
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: #character go right
            x += speed
            left = False
            right = True

            #game boundries
        if x >= 550:
            x = 550
        if x <= 0:
            x = 0
        if y > 595:
            y = 595



            #spawns in the enemy at random place
        if enemyx <= -1000 or enemyx >= 1000:
            enemyleftorright = random.randrange(1,3)
            if enemyleftorright == 1:
                enemyx = random.randrange(700,999)
            if enemyleftorright == 2:
                enemyx = random.randrange(-999,-700)

        if 1 == 1: #moves enemy
            if enemyx >= 570 and enemyx <= 620 or enemyx >= 0 and enemyx <= 50:
                enemyslowdown = 1
                enemyspeed = random.randrange(2,4)
            else:
                enemyslowdown = 2



        if enemyleftorright == 1: #enemy speeds
            enemyx = enemyx - ((enemyspeed + enemyspeedup) * jumpcoffeespeed) * enemyslowdown
            enemycharacter = enemyleft
        if enemyleftorright == 2:
            enemyx = enemyx + ((enemyspeed + enemyspeedup) * jumpcoffeespeed) * enemyslowdown
            enemycharacter = enemyright

        #player hitbox for checking if enemy has hit player

        distance = math.sqrt(math.pow(enemyx - x, 2) + (math.pow(590 - y, 2))) #https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org (1:34:24)
        if distance < 60:
            if mutee == 1:
                death.play()
            randomtip = random.choice(tipslist)
            carx = carspawn
            animation = 0
            game_over = 1


        for i in range(num_of_coffee): #checks if coffee has hit the ground
            if coffeey[i] >= 650:
                coffeey[i] = random.randrange(-100, -45)
                coffeex[i] = random.randrange(40, 610)
                turn = random.randrange(1,361)
                coffeeskin = pygame.transform.rotate(coffee_bean, turn)
                coffeeimage[i] = coffeeskin

        for i in range(num_of_coffee): #checks if coffee has hit the player
            if coffeey[i] >= playerhitboxup and coffeex[i] >= playerhitboxleft and coffeex[i] <= playerhitboxright:
                coffeey[i] = random.randrange(-100, -45)
                coffeex[i] = random.randrange(40, 610)
                turn = random.randrange(1, 361)
                coffeeskin = pygame.transform.rotate(coffee_bean, turn)
                coffeeimage[i] = coffeeskin
                score += 1
                if mutee == 1:
                    effect.play()


        screen.blit(bg, (0, 0))

        for i in range(num_of_clouds):
            if cloudx[i] >= 700:
                cloudx[i] = random.randrange(-300,-100)
                cloudy[i] = random.randrange(10,300)
            cloudx[i] += 1
            screen.blit(cloud,(cloudx[i], cloudy[i]))


        if xy <= 650:
            xy += 1
        screen.blit(x_power_up,(xx,xy))

        powerupdistance = math.sqrt(math.pow(x - xx, 2) + (math.pow(y - xy, 2))) #https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org (1:34:24) if you hit the powerup and what it does after that
        if powerupdistance < 80:
            if mutee == 1:
                powerupsound.play()
            xx = random.randrange(50, 600)
            xy = random.randrange(-2000, -1000)
            coffees *= 2
            num_of_coffee *= 2
            for i in range(num_of_coffee):
                turn = random.randrange(1, 361)
                coffeeimage.append(pygame.transform.rotate(coffee_bean, turn))
                coffeex.append(random.randrange(0, 640))
                coffeey.append(random.randrange(-600, -45))
                coffeey_change.append(coffeefallspeed)


        if 1 == 1: #teleports anvil back up if it hits the floor
            if anvily <= 650:
                anvily += 7.5
            else:
                anvilx = random.randrange(50,600)
                anvily = -1000

        anvildistance = math.sqrt(math.pow(x - anvilx, 2) + (math.pow(y - anvily, 2)))  # https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org (1:34:24) this is if the anvil hits and player and what to do next
        if anvildistance < 60:
            if mutee == 1:
                bonk.play()
            randomtip = random.choice(tipslist)
            carx = carspawn
            animation = 0
            game_over = 1








        draw_text("Time:", smallfont, white, 10, 720)
        if not (isJump): #jumping code
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:  # jumping code
                isJump = True
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.75
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False  # jumping code


        timer1 = pygame.time.get_ticks() - start_time - end_time
        timer2 = timer1 / 1000
        timer = round(timer2, 1)

        game_timer = timer2

        draw_text(f'{timer}', smallfont, white, 10, 752)



        direction(left, right, skin)
        draw_text("George is dumb", font, green, 100, 400)
        draw_text(f"{score}", smallfont, white, 560, 740)
        power_ups()
        for i in range(num_of_coffee):
            coffeey[i] += coffeey_change[i] * jumpcoffeespeed * coffeeaddspeed
            coffee(coffeex[i], coffeey[i], i)

        if anvilturn >= 360:
            anvilturn = 0

        anvilturn += 1

        anvilspin = pygame.transform.rotate(anvil, anvilturn)

        screen.blit(anvilspin,(anvilx,anvily))
        screen.blit(enemycharacter, (enemyx, 590))

        #arrows to show where the enemy is coming from
        if enemyx >= 650 and enemyx <= 900:
            screen.blit(arrow_right,(550,585))
        if enemyx <= 0 and enemyx >= -250:
            screen.blit(arrow_left,(0,585))


        for event in pygame.event.get(): #quits to endgame menu
            if event.type == pygame.QUIT:
                menu = False
            if keys[pygame.K_ESCAPE]:
                if mutee == 1:
                    death.play()
                animation = 0
                randomtip = random.choice(tipslist)
                carx = carspawn
                game_over = 1
                                            #add speed power up
            if keys[pygame.K_e] or mx >= 312 and mx <= 419 and my >= 725 and my <= 795 and event.type == pygame.MOUSEBUTTONDOWN:
                if score >= speedcost:
                    speed += 0.5
                    score -= speedcost
                    speeds += 1
                    speedcost += 5

            if keys[pygame.K_l]:
                score += 100000

                                 #add more coffee power up
            if keys[pygame.K_q] or mx >= 147 and mx <= 253 and my >= 725 and my <= 795 and event.type == pygame.MOUSEBUTTONDOWN:
                if score >= coffeecost:
                    score -= coffeecost
                    coffees += 1
                    coffeecost += 10
                    num_of_coffee += 1
                    coffeeaddspeed += 0.01
                    for i in range(num_of_coffee):
                        turn = random.randrange(1, 361)
                        coffeeimage.append(pygame.transform.rotate(coffee_bean, turn))
                        coffeex.append(random.randrange(0, 640))
                        coffeey.append(random.randrange(-600, -45))
                        coffeey_change.append(coffeefallspeed)
               #mute
            if keys[pygame.K_m] or mx >= 10 and mx <= 55 and my >= 14 and my <= 54 and event.type == pygame.MOUSEBUTTONDOWN:
                if mutee == 1:
                    mutee = 0
                    muteorunmute = mutepng
                    pygame.mixer.music.pause()
                elif mutee == 0:
                    mutee = 1
                    muteorunmute = unmutepng
                    pygame.mixer.music.unpause()



            if mx >= 10 and mx <= 28 and my >= 63 and my <= 97 and event.type == pygame.MOUSEBUTTONUP:
                song += 1
                if song == 7:
                    song = 1
                music = pygame.mixer.music.load(f'newgameimg/sounds/music{song}.wav')
                pygame.mixer.music.play(-1)
            # song changer
            if mx >= 36 and mx <= 53 and my >= 63 and my <= 97 and event.type == pygame.MOUSEBUTTONUP:
                song -= 1
                if song == 0:
                    song = 4
                music = pygame.mixer.music.load(f'newgameimg/sounds/music{song}.wav')
                pygame.mixer.music.play(-1)




        screen.blit(muteorunmute,(10,10))
        screen.blit(arrow_left, (-35, 60))
        screen.blit(arrow_right, (-10, 60))

          #draws power up info

        draw_text(f"Level {coffees}", supersmallfont, grey, 158, 760)
        draw_text(f"{coffeecost}", supersmallfont, black, 200, 736)
        draw_text(f"Level {speeds}", supersmallfont, grey, 323, 760)
        draw_text(f"{speedcost}", supersmallfont, black, 365, 736)
        draw_text("Q", smallfont, black, 265, 736)
        draw_text("E", smallfont, black, 440, 736)

        pygame.display.update()

    if game_over == 1: #endgame menu
        end_time = pygame.time.get_ticks() #gets end time for timer
        keys = pygame.key.get_pressed() #easier way of getting keys
        mx, my = pygame.mouse.get_pos() #finds mouse
        carx += 2
        if carx >= 1050:
            carx = carspawn
        if carx == 250:
            randomsound = random.randrange(1,4)
            randomsound1 = pygame.mixer.Sound(f'newgameimg/sounds/effect{randomsound}.wav')
            if mutee == 1:
                randomsound1.play()



        endgamebuttons()
        if animation <= 6:
            animation += 1
            explosion(animation)
        center_text(f"Pro tip: {randomtip}", white, 310,supersmallfont) #draws tips
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if keys[pygame.K_m] or mx >= 65 and mx <= 109 and my >= 739 and my <= 788 and event.type == pygame.MOUSEBUTTONUP: #mute button code
                if mutee == 1:
                    mutee = 0
                    muteorunmute = mutepng
                    pygame.mixer.music.pause()
                elif mutee == 0:
                    mutee = 1
                    muteorunmute = unmutepng
                    pygame.mixer.music.unpause()
            if mx >= 200 and mx <= 450 and my >= 350 and my <= 450 and event.type == pygame.MOUSEBUTTONUP:  # puts you back into the game
                end_time = pygame.time.get_ticks() - start_time - game_timer
                score = 0
                speedcost = 5
                speeds = 1
                speed = playerspeed
                coffeefallspeed = 2.5
                coffeecost = 10
                coffees = 1
                enemyx = 998
                enemyspeedup = 0
                isJump = False
                coffeeaddspeed = 1
                jumpCount = 10

                #spawns the clouds

                cloudx = []
                cloudy = []
                cloudimage = []
                cloudx_change = []
                for i in range(num_of_clouds):
                    cloudimage.append(pygame.image.load("newgameimg/bg/cloud.png"))
                    cloudx.append(random.randrange(-200, 700))
                    cloudy.append(random.randrange(10, 300))
                    cloudx_change.append(1)


                coffeeimage = []
                coffeex = []
                coffeey = []
                coffeey_change = []
                num_of_coffee = 1
                for i in range(num_of_coffee):
                    turn = random.randrange(1, 361)
                    coffeeimage.append(pygame.transform.rotate(coffee_bean, turn))
                    coffeex.append(random.randrange(0, 600))
                    coffeey.append(random.randrange(-250, -45))
                    coffeey_change.append(coffeefallspeed)

                x = 25
                y = 595
                xx = random.randrange(50, 600)
                xy = random.randrange(-300, -100)
                anvilx = random.randrange(50, 600)
                anvily = random.randrange(-300, -100)
                game_over = 0



            # song changer

            if mx >= 405 and mx <= 421 and my >= 742 and my <= 777 and event.type == pygame.MOUSEBUTTONUP:
                song += 1
                if song == 7:
                    song = 1
                music = pygame.mixer.music.load(f'newgameimg/sounds/music{song}.wav')
                pygame.mixer.music.play(-1)
            # song changer
            if mx >= 215 and mx <= 234 and my >= 742 and my <= 777 and event.type == pygame.MOUSEBUTTONUP:
                song -= 1
                if song == 0:
                    song = 6
                music = pygame.mixer.music.load(f'newgameimg/sounds/music{song}.wav')
                pygame.mixer.music.play(-1)

            #takes you back to main menu
            if mx >= 200 and mx <= 450 and my >= 500 and my <= 600 and event.type == pygame.MOUSEBUTTONUP:  # gets x and y of mouse to check if it is on the button
                end_time = 0
                game_over = 2

        screen.blit(muteorunmute,(65,735))
        screen.blit(main17,(carx,595))



    enemyspeedup = enemyspeedup + 0.00005
    pygame.display.update()

