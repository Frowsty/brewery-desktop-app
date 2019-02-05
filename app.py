import pygame
from random import choice
from random import randint
from time import sleep

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (70, 70, 200)
GREEN = (0, 255, 0)
RED = (200, 30, 30)
BLUEISH = (27, 64, 96)
GREY = (103, 109, 114)
position = (0, 0)
page = "Hem"

# set screen size (x,y)
screen_width = 1100
screen_height = 720

# global variable for height of objects to use for scroll animation
aos_height = 720

# hover animation variable
animation_size = [0, 0, 0, 0, 0, 0]

# hover variables
product_1 = "not hover"
product_2 = "not hover"
product_3 = "not hover"
product_4 = "not hover"
product_5 = "not hover"
product_6 = "not hover"

# global variables for each page
draw_hem = True
draw_produkter = False
draw_om_oss = False
draw_kontakt = False

def input_system(mouse_x, mouse_y):
    global page, product_1, product_2, product_3, product_4, product_5, product_6
    # check if mouse1 is pressed
    if pygame.mouse.get_pressed()[0] == True:
        # check if mouse is within any box region
        if mouse_x >= 540 and mouse_x <= 600:
            if mouse_y < 50:
                page = "Hem"
        if mouse_x >= 620 and mouse_x <= 750:
            if mouse_y < 50:
                page = "Produkter"
        if mouse_x >= 770 and mouse_x <= 880:
            if mouse_y < 50:
                page = "Om Oss"
        if mouse_x >= 900 and mouse_x <= 1080:
            if mouse_y < 50:
                page = "Kontakta Oss"
    # check if mouse is hovering products
    if mouse_x >= 150 and mouse_x <= 350:
        if mouse_y >= aos_height + 80 and mouse_y <= aos_height + 320:
            product_1 = "hover"
        else:
            product_1 = "not hover"
    else:
        product_1 = "not hover"
    if mouse_x >= 450 and mouse_x <= 650:
        if mouse_y >= aos_height + 80 and mouse_y <= aos_height + 320:
            product_2 = "hover"
        else:
            product_2 = "not hover"
    else:
        product_2 = "not hover"
    if mouse_x >= 750 and mouse_x <= 950:
        if mouse_y >= aos_height + 80 and mouse_y <= aos_height + 320:
            product_3 = "hover"
        else:
            product_3 = "not hover"
    else:
        product_3 = "not hover"
    if mouse_x >= 150 and mouse_x <= 350:
        if mouse_y >= aos_height + 410 and mouse_y <= aos_height + 650:
            product_4 = "hover"
        else:
            product_4 = "not hover"
    else:
        product_4 = "not hover"
    if mouse_x >= 450 and mouse_x <= 650:
        if mouse_y >= aos_height + 410 and mouse_y <= aos_height + 650:
            product_5 = "hover"
        else:
            product_5 = "not hover"
    else:
        product_5 = "not hover"
    if mouse_x >= 750 and mouse_x <= 950:
        if mouse_y >= aos_height + 410 and mouse_y <= aos_height + 650:
            product_6 = "hover"
        else:
            product_6 = "not hover"
    else:
        product_6 = "not hover"

def draw_navbar(screen, my_font):
    hem_text = my_font.render("Hem", False, GREY)
    produkt_text = my_font.render("Produkter", False, GREY)
    om_oss_text = my_font.render("Om Oss", False, GREY)
    kontakt_text = my_font.render("Kontakta Oss", False, GREY)

    screen.blit(hem_text, (540, 10))
    screen.blit(produkt_text, (620, 10))
    screen.blit(om_oss_text, (770, 10))
    screen.blit(kontakt_text, (900, 10))

def hover_animation():
    global animation_size, product_1, product_2, product_3, product_4, product_5, product_6
    if product_1 == "hover":
        animation_size[0] += 2
        if animation_size[0] >= 20:
            animation_size[0] = 20
    else:
        animation_size[0] -= 2
        if animation_size[0] <= 0:
            animation_size[0] = 0
    if product_2 == "hover":
        animation_size[1] += 2
        if animation_size[1] >= 20:
            animation_size[1] = 20
    else:
        animation_size[1] -= 2
        if animation_size[1] <= 0:
            animation_size[1] = 0
    if product_3 == "hover":
        animation_size[2] += 2
        if animation_size[2] >= 20:
            animation_size[2] = 20
    else:
        animation_size[2] -= 2
        if animation_size[2] <= 0:
            animation_size[2] = 0
    if product_4 == "hover":
        animation_size[3] += 2
        if animation_size[3] >= 20:
            animation_size[3] = 20
    else:
        animation_size[3] -= 2
        if animation_size[3] <= 0:
            animation_size[3] = 0
    if product_5 == "hover":
        animation_size[4] += 2
        if animation_size[4] >= 20:
            animation_size[4] = 20
    else:
        animation_size[4] -= 2
        if animation_size[4] <= 0:
            animation_size[4] = 0
    if product_6 == "hover":
        animation_size[5] += 2
        if animation_size[5] >= 20:
            animation_size[5] = 20
    else:
        animation_size[5] -= 2
        if animation_size[5] <= 0:
            animation_size[5] = 0

def draw_objects(screen, picture):
    global aos_height

    pygame.draw.polygon(screen, BLUE, ([150 - animation_size[0], aos_height + 320 + animation_size[0]], 
                                       [350 + animation_size[0], aos_height + 320 + animation_size[0]],
                                       [350 + animation_size[0], aos_height + 80 - animation_size[0]], 
                                       [150 - animation_size[0], aos_height + 80 - animation_size[0]]
                                       ))
    pygame.draw.polygon(screen, BLUE, ([450 - animation_size[1], aos_height + 320 + animation_size[1]],
                                       [650 + animation_size[1], aos_height + 320 + animation_size[1]], 
                                       [650 + animation_size[1], aos_height + 80 - animation_size[1]], 
                                       [450 - animation_size[1], aos_height + 80 - animation_size[1]]
                                       ))
    pygame.draw.polygon(screen, BLUE, ([750 - animation_size[2], aos_height + 320 + animation_size[2]],
                                       [950 + animation_size[2], aos_height + 320 + animation_size[2]], 
                                       [950 + animation_size[2], aos_height + 80 - animation_size[2]], 
                                       [750 - animation_size[2], aos_height + 80 - animation_size[2]]
                                       ))
    pygame.draw.polygon(screen, BLUE, ([150 - animation_size[3], aos_height + 650 + animation_size[3]], 
                                       [350 + animation_size[3], aos_height + 650 + animation_size[3]], 
                                       [350 + animation_size[3], aos_height + 410 - animation_size[3]], 
                                       [150 - animation_size[3], aos_height + 410 - animation_size[3]]
                                       ))
    pygame.draw.polygon(screen, BLUE, ([450 - animation_size[4], aos_height + 650 + animation_size[4]], 
                                       [650 + animation_size[4], aos_height + 650 + animation_size[4]], 
                                       [650 + animation_size[4], aos_height + 410 - animation_size[4]], 
                                       [450 - animation_size[4], aos_height + 410 - animation_size[4]]
                                       ))
    pygame.draw.polygon(screen, BLUE, ([750 - animation_size[5], aos_height + 650 + animation_size[5]], 
                                       [950 + animation_size[5], aos_height + 650 + animation_size[5]],
                                       [950 + animation_size[5], aos_height + 410 - animation_size[5]], 
                                       [750 - animation_size[5], aos_height + 410 - animation_size[5]]
                                       ))
    screen.blit(picture, (150, aos_height + 80))
    screen.blit(picture, (450, aos_height + 80))
    screen.blit(picture, (750, aos_height + 80))
    screen.blit(picture, (150, aos_height + 410))
    screen.blit(picture, (450, aos_height + 410))
    screen.blit(picture, (750, aos_height + 410))

    pygame.draw.polygon(screen, BLUE, ([150, aos_height + 830], [950, aos_height + 830], [950, aos_height + 1330], [150, aos_height + 1330]))
    
    pygame.draw.polygon(screen, BLUE, ([150, aos_height + 1760], [350, aos_height + 1760], [350, aos_height + 1540], [150, aos_height + 1540]))
    pygame.draw.polygon(screen, BLUE, ([450, aos_height + 1760], [650, aos_height + 1760], [650, aos_height + 1540], [450, aos_height + 1540]))
    pygame.draw.polygon(screen, BLUE, ([750, aos_height + 1760], [950, aos_height + 1760], [950, aos_height + 1540], [750, aos_height + 1540]))


# toggle fullscreen (ON/OFF)
def toggle_fullscreen(fullscreen):
    if fullscreen:
        screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.RESIZABLE
        )
    else:
        screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.FULLSCREEN
        )
    return not fullscreen

def aos():
    global page, aos_height, draw_hem, draw_produkter, draw_om_oss, draw_kontakt
    if page == "Hem":
        draw_hem = True
        aos_height += 30
        if aos_height >= 720:
            aos_height = 720
            draw_kontakt = False
            draw_om_oss = False
            draw_produkter = False
    elif page == "Produkter":
        draw_produkter = True
        if draw_om_oss == True or draw_kontakt == True:
            aos_height += 30
        else:
            aos_height -= 30
        if aos_height < 0 and aos_height > -35:
            aos_height = 0
            draw_hem = False
            draw_om_oss = False
            draw_kontakt = False
    elif page == "Om Oss":
        draw_om_oss = True
        if draw_kontakt == True:
            aos_height += 30
        else:
            aos_height -= 30
        if aos_height <= -720 and aos_height >= -755:
            aos_height = -720
            draw_hem = False
            draw_produkter = False
            draw_kontakt = False
    elif page == "Kontakta Oss":
        draw_kontakt = True
        aos_height -= 30
        if aos_height <= -1440 and aos_height >= -1475:
            aos_height = -1440
            draw_hem = False
            draw_produkter = False
            draw_om_oss = False
        
# define a main function
def main():
    # initialize pygame modules
    pygame.init()
    pygame.font.init()

    # load and set the logo
    logo = pygame.image.load("hasse-800x700.png")
    pygame.display.set_icon(logo)

    # pictures used
    home_picture = pygame.transform.scale(pygame.image.load("hasse-800x700.png"), (720, 680))
    back_picture = pygame.image.load("stars-background.jpg")
    bottle_picture = pygame.transform.scale(pygame.image.load("Hasseflarra.jpg"), (201, 241))

    # set window title
    pygame.display.set_caption("Bryggeri Hemsida")

    # create fonts for text used in the program
    my_font = pygame.font.SysFont("Times New Roman", 30, 1)
    my_large_font = pygame.font.SysFont("Comic Sans MS", 100, 1)

    # create a main surface we can render objects on
    screen = pygame.display.set_mode((screen_width, screen_height))

    # get the size of our main surface and create a sub surface
    background = pygame.Surface(screen.get_size())

    # set previous sub surface to color black and fill the whole surface
    background = background.convert()

    fullscreen = False
    running = True
    
    #some_text = my_font.render(f"Hovering: {page}", False, GREEN)

    clock = pygame.time.Clock()

    # our game loop
    while running:
        # check if any events are happening and if
        # they are related to pressing the exit button
        # in the top right or pressing the ESC key on your keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
                quit()
            if pygame.key.get_pressed()[pygame.K_F12]:
                fullscreen = toggle_fullscreen(fullscreen)

        # set background of the application
        # screen.fill(BLUEISH)
        screen.blit(back_picture, (-290, aos_height - 720))

        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        input_system(mouse_pos_x, mouse_pos_y)

        if draw_hem == True:
            screen.blit(home_picture, (190, aos_height - 690))

        # some_text = my_font.render(f"Page: {page}", False, GREEN)
        # screen.blit(some_text, (10, 10))
    
        draw_objects(screen, bottle_picture)
        draw_navbar(screen, my_font)

        if draw_produkter == True and draw_om_oss == False and draw_kontakt == False and draw_hem == False:
            hover_animation()
        aos()

        # limit FPS (Frames per seconds)
        clock.tick(30)

        # update screen
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
