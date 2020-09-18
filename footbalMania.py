# imports
import pygame, sys, time, random, math
from pygame.locals import *

# globals
res = w, h = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
maize = (255, 203, 5)
orange = (255, 102, 0)
green = (6, 202, 0)
light_green = (7, 225, 0)
red = (225, 0, 0)
light_red = (255, 0, 0)
grey = (50, 50, 50)
blue = (0, 24, 180)
light_blue = (0, 35, 255)
p1x, p1y = 640, 244
p2x, p2y = 82, 244
bx, by = 385, 260
p1move, p2move = 6, 6
p1frame, p2frame = 0, 0
p1direction, p2direction = 0, 0
bdirx, bdiry = 5, -5
radius = 6
aiplayermode = True

# initialize
pygame.init()
pygame.joystick.init()
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Football Mania")
fps = pygame.time.Clock()


# image loads (All images taken from spriters-resource.net)
char1 = pygame.image.load("player1.png").convert_alpha()
char2 = pygame.image.load("player2.png").convert_alpha()
bg = pygame.image.load("bg.png").convert_alpha()
ball = pygame.image.load("ball.png").convert_alpha()
mich = pygame.image.load("michiganwins.png").convert_alpha()
miami = pygame.image.load("miamiwins.png").convert_alpha()
start_menu = pygame.image.load("startmenu.png").convert_alpha()
gameoverscreen = pygame.image.load("gameoverscreen.png").convert_alpha()
howto = pygame.image.load("howtoplay.png").convert_alpha()

# audio loads (royalty free music)
pygame.mixer.music.load("maintheme.wav")
whistle = pygame.mixer.Sound("whistle.wav")
td = pygame.mixer.Sound("td.wav")
crowd = pygame.mixer.Sound("crowd.wav")
gameover_fx = pygame.mixer.Sound("gameover.wav")


# frame grab
def get_image(posx, posy, width, height, sprite_sheet):
    """Extracts frames from sprite sheet when given the x and y
    coordinates of the top left corner of the desired frame, the 
    width and height of the desired frame and the sprite sheet from
    which to extract the frame"""

    image = pygame.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    image.set_colorkey(black)
    return image


# player 1 frames
# walking towards
t1 = get_image(100, 1000, 32, 36, sprite_sheet=char1)
t2 = get_image(132, 1000, 32, 36, sprite_sheet=char1)
t3 = get_image(164, 1000, 32, 36, sprite_sheet=char1)
t4 = get_image(196, 1000, 32, 36, sprite_sheet=char1)
# walking right
r1 = get_image(0, 124, 28, 36, sprite_sheet=char1)
r2 = get_image(32, 124, 28, 36, sprite_sheet=char1)
r3 = get_image(64, 124, 28, 36, sprite_sheet=char1)
r4 = get_image(96, 124, 28, 36, sprite_sheet=char1)
# walking left
l1 = pygame.transform.flip(r1, True, False)
l2 = pygame.transform.flip(r2, True, False)
l3 = pygame.transform.flip(r3, True, False)
l4 = pygame.transform.flip(r4, True, False)
# walking away
a1 = get_image(0, 920, 32, 36, sprite_sheet=char1)
a2 = get_image(32, 920, 32, 36, sprite_sheet=char1)
a3 = get_image(64, 920, 32, 36, sprite_sheet=char1)
a4 = get_image(96, 920, 32, 36, sprite_sheet=char1)

# player 2 frames
# walking towards
t12 = get_image(100, 1000, 32, 36, sprite_sheet=char2)
t22 = get_image(132, 1000, 32, 36, sprite_sheet=char2)
t32 = get_image(164, 1000, 32, 36, sprite_sheet=char2)
t42 = get_image(196, 1000, 32, 36, sprite_sheet=char2)
# walking right
r12 = get_image(0, 124, 28, 36, sprite_sheet=char2)
r22 = get_image(32, 124, 28, 36, sprite_sheet=char2)
r32 = get_image(64, 124, 28, 36, sprite_sheet=char2)
r42 = get_image(96, 124, 28, 36, sprite_sheet=char2)
# walking left
l12 = pygame.transform.flip(r12, True, False)
l22 = pygame.transform.flip(r22, True, False)
l32 = pygame.transform.flip(r32, True, False)
l42 = pygame.transform.flip(r42, True, False)
# walking away
a12 = get_image(0, 920, 32, 36, sprite_sheet=char2)
a22 = get_image(32, 920, 32, 36, sprite_sheet=char2)
a32 = get_image(64, 920, 32, 36, sprite_sheet=char2)
a42 = get_image(96, 920, 32, 36, sprite_sheet=char2)

# image scaling
# right
r1 = pygame.transform.scale(r1, (74, 82))
r2 = pygame.transform.scale(r2, (74, 82))
r3 = pygame.transform.scale(r3, (74, 82))
r4 = pygame.transform.scale(r4, (74, 82))
# left
l1 = pygame.transform.scale(l1, (74, 82))
l2 = pygame.transform.scale(l2, (74, 82))
l3 = pygame.transform.scale(l3, (74, 82))
l4 = pygame.transform.scale(l4, (74, 82))
# towards
t1 = pygame.transform.scale(t1, (74, 82))
t2 = pygame.transform.scale(t2, (74, 82))
t3 = pygame.transform.scale(t3, (74, 82))
t4 = pygame.transform.scale(t4, (74, 82))
# away
a1 = pygame.transform.scale(a1, (74, 82))
a2 = pygame.transform.scale(a2, (74, 82))
a3 = pygame.transform.scale(a3, (74, 82))
a4 = pygame.transform.scale(a4, (74, 82))
# p2 right
r12 = pygame.transform.scale(r12, (74, 82))
r22 = pygame.transform.scale(r22, (74, 82))
r32 = pygame.transform.scale(r32, (74, 82))
r42 = pygame.transform.scale(r42, (74, 82))
# p2 left
l12 = pygame.transform.scale(l12, (74, 82))
l22 = pygame.transform.scale(l22, (74, 82))
l32 = pygame.transform.scale(l32, (74, 82))
l42 = pygame.transform.scale(l42, (74, 82))
# p2 towards
t12 = pygame.transform.scale(t12, (74, 82))
t22 = pygame.transform.scale(t22, (74, 82))
t32 = pygame.transform.scale(t32, (74, 82))
t42 = pygame.transform.scale(t42, (74, 82))
# p2 away
a12 = pygame.transform.scale(a12, (74, 82))
a22 = pygame.transform.scale(a22, (74, 82))
a32 = pygame.transform.scale(a32, (74, 82))
a42 = pygame.transform.scale(a42, (74, 82))
# ball
ball = pygame.transform.scale(ball, (38, 34))

# p1 walking animation lists
p1walking_towards = [t1, t2, t3, t4]
p1walking_left = [l1, l2, l3, l4]
p1walking_right = [r1, r2, r3, r4]
p1walking_away = [a1, a2, a3, a4]

# p2 walking animation lists
p2walking_towards = [t12, t22, t32, t42]
p2walking_left = [l12, l22, l32, l42]
p2walking_right = [r12, r22, r32, r42]
p2walking_away = [a12, a22, a32, a42]

# idles
p1current_frame = p1walking_towards[0]
p2current_frame = p2walking_towards[0]

# masks
char1_mask = pygame.mask.from_surface(p1current_frame)
char2_mask = pygame.mask.from_surface(p2current_frame)
ball_mask = pygame.mask.from_surface(ball)

# score counters
p1score = 0
p2score = 0

# p1 walking animation function
def player1_animation():
    """takes the frames taken by the get_image function which are
    in lists at this point and loops through the lists using the 
    floor divison operator in order to change the image. This creates
    an animation"""

    global p1frame

    if p1frame + 1 >= 12:
        p1frame = 0
    
    if p1direction == 0:
        p1current_frame = p1walking_towards[p1frame // 3]
        screen.blit(p1current_frame, (p1x, p1y))
        p1frame += 1

    if p1direction == 1:
        p1current_frame = p1walking_left[p1frame // 3]
        screen.blit(p1current_frame, (p1x, p1y))
        p1frame += 1
    if p1direction == 2:
        p1current_frame = p1walking_right[p1frame // 3]
        screen.blit(p1current_frame, (p1x, p1y))
        p1frame += 1
    if p1direction == 3:
        p1current_frame = p1walking_away[p1frame // 3]
        screen.blit(p1current_frame, (p1x, p1y))
        p1frame += 1
    if p1direction == 4:
        p1current_frame = p1walking_towards[p1frame // 3]
        screen.blit(p1current_frame, (p1x, p1y))
        p1frame += 1


# p1 walking animation function
def player2_animation():
    """takes the frames taken by the get_image function which are
    in lists at this point and loops through the lists using the 
    floor divison operator in order to change the image. This creates
    an animation"""

    global p2frame

    if p2frame + 1 >= 12:
        p2frame = 0
    
    if p2direction == 0:
        p2current_frame = p2walking_towards[p2frame // 3]
        screen.blit(p2current_frame, (p2x, p2y))
        p2frame += 1

    if p2direction == 1:
        p2current_frame = p2walking_left[p2frame // 3]
        screen.blit(p2current_frame, (p2x, p2y))
        p2frame += 1
    if p2direction == 2:
        p2current_frame = p2walking_right[p2frame // 3]
        screen.blit(p2current_frame, (p2x, p2y))
        p2frame += 1
    if p2direction == 3:
        p2current_frame = p2walking_away[p2frame // 3]
        screen.blit(p2current_frame, (p2x, p2y))
        p2frame += 1
    if p2direction == 4:
        p2current_frame = p2walking_towards[p2frame // 3]
        screen.blit(p2current_frame, (p2x, p2y))
        p2frame += 1


# boundaries and movement for the ball
def ballmovement():
    """ Sets boundaries for the ball and returns it to the center
    of the field if taken out of bounds"""

    global bx, by, bdirx, bdiry

    if bx > 783 or bx - 10 < 0:
        pygame.mixer.Sound.play(whistle)
        bx, by = 385, 260
        
    if by > 548 or by - 10 < 0:
        pygame.mixer.Sound.play(whistle)
        bx, by = 385, 260


# function for displaying text
def message_to_screen(text, color, x, y, size):
    """takes in 4 parameters, text, color, position and font size
    then displays text accordingly when the function is called"""
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))


# font and text rect function
def text_objects(text, font):
    """allows me to render fonts into text surface objects"""
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


# button making function
def button(text, x, y, w, h, ic, ac, action):
    """Takes in 8 parameters to create interactive buttons. 
    The parameters are the text that will be displayed, x and
    y positions, width and height, inactive color for when the
    cursor isn't hovering and acive color when the cursor
    is over the button and action, which is the function tied 
    to the button"""

    mousexy = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # joystick count and init
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        None
    else:     
        joystick_0 = pygame.joystick.Joystick(0)
        joystick_0.init()

    if x + w > mousexy[0] > x and y + h > mousexy[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    defaultfont = pygame.font.SysFont(None, 35)
    textSurf, textRect = text_objects(text, defaultfont)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


# quit function
def quitgame():
    """quit function that can be added to buttons"""
    pygame.quit()
    sys.exit()


# start menu
def main_menu():
    """main menu function which contains the four buttons that
    are first displayed when the program is launched"""
    pygame.mixer.music.play()
    pygame.mixer.Sound.stop(crowd)
    menu = True
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.blit(start_menu, (0, 0))

        button("1 PLAYER", 86, 447, 125, 75, green, light_green, aiplayer)
        button("2 PLAYER", 244, 447, 125, 75, red, light_red, gameloop)
        button("HOW TO", 420, 447, 125, 75, blue, light_blue, helpscreen)
        button("QUIT", 584, 447, 125, 75, black, grey, quitgame)

        pygame.display.update()


# how to button
def helpscreen():
    """the function for the screen which is displayed when the 
    how to button is clicked"""
    pygame.mixer.Sound.stop(crowd)
    helpuser = True
    while helpuser:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(howto, (0, 0))

        button("RETURN", 315, 456, 175, 75, light_green, green, main_menu)
        pygame.display.update()


# game over screen
def gameover():
    """function for screen that is displayed when the game is over"""
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(gameover_fx)
    pygame.mixer.Sound.stop(crowd)
    endofgame = False
    while not endofgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(gameoverscreen, (0, 0))
        
        if aiplayermode:
            button("PLAY AGAIN", 283, 265, 175, 75, green, light_green, aiplayer)
        else: 
            button("PLAY AGAIN", 283, 265, 175, 75, green, light_green, gameloop)
        button("MAIN MENU", 283, 365, 175, 75, light_red, red, main_menu)
        button("QUIT", 283, 465, 175, 75, light_blue, blue, quitgame)
        pygame.display.update()
     

# 1 player mode
def aiplayer():
    """function containing the main loop. This function allows 
    for the ability to play again by simply calling the function
    again if the player wants to play again. This is the one 
    player version of the main game loop"""

    global bx, by, p1x, p1y, p2x, p2y, p1direction, p2direction
    char1_mask, char2_mask, ball_mask

    aiplayermode = True

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crowd, -1)
    gameexit = False

    # joystick count and init
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        None
    else:     
        joystick_0 = pygame.joystick.Joystick(0)
        joystick_0.init()
        

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # blits    
        screen.blit(bg, (0, 0))
        screen.blit(ball, (bx, by))

        # joystick axis control
        if joystick_count != 0:
            p1x_axis = joystick_0.get_axis(0)
            p1y_axis = joystick_0.get_axis(1)
        
        # movement
        keys = pygame.key.get_pressed()
        # player 1 movements
        if keys[pygame.K_LEFT]: # or p1x_axis < -0.5:
            p1direction = 1
            p1x -= p1move
        if keys[pygame.K_RIGHT]: # or p1x_axis > 0.5:
            p1direction = 2
            p1x += p1move
        if keys[pygame.K_UP]: # or p1y_axis < -0.5:
            p1direction = 3
            p1y -= p1move
        if keys[pygame.K_DOWN]: # or p1y_axis > 0.5:
            p1direction = 4
            p1y += p1move

        # int versions of coordinates for AI
        p11x, p11y = int(p1x), int(p1y)
        p22x, p22y = int(p2x), int(p2y)
        b1x, b1y = int(bx), int(by)
        # collison between players and ball
        distance1 = b1x - p11x, b1y - p11y
        distance2 = b1x - p22x, b1y - p22y
        distance3 = p11x - p22x, p11y - p22y
        p1ballcollision = char1_mask.overlap(ball_mask, distance1)
        p2ballcollision = char2_mask.overlap(ball_mask, distance2)
        bothplayerscollide = char1_mask.overlap(char2_mask, distance3)
    
        # AI
        dx = bx - p2x
        dy = by - p2y
        
        if dx != 0:
            radian = (math.atan(dy/dx)) - math.pi / 2
        else:
            global radius
            radius = 3
            radian = math.pi / 2

        if dx < 2:
            p2x += math.sin(radian) * radius
            p2y -= math.cos(radian) * radius 
        else:
            p2x -= math.sin(radian) * radius 
            p2y += math.cos(radian) * radius


        # kicking and possesion
        if p1ballcollision:
            bx, by = p1x, p1y
            if p1direction == 1 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    bx -= bdirx * 12                 
            if p1direction == 2 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    bx += bdirx * 20
            if p1direction == 3 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    by += bdiry * 12
            if p1direction == 4 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    by -= bdiry * 24
        if p2ballcollision:
            if not p1ballcollision:
                bx, by = p2x, p2y 

        # stealing ability
        if bothplayerscollide: 
            if b1x == p22x and b1y == p22y:
                b1x, b1y = p11x, p11y 
            if b1x == p11x and b1y == p11y:
                b1x, b1y = p22x, p22y
        
        # speed control
        # lower speeds when in possesion of the ball
        if bx == p1x and by == p1y:
            p1move = 3
        if bx == p2x and by == p2y:
            radius = 3
        # reset speeds when not in possesion of the ball 
        if not p1ballcollision:
            p1move = 6
        if not p2ballcollision:
            radius = 6
        
        # scoring 
        # p1 scoring
        if bx == p1x and by == p1y or bx == p2x and by == p2y:
            if p1x < 76:
                message_to_screen("Touchdown", maize, 200, 200, 100)
                message_to_screen("Michigan!", maize, 250, 265, 100)          
            if p1x < 73:
                time.sleep(2)
                p1x, p1y = 640, 244
                p2x, p2y = 82, 244
                bx, by = 385, 260
                global p1score, p2score
                p1score += 7
            if p1score > 34:
                p1score, p2score = 0, 0
                gameover()
       
        # p2 scoring
        if bx == p1x and by == p1y or bx == p2x and by == p2y:
            if p2x > 677:
                message_to_screen("Touchdown", orange, 200, 200, 100)
                message_to_screen("Miami!", orange, 305, 265, 100)
            if p2x > 679:
                time.sleep(2) 
                p1x, p1y = 640, 244
                p2x, p2y = 82, 244
                bx, by = 385, 260
                p2score += 7
            if p2score > 35:
                p1score, p2score = 0, 0
                gameover()
                
        # displaying score
        p1str = str(round(p1score))
        p2str = str(round(p2score))
        message_to_screen(p1str, white, 182, 5, 75)
        message_to_screen(p2str, white, 572, 5, 75)    
        
        # function calling
        player1_animation()
        player2_animation()
        ballmovement()

        # frame rate + displaying code
        pygame.display.update()
        fps.tick(20)


# 2 player mode
def gameloop():
    """function containing the main loop. This function allows 
    for the ability to play again by simply calling the function
    again if the player wants to play again"""

    global bx, by, p1x, p1y, p2x, p2y, p1direction, p2direction
    char1_mask, char2_mask, ball_mask, 

    aiplayermode = False

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crowd, -1)
    gameexit = False

    # joystick count and init
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        None
    else:     
        joystick_0 = pygame.joystick.Joystick(0)
        joystick_1 = pygame.joystick.Joystick(1)
        joystick_0.init()
        joystick_1.init()

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

        # blits    
        screen.blit(bg, (0, 0))
        screen.blit(ball, (bx, by))

        # joystick axis control
        if joystick_count != 0:
            p1x_axis = joystick_0.get_axis(0)
            p1y_axis = joystick_0.get_axis(1)
            p2x_axis = joystick_1.getaxis(0)
            p2y_axis = joystick_1.getaxis(1)

        # movement
        keys = pygame.key.get_pressed()
        # player 1 movements
        if keys[pygame.K_LEFT]: # or p1x_axis < -0.5:
            p1direction = 1
            p1x -= p1move
        if keys[pygame.K_RIGHT]: # or p1x_axis > 0.5:
            p1direction = 2
            p1x += p1move
        if keys[pygame.K_UP]: # or p1y_axis < -0.5:
            p1direction = 3
            p1y -= p1move
        if keys[pygame.K_DOWN]: # or p1y_axis > 0.5:
            p1direction = 4
            p1y += p1move
        # player 2 movements
        if keys[pygame.K_a]: # or p2x_axis < -0.5:
            p2direction = 1
            p2x -= p2move
        if keys[pygame.K_d]: # or p2x_axis > 0.5:
            p2direction = 2
            p2x += p2move
        if keys[pygame.K_w]: # or p2y_axis < -0.5:
            p2direction = 3
            p2y -= p2move
        if keys[pygame.K_s]: # or p2y_axis > 0.5:
            p2direction = 4
            p2y += p2move

        # collison between players and ball
        distance1 = bx - p1x, by - p1y
        distance2 = bx - p2x, by - p2y
        distance3 = p1x - p2x, p1y - p2y
        p1ballcollision = char1_mask.overlap(ball_mask, distance1)
        p2ballcollision = char2_mask.overlap(ball_mask, distance2)
        bothplayerscollide = char1_mask.overlap(char2_mask, distance3)
    
        # kicking and possesion
        if p1ballcollision:
            bx, by = p1x, p1y
            if p1direction == 1 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    bx -= bdirx * 12                 
            if p1direction == 2 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    bx += bdirx * 20
            if p1direction == 3 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    by += bdiry * 12
            if p1direction == 4 and p1x > 225:
                if keys[pygame.K_m]: # or joystick_0.get_button(0):
                    by -= bdiry * 24
        if p2ballcollision:
            if not p1ballcollision:
                bx, by = p2x, p2y 
                if p2direction == 1 and p2x < 493:
                    if keys[pygame.K_c]: # or joystick_1.get_button(0):
                        bx -= bdirx * 12                 
                if p2direction == 2 and p2x < 493:
                    if keys[pygame.K_c]: # or joystick_1.get_button(0):                   
                        bx += bdirx * 20
                if p2direction == 3 and p2x < 493:
                    if keys[pygame.K_c]: # or joystick_1.get_button(0):
                        by += bdiry * 12
                if p2direction == 4 and p2x < 493:
                    if keys[pygame.K_c]: # or joystick_1.get_button(0):
                        by -= bdiry * 24

        # stealing ability
        if bothplayerscollide: 
            if bx == p2x and by == p2y:
                bx, by = p1x, p1y 
            if bx == p1x and by == p1y:
                bx, by = p2x, p2y

        # speed control
        # lower speeds when in possesion of the ball
        if bx == p1x and by == p1y:
            p1move = 3
        if bx == p2x and by == p2y:
            p2move = 3
        # reset speeds when not in possesion of the ball 
        if not p1ballcollision:
            p1move = 6
        if not p2ballcollision:
            p2move = 6
        
        # scoring 
        # p1 scoring
        if bx == p1x and by == p1y or bx == p2x and by == p2y:
            if p1x < 76:
                message_to_screen("Touchdown", maize, 200, 200, 100)
                message_to_screen("Michigan!", maize, 250, 265, 100)          
            if p1x < 73:
                pygame.mixer.Sound.play(td)
                time.sleep(2)
                p1x, p1y = 640, 244
                p2x, p2y = 82, 244
                bx, by = 385, 260
                global p1score, p2score
                p1score += 7 
            if p1score > 35:
                p1score, p2score = 0, 0
                gameover()
       
        # p2 scoring
        if bx == p1x and by == p1y or bx == p2x and by == p2y:
            if p2x > 646:
                message_to_screen("Touchdown", orange, 200, 200, 100)
                message_to_screen("Miami!", orange, 305, 265, 100)
            if p2x > 649:
                pygame.mixer.Sound.play(td)
                time.sleep(2) 
                p1x, p1y = 640, 244
                p2x, p2y = 82, 244
                bx, by = 385, 260
                p2score += 7
            if p2score > 35:
                p1score, p2score = 0, 0
                gameover()
                
        # displaying score
        p1str = str(round(p1score))
        p2str = str(round(p2score))
        message_to_screen(p1str, white, 182, 5, 75)
        message_to_screen(p2str, white, 572, 5, 75)    
        
        # function calling
        player1_animation()
        player2_animation()
        ballmovement()

        # frame rate + displaying code
        pygame.display.update()
        fps.tick(20)


# function call
main_menu()

