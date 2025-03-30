import pygame


pygame.init()

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

image = pygame.transform.scale(pygame.image.load("image.jpg").convert(), (50, 50))
x = 0
y = 0

windowOn = True
while windowOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowOn = False
    
    list_k_pressed = pygame.key.get_pressed()
    if list_k_pressed[pygame.K_LEFT]:
        x -= 1
    if list_k_pressed[pygame.K_RIGHT]:
        x += 1
    if list_k_pressed[pygame.K_UP]:
        y -= 1
    if list_k_pressed[pygame.K_DOWN]:
        y += 1

    screen.fill((0, 0, 0))
    screen.blit(image, (x, y))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()