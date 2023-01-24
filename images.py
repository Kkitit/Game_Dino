import pygame

pygame.init()


icon = pygame.image.load("Background/icon.png")
menu_backg = pygame.image.load('Background/Menu.jpg')
land = pygame.image.load('Background/Land.jpg')

cactus_img = [pygame.image.load('Objects/Cactus0.png'), pygame.image.load('Objects/Cactus1.png'),
              pygame.image.load('Objects/Cactus2.png')]

cactus_options = [69, 449, 37, 410, 40, 420]

stone_img = [pygame.image.load('Objects/Stone0.png'), pygame.image.load('Objects/Stone1.png')]

cloud_img = [pygame.image.load('Objects/Cloud0.png'), pygame.image.load('Objects/Cloud1.png')]

cloud_img[0] = pygame.transform.scale(cloud_img[0], (93, 51))
cloud_img[1] = pygame.transform.scale(cloud_img[1], (120, 56))

dino_img = [pygame.image.load('Dino/Dino0.png'), pygame.image.load('Dino/Dino1.png'),  pygame.image.load('Dino/Dino2.png'),
            pygame.image.load('Dino/Dino3.png'),  pygame.image.load('Dino/Dino4.png')]

bird_img = [pygame.image.load('Bird/Bird0.png'), pygame.image.load('Bird/Bird1.png'),
            pygame.image.load('Bird/Bird2.png'),pygame.image.load('Bird/Bird3.png'),
            pygame.image.load('Bird/Bird4.png'), pygame.image.load('Bird/Bird5.png')]

health_img = pygame.image.load('Effects/heart.png')
health_img = pygame.transform.scale(health_img, (30, 30))

bullet_img = pygame.image.load('Effects/shot.png')
bullet_img = pygame.transform.scale(bullet_img, (30, 9))

light_img = [pygame.image.load('Effects/Light0.png'), pygame.image.load('Effects/Light1.png'), pygame.image.load('Effects/Light2.png'),
             pygame.image.load('Effects/Light3.png'), pygame.image.load('Effects/Light4.png'), pygame.image.load('Effects/Light5.png'),
             pygame.image.load('Effects/Light6.png'), pygame.image.load('Effects/Light7.png'),
             pygame.image.load('Effects/Light8.png'), pygame.image.load('Effects/Light9.png'), pygame.image.load('Effects/Light10.png') ]


