import pygame
import time

def text_object(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    global show_message
    if not show_message:
        return
    largeText = pygame.font.SysFont('times', 100)
    text_surf, text_rect = text_object(text, largeText)
    text_rect.center = (display_width*0.5, display_height*0.5)

    screen.blit(text_surf, text_rect)
    show_message = False

def check_collision(player, obstacle):
    if not isinstance(player, Sprite):
        raise ValueError("Cannot use check collision with non sprites for player")
    if not isinstance(obstacle, Sprite):
        raise ValueError("Cannot use check collision with non sprites for obstacle")

    squared_summed_radii = (player.radius + obstacle.radius)**2
    distance = (player.x - obstacle.x)**2 + (player.y - obstacle.y)**2

    if squared_summed_radii >= distance:
        return  True
    else:
        return False

class Sprite:
    ''' A sprite object '''
    x = 0
    y = 0
    radius = 1
    img = ""

    def __init__(self, x, y, radius, img):
        self.x = x
        self.y = y
        self.radius = radius
        self.img = pygame.image.load(img)

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

pygame.init()

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("My Simple Pygame")

blue = (0, 0, 255)
#white = pygame.Color(255, 255, 255, 255)
white = (255, 255, 255)
#black = (0, 0, 0, 255)
black = (0, 0, 0)
# mario_img = pygame.image.load('mario_idle_01.png')

y = display_height * 0.5
x = display_width * 0.5

otherx = 50
othery = 100

mario_sprite = Sprite(x, y, 32, 'mario_idle_01.png')
mushroom_sprite = Sprite(otherx, othery, 16, 'mushroom.png')

obst_rect = pygame.Rect(200,100,30,30)

is_running = True

clock = pygame.time.Clock()

show_message = True


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # input
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        mario_sprite.y += 5
    elif pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        mario_sprite.y -= 5

    if pressed_keys[pygame.K_RIGHT]:
        mario_sprite.x += 5
    elif pressed_keys[pygame.K_LEFT]:
        mario_sprite.x -= 5

    if pressed_keys[pygame.K_SPACE]:
        show_message = True

    # bounds
    mario_sprite.x = max(mario_sprite.x, 0)
    mario_sprite.x = min(mario_sprite.x, display_width - (mario_sprite.radius*2))
    mario_sprite.y = max(mario_sprite.y, 0)
    mario_sprite.y = min(mario_sprite.y, display_height - (mario_sprite.radius*2))

    if check_collision(mario_sprite, mushroom_sprite):
        show_message = True


    screen.fill(white)
    #screen.blit(mario_img, (x, y))
    mario_sprite.render(screen)
    mushroom_sprite.render(screen)


    pygame.draw.rect(screen, blue, obst_rect)

    message_display("On the top")
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
