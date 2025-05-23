#Example file showing a circle moving on screen
from random import choice

import pygame
import random
import time
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()
    running = True
    gamescreen = 'menu'
    gamephasephase = 0
    satr = ''
    soton = ''
    inp = ''
    gamemap = list()
    refills = 0
    score = 0
    rerolls = 3
    empty = list()
    protected = list()
    tempset = list()
    candies = ['r','o','y','g','b','p'] #for red, orange, yellow,green,blue and purple respetively
    # pint , teal and white
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
                    with open('gamesave.txt','a') as file:
                        file.write('emptycheck')
                    with open('gamesave.txt','r') as file:
                        content = file.read()
                        if content[0] != 'emptycheck':
                            gamescreen = 'newgame'
                elif 180<=mousepos[0]<=540 and 320<=mousepos[1]<=400:
                    gamescreen = 'cont'
        elif gamescreen == 'newgame':
            if mouse[0] == True:
                if 180<=mousepos[0]<=540 and 480<=mousepos[1]<=560:
                    if gamephasephase == 0 and held == False:
                        if inp.isdigit():
                            if int(inp) != 0:
                                satr = int(inp)
                                gamephasephase = 1
                        inp =''
                    elif gamephasephase == 1 and not held:
                        if inp.isdigit():
                            if int(inp) != 0:
                                soton = int(inp)
                                gamephasephase = 2
                        inp = ''
                    elif gamephasephase == 2 and not held:
                        empty = tempset
                        tempset = list()
                        inp = ''
                        gamephasephase = 3
                    elif gamephasephase == 3 and not held:
                        protected = tempset
                        tempset = list()
                        inp = ''
                        gamephasephase = 4
                    elif gamephasephase == 4 and not held:
                        if inp == '':
                            inp = '0'
                        refills = int(inp)
                        inp = ''
                        gamephasephase = 0
                        gamescreen = 'gameprep'
                elif 180<=mousepos[0]<=540 and 330<=mousepos[1]<=410 and (gamephasephase == 2 or gamephasephase == 3) and not held:
                    inp = inp.split(',')
                    inp[0] = int(inp[0])
                    inp[1] = int(inp[1])
                    if 0 < int(inp[0]) <= satr and 0 < int(inp[1]) <= soton:
                        tempset.append([inp[0]-1,inp[1]-1])
                    inp = ''
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
            elif keys[pygame.K_COMMA]:
                if not held:
                    inp += ','
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
                    if [i,j] not in empty:
                        gamemap = candyfill(gamemap,i,j)
                    else:
                        gamemap[i][j] = 'blocked'
            amodimult = 720//satr
            ofoghimult = 600//soton
            selected1 = []
            selected2 = []
            selected3 = []
            starttime = time.time()
            gamescreen = 'game'
        elif gamescreen == 'cont':
            with open('gamesave.txt','r') as file:
                content = file.readlines()
                satr = int(content[0].replace('\n',''))
                soton = int(content[1].replace('\n',''))
                temp = content[2]
                temp = temp.replace('[','').replace(']','').replace(' ','').replace('\n','')
                temp = temp.split(',')
                templist = list()
                for adaad in range (len(temp)//2):
                    templist.append([int(temp[adaad*2]),int(temp[(adaad*2)+1])])
                empty = templist
                temp = content[3]
                temp = temp.replace('[','').replace(']','').replace(' ','').replace('\n','')
                temp = temp.split(',')
                templist = list()
                for adaad in range (len(temp)//2):
                    templist.append([int(temp[adaad*2]),int(temp[(adaad*2)+1])])
                protected = templist
                refills = int(content[4].replace('\n',''))
                score = int(content[5].replace('\n',''))
                temp = content[6]
                temp = temp.replace('[','').replace(']','').replace(' ','').replace("'",'').replace('\n','')
                temp = temp.split(',')
                templist = list()
                for adaad in range (satr):
                    templistlist = list()
                    for adaad2 in range (soton):
                        templistlist.append(temp[(adaad*satr)+adaad2])
                    templist.append(templistlist)
                gamemap = templist
                rerolls = int(content[7].replace('\n',''))
                amodimult = 720//satr
                ofoghimult = 600//soton 
                selected1 = []
                selected2 = []
                selected3 = []
                starttime = time.time()
                held = True
                gamescreen = 'game'
        elif gamescreen == 'game':
            if mouse[0] == True and 0<=gamephasephase<=1 :
                if mousepos[0] >= 120 and not held :
                    if gamephasephase == 0:
                        selected1 = [(mousepos[1])//amodimult,(mousepos[0]-120)//ofoghimult]
                        if selected1 not in empty and selected1 not in protected:
                            gamephasephase = 1
                        else:
                            selected1 = []
                    else:
                        selected2 = [(mousepos[1])//amodimult,(mousepos[0]-120)//ofoghimult]
                        if selected2 not in empty and selected1 not in protected:
                            chainreaction = False
                            allfine =True
                            gamephasephase = 2
                        else:
                            selected2 = []
                elif gamephasephase == 0 and not held:
                    if 20<=mousepos[1]<=120:
                        gamephasephase = 3 #save
                    elif 130<=mousepos[1]<=210:
                        if rerolls > 0:
                            gamephasephase = 4 #reroll
                    elif 240<=mousepos[1]<=360:
                        if score >= satr*soton: 
                            gamephasephase = 5 #changecolor
                    elif 390<=mousepos[1]<=480:
                        if score >= satr*soton*2:
                            gamephasephase = 7 #swap
            elif gamephasephase == 2:
                if allfine:
                    difi = abs(selected1[0]-selected2[0])
                    difj = abs(selected1[1]-selected2[1])
                    if (difi == 0 and difj == 1) or (difi == 1 and difj == 0):
                        flag = False
                        returned = viableswap(gamemap, selected1, selected2,satr,soton)
                        if (gamemap[selected1[0]][selected1[1]] == 'satrsoton' or gamemap[selected1[0]][selected1[1]] == 'bomb' or gamemap[selected1[0]][selected1[1]] == 'rainbow'):
                            flag = '1'
                        elif (gamemap[selected2[0]][selected2[1]] == 'bomb' or gamemap[selected2[0]][selected2[1]] == 'rainbow' or gamemap[selected2[0]][selected2[1]] == 'satrsoton'):
                            flag = '2'
                        elif returned[0] != False and returned[1] != False:
                            flag = '12'
                        elif returned [0] != False:
                            flag = '1'
                        elif returned[1] != False:
                            flag = '2'
                        if flag != False:
                            gamemap[selected1[0]][selected1[1]] , gamemap[selected2[0]][selected2[1]] = gamemap[selected2[0]][selected2[1]] , gamemap[selected1[0]][selected1[1]]
                            if flag == '12':
                                gamemap = popcandy(gamemap, selected2[0],selected2[1], returned[0], satr, soton)
                                gamemap = popcandy(gamemap, selected1[0],selected1[1], returned[1], satr, soton)
                            elif flag == '1':
                                if gamemap[selected2[0]][selected2[1]] == 'rainbow':
                                    gamemap = popcandy(gamemap, selected2[0],selected2[1], returned[0], satr, soton,makecandies = False,swapedwith=gamemap[selected1[0]][selected1[1]])
                                elif gamemap[selected2[0]][selected2[1]] == 'satrsoton':
                                    if (selected1[0]-selected2[0]) == 0:
                                        gamemap = popcandy(gamemap, selected2[0],selected2[1], returned[0], satr, soton,satrsoton='satr')
                                    else:
                                        gamemap = popcandy(gamemap, selected2[0],selected2[1], returned[0], satr, soton,satrsoton='soton')
                                else:
                                    gamemap = popcandy(gamemap, selected2[0],selected2[1], returned[0], satr, soton)
                            elif flag == '2':
                                if gamemap[selected1[0]][selected1[1]] == 'rainbow':
                                    gamemap = popcandy(gamemap, selected1[0],selected1[1], returned[0], satr, soton,makecandies = False,swapedwith=gamemap[selected2[0]][selected2[1]])
                                elif gamemap[selected1[0]][selected1[1]] == 'satrsoton':
                                    if (selected1[0]-selected2[0]) == 0:
                                        gamemap = popcandy(gamemap, selected1[0],selected1[1], returned[0], satr, soton,satrsoton='satr')
                                    else:
                                        gamemap = popcandy(gamemap, selected1[0],selected1[1], returned[0], satr, soton,satrsoton='soton')
                                else:
                                    gamemap = popcandy(gamemap, selected1[0],selected1[1], returned[1], satr, soton)
                            for temp1 in range (satr):
                                for temp2 in range (soton) :
                                    if gamemap[temp1][temp2] == 'poped':
                                        score += 1
                                        if [temp1,temp2] in protected:
                                            protected.remove([temp1,temp2])
                                        else:
                                            for bir in [-1,0,1]:
                                                for iki in [-1,0,1]:
                                                    if 0<=temp1+bir<satr and 0<=temp2+iki<soton and [temp1+bir,temp2+iki] in protected:
                                                        protected.remove([temp1+bir,temp2+iki])
                                        gamemap = candyfill(gamemap,temp1,temp2,refills)
                                        if refills > 0:
                                            refills -= 1
                            for temp1 in range(satr):
                                for temp2 in range(soton):
                                    if gamemap[temp1][temp2] not in candies and gamemap[temp1][temp2] != 'satrsoton' and gamemap[temp1][temp2] != 'bomb' and gamemap[temp1][temp2] != 'rainbow':
                                        gamemap[temp1][temp2] = 'blocked'
                                    if gamemap[temp1][temp2] == 'blocked':
                                        empty.append([temp1,temp2])
                else:
                    returned = doesitpop(gamemap, [selected3[0],selected3[1]],satr,soton)
                    gamemap = popcandy(gamemap, selected3[0],selected3[1], returned , satr, soton)
                    for temp1 in range (satr):
                                for temp2 in range (soton) :
                                    if gamemap[temp1][temp2] == 'poped':
                                        score += 1
                                        if [temp1,temp2] in protected:
                                            protected.remove([temp1,temp2])
                                        else:
                                            for bir in [-1,0,1]:
                                                for iki in [-1,0,1]:
                                                    if 0<=temp1+bir<satr and 0<=temp2+iki<soton and [temp1+bir,temp2+iki] in protected:
                                                        protected.remove([temp1+bir,temp2+iki])
                                        gamemap = candyfill(gamemap,temp1,temp2,refills)
                                        if refills > 0:
                                            refills -= 1
                    for temp1 in range(satr):
                        for temp2 in range(soton):
                            if gamemap[temp1][temp2] not in candies and gamemap[temp1][temp2] != 'satrsoton' and gamemap[temp1][temp2] != 'bomb' and gamemap[temp1][temp2] != 'rainbow':
                                gamemap[temp1][temp2] = 'blocked'
                            if gamemap[temp1][temp2] == 'blocked':
                                empty.append([temp1,temp2])
                selected1 = []
                selected2 = []
                selected3 = []
                allfine = True
                for noombarbir in range(satr-1,-1,-1):
                    for noombariki in range(soton):
                        if doesitpop(gamemap, [noombarbir,noombariki],satr,soton) != False:
                            allfine = False
                            selected3 = [noombarbir,noombariki]
                            break
                    if not allfine:
                        break
                if allfine:
                    gamephasephase = 0
            elif gamephasephase == 3: #save
                with open('gamesave.txt','w') as file:
                    file.write(f'{satr}\n{soton}\n{empty}\n{protected}\n{refills}\n{score}\n{gamemap}\n{rerolls}')
                running = False
            elif gamephasephase ==4: #reroll
                gamemap2 =[]
                for i in range(satr):
                    for i in range(satr):
                        gamemap2.append(['generated' for j in range(soton)])
                for i in range(satr):
                    for j in range(soton):
                        if [i,j] not in empty:
                            gamemap2 = candyfill(gamemap,i,j)
                        else:
                            gamemap2[i][j] = 'blocked'
                            gamemap = gamemap2
                rerolls -= 1
                gamephasephase = 0
            elif gamephasephase == 5 and not held and mouse[0] == True and mousepos[0] >= 120: #changecolor
                colorselect = [(mousepos[1])//amodimult,(mousepos[0]-120)//ofoghimult]
                if colorselect not in empty:
                    gamephasephase = 6
            elif gamephasephase == 6 and not held and mouse[0] == True and 310<=mousepos[1]<=410: #pickcolor
                if 120<mousepos[0]<220:
                    gamemap[colorselect[0]][colorselect[1]] = 'r'
                elif 220<mousepos[0]<320:
                    gamemap[colorselect[0]][colorselect[1]] = 'b'
                elif 320<mousepos[0]<420:
                    gamemap[colorselect[0]][colorselect[1]] = 'y'
                elif 420<mousepos[0]<520:
                    gamemap[colorselect[0]][colorselect[1]] = 'p'
                elif 520<mousepos[0]<620:
                    gamemap[colorselect[0]][colorselect[1]] = 'o'
                elif 620<mousepos[0]<720:
                    gamemap[colorselect[0]][colorselect[1]] = 'g'
                score -= satr*soton
                gamephasephase = 0
            elif gamephasephase == 7 : #swap
                if selected1 == [] and not held and 120 <= mousepos[0] and mouse[0] == True:
                    selected1 = [(mousepos[1])//amodimult,(mousepos[0]-120)//ofoghimult]
                elif selected2 == [] and not held and 120 <= mousepos[0] and mouse[0] == True:
                    selected2 = [(mousepos[1])//amodimult,(mousepos[0]-120)//ofoghimult]
                elif selected1 != [] and selected2 != [] and selected1 != selected2:
                    gamemap[selected1[0]][selected1[1]] , gamemap[selected2[0]][selected2[1]] = gamemap[selected2[0]][selected2[1]] , gamemap[selected1[0]][selected1[1]]
                    selected1 = []
                    selected2 = []
                    score -= satr*soton*2
                    gamephasephase = 0
            if gamephasephase == 0 and rerolls == 0:
                gameover = True
                for temp11 in range(satr):
                    for temp12 in range(soton):
                        for temp21,temp22 in [[-1,0],[1,0],[0,-1],[0,1]]:
                            if 0 <= temp11+temp21 <satr and 0 <= temp12+temp22 <soton and [temp11,temp12] not in empty and [temp11+temp21,temp12+temp22] not in empty:
                                if viableswap(gamemap, [temp11,temp12], [temp11+temp21,temp12+temp22],satr,soton) != [False,False]:
                                    gameover = False
                            if gameover == False:
                                break
                        if gameover == False:
                            break
                    if gameover == False:
                        break
                if gameover == True:
                    gamescreen = 'gameover'
            if mouse[0] == True:
                   held = True
            elif mouse[0] == False:
                held = False
        elif gamescreen == 'gameover':
            if mouse[0] and not held:
                running = False
            if mouse[0] == True:
                   held = True
            elif mouse[0] == False:
                held = False
        # fill the screen with a color to wipe away anything from last frame
        screen.fill('black')
        font1 = pygame.font.SysFont(None, 70)
        font2 = pygame.font.SysFont(None, 50)
        font3 = pygame.font.SysFont(None, 40)
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
        elif gamescreen == 'newgame':
            if gamephasephase == 0:
                screen.blit(font1.render('How many rows?', True, "white"), (160, 150))
            elif gamephasephase == 1:
                screen.blit(font1.render('How many colomns?', True, "white"), (160, 150))
            elif gamephasephase == 2:
                screen.blit(font2.render('what spaces should be blocked ?', True, "white"), (80, 150))
                pygame.draw.rect(screen, 'grey', (180, 330, 360, 80), 5)
                screen.blit(font1.render('Add', True, "white"), (310, 347))
            elif gamephasephase == 3:
                screen.blit(font2.render('what spaces should be protected ?', True, "white"), (80, 150))
                pygame.draw.rect(screen, 'grey', (180, 330, 360, 80), 5)
                screen.blit(font1.render('Add', True, "white"), (310, 347))
            elif gamephasephase == 4:
                screen.blit(font1.render('how many fill-in candies ?', True, "white"), (60, 150))
            if gamephasephase == 0 or gamephasephase == 1 or gamephasephase == 4:
                screen.blit(font1.render(inp, True, "white"), (245, 200))
            elif gamephasephase == 2 or gamephasephase == 3:
                screen.blit(font1.render(f'({inp})', True, "white"), (245, 200))
            pygame.draw.rect(screen, 'grey', (180, 480, 360, 80), 5)
            screen.blit(font1.render('Confirm', True, "white"), (263, 497))
        elif gamescreen == 'game':
            if amodimult < ofoghimult :
                r = amodimult/2
            else:
                r = ofoghimult/2
            if selected1 != []:
                pygame.draw.rect(screen,'white',[(selected1[1]*ofoghimult)+120,selected1[0]*amodimult,ofoghimult,amodimult],500)
            screen.blit(font2.render('save &', True, "white"), (10, 20))
            screen.blit(font1.render('exit', True, "white"), (10, 50))
            if gamephasephase == 0:
                screen.blit(font3.render('refresh', True, "white"), (10, 130))
                screen.blit(font2.render(f'{rerolls} left', True, "white"), (10, 160))
                screen.blit(font3.render('change', True, "white"), (10, 240))
                screen.blit(font2.render('color', True, "white"), (10, 270))
                screen.blit(font2.render(f'-{satr*soton}', True, "white"), (10, 310))
                screen.blit(font2.render('swap', True, "white"), (10, 390))
                screen.blit(font2.render(f'-{satr*soton*2}', True, "white"), (10, 430))
            if gamephasephase == 5:
                screen.blit(font3.render('select', True, "white"), (10, 130))
                screen.blit(font3.render('a candy', True, "white"), (10, 160))
                screen.blit(font3.render('to', True, "white"), (10, 190))
                screen.blit(font3.render('change', True, "white"), (10, 220))
                screen.blit(font3.render('its', True, "white"), (10, 250))
                screen.blit(font3.render('color', True, "white"), (10, 280))
            if gamephasephase == 7:
                screen.blit(font3.render('select', True, "white"), (10, 130))
                screen.blit(font3.render('the', True, "white"), (10, 160))
                if selected1 == []:
                    screen.blit(font3.render('first', True, "white"), (10, 190))
                else:
                    screen.blit(font3.render('second', True, "white"), (10, 190))
                screen.blit(font3.render('candy', True, "white"), (10, 220))
            if gamephasephase == 0 or gamephasephase == 1 or gamephasephase == 2 or gamephasephase == 5 or gamephasephase == 7:
                for i in range(satr):
                    for j in range(soton):
                        if [i,j] in protected:
                            pygame.draw.rect(screen,'white',[(j*ofoghimult)+120,i*amodimult,ofoghimult,amodimult],500)
                        if gamemap[i][j] == 'r':
                            color = 'red'
                        elif gamemap[i][j] == 'b':
                            color = 'blue'
                        elif gamemap[i][j] == 'y':
                            color = 'yellow'
                        elif gamemap[i][j] == 'p':
                            color = 'purple'
                        elif gamemap[i][j] == 'o':
                            color = 'orange'
                        elif gamemap[i][j] == 'g':
                            color = 'green'
                        elif gamemap[i][j] == 'bomb':
                            color = 'grey'
                        elif gamemap[i][j] == 'rainbow':
                            color = 'pink'
                        elif gamemap[i][j] == 'satrsoton':
                            color = 'teal'
                        else:
                            color = 'black'
                        pygame.draw.circle(screen,color,(120 + ((j+0.5)*ofoghimult),(i+0.5)*amodimult),r,500)
            if gamephasephase == 6:
                pygame.draw.circle(screen,'red',(120 + ((0+0.5)*100),360),45,500)
                pygame.draw.circle(screen,'blue',(120 + ((1+0.5)*100),360),45,500)
                pygame.draw.circle(screen,'yellow',(120 + ((2+0.5)*100),360),45,500)
                pygame.draw.circle(screen,'purple',(120 + ((3+0.5)*100),360),45,500)
                pygame.draw.circle(screen,'orange',(120 + ((4+0.5)*100),360),45,500)
                pygame.draw.circle(screen,'green',(120 + ((5+0.5)*100),360),45,500)
            screen.blit(font2.render(f'{int(time.time()-starttime)//60}:{int(time.time()-starttime)%60}', True, "white"), (10, 550))
            screen.blit(font2.render('score:', True, "white"), (10, 620))
            screen.blit(font1.render(f'{score}', True, "white"), (10, 660))
        elif gamescreen == 'gameover':
            screen.blit(font1.render('game over !', True, "white"), (200, 250))
            screen.blit(font2.render(f'your score is : {score}', True, "white"), (200, 350))
            screen.blit(font3.render('click to exit the game', True, "white"), (200, 420))


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
def viableswap(gamemap,sel1,sel2,satr,soton):
    lis = [[-2,-1,0],[-1,0,1],[0,1,2]]
    lis2 = [[sel2[0],sel2[1]],[sel1[0],sel1[1]]]
    ret = [False,False]
    gmmap = list()
    for bir in range(satr):
        gmmap.append([addaad for addaad in gamemap[bir]])
    gmmap[sel1[0]][sel1[1]] , gmmap[sel2[0]][sel2[1]] = gmmap[sel2[0]][sel2[1]] , gmmap[sel1[0]][sel1[1]]
    for n in  range(2):
        i , j = lis2[n]
        for r in range(3):
            one, two, three = lis[r]
            if i+one >=0 and i+three <satr:
                if (gmmap[i+one][j] == gmmap[i+two][j] and gmmap[i+two][j] == gmmap[i+three][j]):
                    ret[n] = 'i'
            if j+one >=0 and j+three <soton:
                if (gmmap[i][j+one] == gmmap[i][j+two] and gmmap[i][j+two] == gmmap[i][j+three]):
                    ret[n] = 'j'
    return ret
def doesitpop (gamemap,sel1,satr,soton):
    if gamemap[sel1[0]][sel1[1]] != 'blocked':
        lis = [[-2,-1,0],[-1,0,1],[0,1,2]]
        for r in range(3):
            one, two, three = lis[r]
            if sel1[0]+one >=0 and sel1[0]+three <satr:
                if (gamemap[sel1[0]+one][sel1[1]] == gamemap[sel1[0]+two][sel1[1]] and gamemap[sel1[0]+two][sel1[1]] == gamemap[sel1[0]+three][sel1[1]]):
                    return 'i'
            if sel1[1]+one >=0 and sel1[1]+three <soton:
                if (gamemap[sel1[0]][sel1[1]+one] == gamemap[sel1[0]][sel1[1]+two] and gamemap[sel1[0]][sel1[1]+two] == gamemap[sel1[0]][sel1[1]+three]):
                    return 'j'
    return False
def popcandy(gamemap,i,j,returned,satr,soton,makecandies = True , satrsoton = '',swapedwith = ''):
    if gamemap[i][j] != 'bomb' and gamemap[i][j] != 'rainbow' and gamemap[i][j] != 'satrsoton':
        lort = False
        color = gamemap[i][j]
        explored = [[i,j]]
        if returned == 'i':
            higher = i
            lower = i
        elif returned == 'j':
            higher = j
            lower = j
        else:
            raise ValueError('unviable candy was given to popcandy')
        if returned == 'i':
            while higher != False and higher <satr-1:
                if gamemap[higher+1][j] == color:
                    higher += 1
                    explored.append([higher,j])
                else:
                    higher = False
            while lower != False  and 0 < lower:
                if gamemap[lower-1][j] == color:
                    lower -= 1
                    explored.append([lower,j])
                else:
                    lower = False
        else:
            while higher != False and higher <soton-1:
                if gamemap[i][higher+1] == color:
                    higher += 1
                    explored.append([i,higher])
                else:
                    higher = False
            while lower != False  and 0 < lower:
                if gamemap[i][lower-1] == color:
                    lower -= 1
                    explored.append([i,lower])
                else:
                    lower = False
        if returned == 'i':
            for one , two in [[-2,-1],[-1,1],[1,2]]:
                try:
                    if gamemap[higher][j+one] == color and gamemap[higher][j+two] == color:
                        explored.append([higher,j+one])
                        explored.append([higher,j+two])
                        lort = True
                        break
                except:
                    pass
                try:
                    if gamemap[lower][j+one] == color and gamemap[lower][j+two] == color:
                        explored.append([lower,j+one])
                        explored.append([lower,j+two])
                        lort = True
                        break
                except:
                    pass
        elif returned == 'j':
            for one , two in [[-2,-1],[-1,1],[1,2]]:
                try:
                    if gamemap[i+one][higher] == color and gamemap[i+two][higher] == color:
                        explored.append([i+one,higher])
                        explored.append([i+two,higher])
                        lort = True
                        break
                except:
                    pass
                try:
                    if gamemap[i+one][lower] == color and gamemap[i+two][lower] == color:
                        explored.append([i+one,lower])
                        explored.append([i+two,lower])
                        lort = True
                        break
                except:
                    pass
        for tile in explored:
            k = tile[0]
            l = tile[1]
            gamemap[k][l] = 'poped'
        if makecandies:
            target = random.choice(explored)
            if lort:
                gamemap[target[0]][target[1]] = 'bomb'
            elif len(explored) >= 5:
                gamemap[target[0]][target[1]] = 'rainbow'
            elif len(explored) == 4:
                gamemap[target[0]][target[1]] = 'satrsoton'
    elif gamemap[i][j] == 'bomb':
        for k in [-1,0,1]:
            for l in [-1,0,1]:
                if 0 <= i+k < satr and 0 <= j+l <soton:
                    gamemap[i+k][j+l] = 'poped'
    elif gamemap[i][j] == 'satrsoton':
        if satrsoton == 'satr':
            for temp2 in range(soton):
                gamemap[i][temp2] = 'poped'
        else:
            for temp1 in range(satr):
                gamemap[temp1][j] = 'poped'
    elif gamemap[i][j] == 'rainbow':
        gamemap[i][j] = 'poped'
        for temp1 in range(satr):
            for temp2 in range(soton):
                if gamemap[temp1][temp2] == swapedwith:
                    gamemap[temp1][temp2] = 'poped'
    return gamemap
def candyfill(gamemap,i,j,refills = -1):
    for temp in range(i-1,-1,-1):
        if gamemap[temp][j] !='poped' and gamemap[temp][j] !='blocked':
            gamemap[temp][j],gamemap[i][j] = gamemap[i][j] , gamemap[temp][j]
            i = temp
        else:
            break
    if refills > 0 or refills == -1 :
        counter = {'r':0,'o':0,'y':0,'g':0,'b':0,'p':0}
        for k,l in [[i,j-1],[i,j+1],[i,j-2],[i,j+2],[i-1,j],[i+1,j],[i-2,j],[i+2,j]]:
                try:
                    if gamemap[k][l] in counter:
                        counter[gamemap[k][l]] += 1
                except:
                    pass
        choices = []
        for color in counter:
            if counter[color] < 2:
                choices.append(color)
                if counter[color] == 1:
                    choices.append(color)
        gamemap[i][j] = random.choice(choices)
    return gamemap
if __name__ == '__main__':
    main()
#...make every single empty space blocked so that refreshing dosent generate candies there and you cant swap there