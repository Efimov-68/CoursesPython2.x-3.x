# ******************* 
# My Game Лыжник Test 
# ******************* 

import pygame, sys, random

skier_images = ['skier_down.png',
                'skier_right1.png',
                'skier_right2.png',
                'skier_left2.png',
                'skier_left1.png']

class SkierClass(pygame.sprite.Sprite):# Создаем лыжника
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('skier_down.png')
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction):# Поворачиваем лыжника
        self.angle = self.angle + direction
        if self.angle < -2: self.angle = -2
        if self.angle > 2: self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed

    def move(self, speed): # Двигаем лыжника "влево" и "вправо"
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

class ObstacleClass(pygame.sprite.Sprite):# Создаем деревья и флаги
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False
        
    def update(self):# Обеспечиваем прокрутку игрового поля
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery < -32:# Удаляем препятствия, ушедшие за верхнюю границу экрана
            self.kill()

def create_map():      # Создаем экран со случайным образом
    global obstacles   # расположенными деревьями и флагами
    locations = []
    for i in range(10):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20 + 640]
        if not (location in locations):
            locations.append(location)
            type = random.choice(['tree', 'flag'])
            if type == 'tree': img = 'skier_tree.png'
            elif type == 'flag': img = 'skier_flag.png'
            obstacle = ObstacleClass(img, location, type)
            obstacles.add(obstacle)

def animate(): #Обновляем экран
    screen.fill([255, 255, 255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()
    
pygame.init() # Готовим все к запуску
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
obstacles = pygame.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None, 50) #****
runing = True # Запускаем основной цикл
while runing: #****
    clock.tick(30) #<--Обновляем графику 30 раз в секунду
    for event in pygame.event.get(): # Проверяем нажатие клавиш или закрытие окна
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed) # <-- Перемещаем лыжника

    map_position += speed[1] # <-- Прокручиваем экран

    if map_position >= 640: #Создаем новый экран с декорациями
        create_map()
        map_position = 0
        
    hit = pygame.sprite.spritecollide(skier, obstacles, False)# Проверяем столкновение
    if hit: # с деревьями и взятие флагов
        if hit[0].type == 'tree' and not hit[0].passed:
            points = points - 100
            skier.image = pygame.image.load('skier_crash.png')
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load('skier_down.png')
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == 'flag' and not hit[0].passed:
            points += 10
            hit[0].kill()

    obstacles.update()
    score_text = font.render('Score: ' + str(points), 1, (0, 0, 0)) # <-- Показываем счет
    animate()
pygame.quit()

# *** #
# END #
# *** #
