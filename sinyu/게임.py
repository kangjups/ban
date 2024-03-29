# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:14:42 2023

@author: angel
"""

import pygame 
import random
# Head, body, tail
class cls_card:
    def __init__(self,img,mp3,name,energy,damage,head,body,tail):
        self.img = pygame.image.load(img)
        self.sound = pygame.mixer.Sound(mp3)
        self.name = name
        self.energy = energy
        self.damage = damage
                
        
        self.head = head
        self.body = body
        self.tail = tail
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        self.font = pygame.font.SysFont(None,30)
    
     
    def screen(self,screen):
        screen.blit(self.font.render(str(self.card_time),True,self.BLACK),(self.x,self.y))

def fn_start():
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    #pygame.display.set_caption("school")
    background = pygame.image.load("back_ground_0.png")
    main_sound = pygame.mixer.Sound("시작 음악.mp3")
    main_sound.set_volume(0.8)
    main_sound.play(-1)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    
            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x_p, y_p = pygame.mouse.get_pos()    
                    if x_p > 200 and x_p < 600 and y_p > 340 and y_p < 390:
                        pygame.quit()    
                        return True
                    if x_p > 200 and x_p < 600 and y_p > 450 and y_p < 500:
                        print("setting")
                    if x_p > 200 and x_p < 600 and y_p > 540 and y_p <610:
                        pygame.quit()    
                        return False
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            
        screen.blit(background,(0,0))
        pygame.display.update()
         
    pygame.quit()

def fn_main(floor,position,hp,ex,gold): # 플레이어의 초기 x,y 위치 / 층 수 / 리스트 속 플레이어 위치
    
    pygame.init() # 게임 초기화
    
    # 게임 화면 크기  
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    main_sound = pygame.mixer.Sound("메인 음악.mp3")
    main_sound.set_volume(0.4)
    main_sound.play(-1)
    
    img = 1
    
    # 이미지 불러오기 
    back = pygame.image.load("back_ground_1.png") # 바탕화면
    event_ = pygame.image.load("event.png") # 이벤트 
    enemy = pygame.image.load("enemy.png") # 적 
    bose = pygame.image.load("bose.png") # 보스
    
    bag = pygame.image.load("bag.png")
    
    player = pygame.image.load("player.png") # 플레이어
    boxs[position] = 'player'
    
    ex = cls_text_create("Ex :",ex,112,20)
    hp = cls_text_create("Hp :",hp,270,20)
    gold = cls_text_create("gold :",gold,445,20)
    
    card_sword = cls_card("소드 타격.png","소드 타격.mp3","card_sword",1,4,"red","red","red")
    card_defending = cls_card("수비.png","pop.mp3","card_sword",2,4,"red","red","green")
    card_arrow = cls_card("애로우.png","애로우.mp3","card_sword",2,6,"red","green","green")
    card_search = cls_card("탐색.png","pop.mp3","card_sword",1,1,"red","green","red")
    card_bomb = cls_card("폭탄 펑!.png","pop.mp3","card_sword",3,8,"red","green","yellow")
    
    all_cards = [card_sword,card_defending,card_arrow,card_search,card_bomb]
    my_cards = [card_sword,card_defending,card_arrow,card_search]
    
    card_1 = my_cards[0]
    card_2 = my_cards[1]
    card_3 = my_cards[2]
    card_4 = my_cards[3]
    
    test_box = pygame.image.load("test_box.png")
    # 루프
    running = True
    while running:
        # 키보드를 누루는 이벤트가 발생했을 때 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
            if event.type == pygame.KEYDOWN and img == 1 :
                if event.key == pygame.K_p: 
                    running = False
                
                if event.key == pygame.K_w:
                    boxs[position] = '-'
                    position += 7
                    if position >= len(boxs):
                        position -= 7 
                        
                    else :
                        pygame.quit()
                        return position,card_1,card_2,card_3,card_4
                        
                if event.key == pygame.K_d: 
                    boxs[position] = '-'
                    position += 1
                    if position >= len(boxs):
                        position -= 1 
                        
                    else :
                        pygame.quit()
                        return position,card_1,card_2,card_3,card_4
                        
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x, y = pygame.mouse.get_pos()
            
                    if x > 700 and x < 800 and y > 700 and y < 800:
                        img = 2
                        
                    if x > 0 and x < 100 and y > 700 and y < 800:
                        img = 1
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            
        # 이미지 그리기 
        if img == 1 :
            
            screen.blit(back,(0,0)) # 바탕화면
            hp.screen(screen)
            ex.screen(screen)
            gold.screen(screen)
            
            
            # 박스들 
            for i in range(len(boxs)):
                if i == floor:
                    floor += 7
                if i < floor :
                    a = 80*(i-(floor-7)) + 120  # 길이 
                    b = 800-(80*(floor/7)) -120 # 높이 
                 
                    if boxs[i] == 'enemy':
                        screen.blit(enemy,(a,b))
                        
                    elif boxs[i] == 'event_':
                        screen.blit(event_,(a,b))
                        
                    elif boxs[i] == 'bose':
                        screen.blit(bose,(a,b))
                        
                    elif boxs[i] == 'player':
                        screen.blit(player,(a,b))
                        
                if i == len(boxs)-1:
                    floor = 7
        if img == 2:
            screen.blit(bag,(0,0))
            for i in range(len(my_cards)):
                #screen.blit(all_cards[i].img,(50+(200*i),100))
                screen.blit(test_box,(50+(200*i),100))
            for i in range(len(all_cards)) :
                #screen.blit(all_cards[i].img,(50+(200*i),400))
                screen.blit(test_box,(50+(200*i),100))
        
        if img == 3:
            back = pygame.image.load("back_ground_1.png")
        
        # 업데이트
        pygame.display.update()
        
    # 초기화
    pygame.quit()                                                                    
    


class cls_character:
    def __init__(self,img,name,x,y,hp,damage):
        self.img = pygame.image.load(img)
        self.name = name
        self.x , self.y = x,y
        #self.max_hp = max_hp
        self.hp = hp
        self.damage = damage
        
        self.count = 0
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        self.font = pygame.font.SysFont(None,30)
        self.hp_img = self.font.render(str(self.hp),True,self.BLACK)
        self.name_img = self.font.render(str(self.name),True,self.BLACK)
    
    def time(self):
        self.count += 1
        if self.count >= 540 :
            
            self.count = 0
            return True
        else :
            return False
    def re_img(self,img):
        self.img = pygame.image.load(img)
        
    def screen(self,screen):
        screen.blit(self.img,(self.x,self.y))
        screen.blit(self.hp_img,(self.x+80,self.y+170))
        screen.blit(self.name_img,(self.x+20,self.y+170))
        
    def hp_change(self,hp):
        self.hp -= hp
        self.hp_img = self.font.render(str(self.hp),True,self.BLACK)
        
class cls_text_create:
    def __init__(self,name,text,x,y):
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.font = pygame.font.SysFont(None,40)
        
        self.name = name
        self.text = text
        self.text_img = self.font.render(str(self.text),True,self.BLACK)
    
        self.x = x
        self.y = y
            
    def screen(self,screen):
        screen.blit(self.text_img,(self.x,self.y))
    
    def text_change(self):
        #self.text_img = self.font.render(self.name + str(self.text),True,self.BLACK)
        self.text_img = self.font.render(str(self.text),True,self.BLACK)

def fn_fight(hp,energy,ex,gold,card_1,card_2,card_3,card_4):
    pygame.init()
    
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    main_sound = pygame.mixer.Sound("전투 음악.mp3")
    main_sound.set_volume(0.3)
    main_sound.play(-1)
    
    back = pygame.image.load("back.png")
    
    player = cls_character("man_0.png","ban",180,100,hp,20)
    woulf = cls_character("nemo_0.png","nemo",540,100,100,4)
    
    monster_sound = pygame.mixer.Sound("monster.mp3")
    monster_sound.set_volume(0.2)
    
    ba = pygame.image.load("ba.png")
    ba_x = 50
    ba_y = 325
    ba_sound = pygame.mixer.Sound("룰렛 소리.mp3")
    
    
    ex = cls_text_create("Ex :",ex,75,18)
    gold = cls_text_create("gold :",gold,205,18)
    energy = cls_text_create("energy :",energy,39,245)  
    
    sword_up = pygame.image.load("sword.png")
    sword_down = pygame.image.load("sword_down.png")
    sword_left = pygame.image.load("sword_left.png")
    sword_right = pygame.image.load("sword_right.png")
    
    sword = sword_up
    
    sword_x_pos = ba_x
    sword_y_pos = ba_y - 12
    sword_speed = 2
    
    green =  pygame.image.load("green.png")
    up_down_random = [60,86,112,138,164] #26   
    green_position = random.choice(up_down_random)
    
    yellow =  pygame.image.load("yellow.png")
    yellow_position = random.choice(up_down_random)
    
    red =  pygame.image.load("red.png")
    right_left_random = [10+ba_y,36+ba_y,62+ba_y,88+ba_y,114+ba_y]
    red_position = random.choice(right_left_random)
    
    blue =  pygame.image.load("blue.png")
    blue_position = random.choice(right_left_random)
    
    red_ball = pygame.image.load("red_ball.png")
    blue_ball = pygame.image.load("blue_ball.png")
    green_ball = pygame.image.load("green_ball.png")
    yellow_ball = pygame.image.load("yellow_ball.png")
    
    balls = []
    
    t = 0
    ball_time = 0
    
    running = True
    while running:
        
      
        t += 1 
        if t >= 280 :
            if energy.text < 4:    
                energy.text += 1
                energy.text_change()
            t = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    running = False
                    
                if event.key == pygame.K_w:
                    sword = sword_up
                    sword_x_pos = ba_x
                    sword_y_pos = ba_y - 12
                    
                    
                if event.key == pygame.K_s:
                    sword = sword_down
                    sword_x_pos = ba_x
                    sword_y_pos = ba_y + 100 + 12
                    
                if event.key == pygame.K_a:
                    sword = sword_left
                    sword_x_pos = ba_x - 12
                    sword_y_pos = ba_y
                    
                    
                if event.key == pygame.K_d:
                    sword = sword_right
                    sword_x_pos = ba_x + 100 + 12
                    sword_y_pos = ba_y 
                    
                    
                if event.key == pygame.K_SPACE:
                    if sword == sword_up and sword_x_pos + 25 >= green_position and sword_x_pos + 25  <= green_position + 50:
                        balls.append("green")
                        ba_sound.play()
                        
                        up_down_random = [60,86,112,138,164]
                        green_position = random.choice(up_down_random)
                        
                    elif sword == sword_down and sword_x_pos + 25 >= yellow_position and sword_x_pos + 25  <= yellow_position + 50:
                        balls.append("yellow")
                        ba_sound.play()
                        
                        up_down_random = [60,86,112,138,164]
                        yellow_position = random.choice(up_down_random)
                        
                    elif sword == sword_left and sword_y_pos + 25 >= red_position and sword_y_pos + 25  <= red_position + 50:
                        balls.append("red")
                        ba_sound.play()
                        right_left_random = [10+ba_y,36+ba_y,62+ba_y,88+ba_y,114+ba_y]
                        red_position = random.choice(right_left_random )
                        
                    elif sword == sword_right and sword_y_pos + 25 >= blue_position and sword_y_pos + 25  <= blue_position + 50:
                        balls.append("blue")
                        ba_sound.play()
                        right_left_random = [10+ba_y,36+ba_y,62+ba_y,88+ba_y,114+ba_y]
                        blue_position = random.choice(right_left_random )
                    
                    else :
                        print("스킬 실패")         
                        balls.clear()
                        
                   
        if sword == sword_up or sword == sword_down:
            sword_x_pos += sword_speed
            
            if sword_x_pos + 25 >= ba_x + 150 :
                sword_speed = -sword_speed
            if sword_x_pos + 25 <= ba_x:
                
                sword_speed = -1*sword_speed
                
        if sword == sword_left or sword == sword_right:
            sword_y_pos += sword_speed
            
            if sword_y_pos + 25 >= ba_y + 150 :
                sword_speed = -sword_speed
                
            if sword_y_pos + 25 <= ba_y:
                sword_speed = -1*sword_speed
        
        if len(balls) >= 3:
            player.re_img("man_1.png")
            if balls[0] == card_1.head and balls[1] == card_1.body and balls[2] == card_1.tail and energy.text >= card_1.energy:    
                card_1.sound.play()
                energy.text -= card_1.energy
                woulf.hp_change(player.damage+card_1.damage)
                
            elif balls[0] == card_2.head and balls[1] == card_2.body and balls[2] == card_2.tail and energy.text >= card_2.energy :                  
                card_2.sound.play()
                energy.text -= card_2.energy
                woulf.hp_change(player.damage+card_2.damage)
              
                
            elif balls[0] == card_3.head and balls[1] == card_3.body and balls[2] == card_3.tail and energy.text >= card_3.energy :                  
                energy.text -= card_3.energy
                card_3.sound.play()
                woulf.hp_change(player.damage+card_3.damage)
          
                
            elif balls[0] == card_4.head and balls[1] == card_4.body and balls[2] == card_4.tail and energy.text >= card_4.energy :                  
                energy.text -= card_4.energy
                card_4.sound.play()
                woulf.hp_change(player.damage+card_4.damage)
          
            energy.text_change()
            balls.clear()
        
        ball_time += 1
        
        if ball_time >= 45:
            player.re_img("man_0.png")
            ball_time = 0
            
        if woulf.time() == False and  woulf.count >= 300 :
            woulf.img = pygame.image.load("nemo_0.png")
            monster_sound.stop()
    
        if woulf.time() == True  :
            monster_sound.play()
            woulf.img = pygame.image.load("nemo_1.png")
            player.hp_change(woulf.damage)
    
        
        if woulf.hp <= 0 :
            pygame.quit()
            return random.randint(3,6),random.randint(4,8), player.hp
        
        if player.hp <= 0 :
            pygame.quit()
            return random.randint(3,6),random.randint(4,8), player.hp
        
        screen.blit(back,(0,0))
        
        player.screen(screen)
        woulf.screen(screen)
        
        energy.screen(screen)
        gold.screen(screen)
        ex.screen(screen)
        
        screen.blit(ba,(ba_x,ba_y))
        
        for i in range(len(balls)):
            
            if balls[i] == "green" :
                screen.blit(green_ball,(ba_x + 20 + (i*40) ,ba_y + 105))
              
            if balls[i] == "yellow" :
                screen.blit(yellow_ball,(ba_x + 20 + (i*40) ,ba_y + 105))
                
            if balls[i] == "blue" :
                screen.blit(blue_ball,(ba_x + 20 + (i*40) ,ba_y + 105))
                
            if balls[i] == "red" :
                screen.blit(red_ball,(ba_x + 20 + (i*40) ,ba_y + 105))
                   
                
        screen.blit(green,(green_position, ba_y + 2))
        screen.blit(yellow,(yellow_position, ba_y + 140))
        screen.blit(red,(ba_x + 2, red_position))
        screen.blit(blue,(ba_x + 140, blue_position))
        
        screen.blit(sword,(sword_x_pos,sword_y_pos))
        
        screen.blit(card_1.img,(300,350))
        screen.blit(card_2.img,(420,350))
        screen.blit(card_3.img,(540,350))
        screen.blit(card_4.img,(660,350))
        
        pygame.display.update()
    
    pygame.quit()
   
if __name__ == "__main__":
    running = fn_start()
    
    # 박스리스트
    boxs = ['-'] * 49
    
    # 층,리스트 속 플레이어 위치
    
    floor = 7
    position = 0
    
    # 박스리스트 채우기
    for i in range(len(boxs)):
        boxs[0] = 'player' 
        boxs[len(boxs)-1] = 'bose'
        if boxs[i] == '-' :
            boxs[i] = random.choice(['enemy','event_'])
            
    inv = {"energy" : 1,"gold" : 0,"ex" : 0}
    hp = 100
    gold = 0
    ex = 0
    print(position,"0")
    # 루프
    while running:
        position,card_1,card_2,card_3,card_4 = fn_main(floor,position,hp,inv["ex"],inv["gold"])
        if position == None :
            break
        if boxs[position] == 'enemy':
            gold,ex,hp = fn_fight(hp,inv["energy"],inv["ex"],inv["gold"],card_1,card_2,card_3,card_4)
            
            inv["gold"] += gold
            inv["ex"] += ex
            
        elif boxs[position] == 'event_':
            e = random.randint(0,1)
            
            if e == 0:
                print("악마가 나타나 당신에게 말을 겁니다... 넌 무엇을 위해 싸우지? : ")
                inv["gold"] += 4
                hp += 5
                #e = int(input("정의를 위해 싸운다(0)/욕망을 위해 싸운다(1)"))
                #if e == 0:
                 #   print("악마는 당신의 대답을 마음에 들어하지 않습니다... 악마에게 공격을 당하여 -5의 피해를 입습니다")
               #     hp -= 5
               # if e == 1:
                #    print("악마는 당신의 대답을 마음에 들어 합니다... 악마가 당시에게 돈을 줍니다")
                  #  inv["gold"] += 5
                    
            if e == 1:
                print("체력이 회복 됩니다")
                hp += 27
        elif boxs[position] == 'bose':
            print("업데이트 준비중 입니다")
        
        if hp <= 0:
                break       
                print("게임 오버")
    
    
    
    
    
    
    
    