#Example file showing a circle moving on screen
import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
gamescreen = 'menu'
satr = ''
soton = ''
inp = ''
gamemap = list()
refills = 0
empty = set()
protected = set()
tempset = set()
candies = ['r','o','y','g','b','p'] #for red, orange, yellow,green,blue and purple respetively
held = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    mousepos = pygame.mouse.get_pos()
    if gamescreen == 'menu':
        if mouse[0] == True:
            if 180<=mousepos[0]<=540 and 480<=mousepos[1]<=560:
                running = False
            elif 180<=mousepos[0]<=540 and 160<=mousepos[1]<=240:
                gamescreen = 'newgame'
    elif gamescreen == 'newgame':
        if mouse[0] == True:
            if 180<=mousepos[0]<=540 and 480<=mousepos[1]<=560:
                if satr == '' and held == False:
                    satr = int(inp)
                    inp =''
                    held = True
                elif soton == '' and not held:
                    soton = int(inp)
                    inp = ''
                elif empty == set() and not held:
                    empty = tempset
                    tempset = set()
                    inp = ''
                elif protected == set() and not held:
                    protected = tempset
                    tempset = set()
                    inp = ''
                else:
                    refills = int(inp)
                    inp = ''
                    gamescreen = 'gameprep'
            elif 180<=mousepos[0]<=540 and 330<=mousepos[1]<=410 and soton != '' and protected == set():
                inp = inp.split(',')
                if inp[0] <= satr and inp[1] <= soton:
                    tempset.add((inp[0],inp[1]))
            held = True
        elif keys[pygame.K_0] or keys[pygame.K_KP0]:
            if not held:
                inp += '0'
            held = True
        elif keys[pygame.K_1] or keys[pygame.K_KP1]:
            if not held:
                inp += '1'
            held = True
        elif keys[pygame.K_2] or keys[pygame.K_KP2]:
            if not held:
                inp += '2'
            held = True
        elif keys[pygame.K_3] or keys[pygame.K_KP3]:
            if not held:
                inp += '3'
            held = True
        elif keys[pygame.K_4] or keys[pygame.K_KP4]:
            if not held:
                inp += '4'
            held = True
        elif keys[pygame.K_5] or keys[pygame.K_KP5]:
            if not held:
                inp += '5'
            held = True
        elif keys[pygame.K_6] or keys[pygame.K_KP6]:
            if not held:
                inp += '6'
            held = True
        elif keys[pygame.K_7] or keys[pygame.K_KP7]:
            if not held:
                inp += '7'
            held = True
        elif keys[pygame.K_8] or keys[pygame.K_KP8]:
            if not held:
                inp += '8'
            held = True
        elif keys[pygame.K_9] or keys[pygame.K_KP9]:
            if not held:
                inp += '9'
            held = True
        elif keys[pygame.K_BACKSPACE]:
            if not held and len(inp) > 0:
                temp = ''
                for letter in range(len(inp)-1):
                    temp += inp[letter]
                inp = temp
            held = True
        else:
            held = False
    elif gamescreen == 'gameprep':
        for i in range(satr):
            gamemap.append(['generated' for j in range(soton)])
            for i in range(satr):
                for j in range(soton):
                    if (i,j) not in empty:
                        gamemap[i][j] = random.choice(candies)
                    else:
                        gamemap[i][j] = 'blocked'
    # fill the screen with a color to wipe away anything from last frame
    screen.fill('black')
    font1 = pygame.font.SysFont(None, 70)
    font2 = pygame.font.SysFont(None, 50)
    if gamescreen == 'menu':
        screen.blit(font1.render('Candy Pop!', True, "white"), (217, 50))
        #newgame
        pygame.draw.rect(screen,'white',(180,160,360,80),5)
        screen.blit(font1.render('New Game', True, "white"), (230, 177))
        #cont
        pygame.draw.rect(screen, 'grey', (180, 320, 360, 80), 5)
        screen.blit(font1.render('Continue', True, "white"), (245, 337))
        #exit
        pygame.draw.rect(screen, 'grey', (180, 480, 360, 80), 5)
        screen.blit(font1.render('Exit', True, "white"), (312, 497))
    if gamescreen == 'newgame':
        if satr == '':
            screen.blit(font1.render('How many rows?', True, "white"), (160, 150))
        elif soton  == '':
            screen.blit(font1.render('How many colomns?', True, "white"), (160, 150))
        elif empty == set():
            screen.blit(font2.render('what spaces should be blocked ?', True, "white"), (80, 150))
            pygame.draw.rect(screen, 'grey', (180, 330, 360, 80), 5)
            screen.blit(font1.render('Add', True, "white"), (310, 347))
        elif protected == set():
            screen.blit(font2.render('what spaces should be protected ?', True, "white"), (80, 150))
            pygame.draw.rect(screen, 'grey', (180, 330, 360, 80), 5)
            screen.blit(font1.render('Add', True, "white"), (310, 347))
        else:
            screen.blit(font1.render('how many fill-in candies ?', True, "white"), (60, 150))
        if satr == '' or soton == '' or (empty != set() and protected != set()):
            screen.blit(font1.render(inp, True, "white"), (245, 200))
        elif empty == set() or protected == set():
            screen.blit(font1.render(f'({inp})', True, "white"), (245, 200))
        pygame.draw.rect(screen, 'grey', (180, 480, 360, 80), 5)
        screen.blit(font1.render('Confirm', True, "white"), (263, 497))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
#game probs crashes with no empty/protected
#game also crashes on first input on the  refills line
#probs need to add a stage tracker akin to gamephasephase