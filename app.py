import os
import pygame
import FroPy as fp
from time import sleep

# preset color variables
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (70, 70, 200)
GREEN = (0, 255, 0)
DARK_GREEN = (13, 196, 13)
DARK_RED = (196, 13, 13)
RED = (255, 0, 0)
BLUEISH = (27, 64, 96)
GREY = (103, 109, 114)
position = (0, 0)

# global page related variables
page = "Hem"
sub_page = 1
draw_sub_1 = True
draw_sub_2 = False
draw_sub_3 = False
draw_sub_4 = False
draw_hem = True
draw_produkter = False
draw_om_oss = False
draw_kontakt = False

# age restriction related variables
did_accept = ''

# set screen size (x,y)
screen_width = 1100
screen_height = 720

# global variable for height of objects to use for scroll animation
aos_height = 720
aos_width = 1280

# hover animation variable
animation_size = [0, 0, 0, 0, 0, 0]

# hover variables
product_1 = "not hover"
product_2 = "not hover"
product_3 = "not hover"
product_4 = "not hover"
product_5 = "not hover"
product_6 = "not hover"

# input system for navbar and products
def input_system(screen, mouse_x, mouse_y):
    global page, product_1, product_2, product_3, product_4, product_5, product_6
    # check if mouse1 is pressed
    if pygame.mouse.get_pressed()[0] == True:
        # check if mouse is within any box region
        if mouse_x >= 540 and mouse_x <= 600:
            if mouse_y < 35:
                page = "Hem"
        if mouse_x >= 620 and mouse_x <= 750:
            if mouse_y < 35:
                page = "Produkter"
        if mouse_x >= 770 and mouse_x <= 880:
            if mouse_y < 35:
                page = "Om Oss"
        if mouse_x >= 900 and mouse_x <= 1080:
            if mouse_y < 35:
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

# draw the navbar we use to navigate the application
def draw_navbar(screen, my_font):
    hem_text = my_font.render("Hem", False, GREY)
    produkt_text = my_font.render("Produkter", False, GREY)
    om_oss_text = my_font.render("Om Oss", False, GREY)
    kontakt_text = my_font.render("Kontakta Oss", False, GREY)

    screen.blit(hem_text, (540, 10))
    screen.blit(produkt_text, (620, 10))
    screen.blit(om_oss_text, (770, 10))
    screen.blit(kontakt_text, (900, 10))

# the animation function when hovering a product
def hover_animation():
    global animation_size, product_1, product_2, product_3, product_4, product_5, product_6
    if product_1 == "hover":
        animation_size[0] += 1
        if animation_size[0] >= 10:
            animation_size[0] = 10
    else:
        animation_size[0] -= 1
        if animation_size[0] <= 0:
            animation_size[0] = 0
    if product_2 == "hover":
        animation_size[1] += 1
        if animation_size[1] >= 10:
            animation_size[1] = 10
    else:
        animation_size[1] -= 1
        if animation_size[1] <= 0:
            animation_size[1] = 0
    if product_3 == "hover":
        animation_size[2] += 1
        if animation_size[2] >= 10:
            animation_size[2] = 10
    else:
        animation_size[2] -= 1
        if animation_size[2] <= 0:
            animation_size[2] = 0
    if product_4 == "hover":
        animation_size[3] += 1
        if animation_size[3] >= 10:
            animation_size[3] = 10
    else:
        animation_size[3] -= 1
        if animation_size[3] <= 0:
            animation_size[3] = 0
    if product_5 == "hover":
        animation_size[4] += 1
        if animation_size[4] >= 10:
            animation_size[4] = 10
    else:
        animation_size[4] -= 1
        if animation_size[4] <= 0:
            animation_size[4] = 0
    if product_6 == "hover":
        animation_size[5] += 1
        if animation_size[5] >= 10:
            animation_size[5] = 10
    else:
        animation_size[5] -= 1
        if animation_size[5] <= 0:
            animation_size[5] = 0

# draw all the page objects within this function
def draw_objects(screen, picture, picture_2, mouse_x, mouse_y):
    global aos_height, aos_width, sub_page, page

    # produkter page
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

    # sub page 1
    screen.blit(picture, (aos_width - 1130, aos_height + 80))
    screen.blit(picture, (aos_width - 830, aos_height + 80))
    screen.blit(picture, (aos_width - 530, aos_height + 80))
    screen.blit(picture, (aos_width - 1130, aos_height + 410))
    screen.blit(picture, (aos_width - 830, aos_height + 410))
    screen.blit(picture, (aos_width - 530, aos_height + 410))
    # sub page 2
    screen.blit(picture, (aos_width + 150, aos_height + 80))
    screen.blit(picture, (aos_width + 450, aos_height + 80))
    screen.blit(picture, (aos_width + 750, aos_height + 80))
    screen.blit(picture, (aos_width + 150, aos_height + 410))
    screen.blit(picture, (aos_width + 450, aos_height + 410))
    screen.blit(picture, (aos_width + 750, aos_height + 410))
    # sub page 3
    screen.blit(picture, (aos_width + 1430, aos_height + 80))
    screen.blit(picture, (aos_width + 1730, aos_height + 80))
    screen.blit(picture, (aos_width + 2030, aos_height + 80))
    screen.blit(picture, (aos_width + 1430, aos_height + 410))
    screen.blit(picture, (aos_width + 1730, aos_height + 410))
    screen.blit(picture, (aos_width + 2030, aos_height + 410))
    # sub page 4
    screen.blit(picture, (aos_width + 2710, aos_height + 80))
    screen.blit(picture, (aos_width + 3010, aos_height + 80))
    screen.blit(picture, (aos_width + 3310, aos_height + 80))
    screen.blit(picture, (aos_width + 2710, aos_height + 410))
    screen.blit(picture, (aos_width + 3010, aos_height + 410))
    screen.blit(picture, (aos_width + 3310, aos_height + 410))

    # page system for products
    # initialize the two buttons for prev/next page
    next_page_btn = fp.Button(BLUEISH, 970, aos_height + 360, 70, 25, '>>>')
    back_page_btn = fp.Button(BLUEISH, 50, aos_height + 360, 70, 25, '<<<')
    
    # draw buttons with the conditions of
    # not being on the last / first page
    if sub_page < 4:
        next_page_btn.draw(screen)
    if sub_page > 1:
        back_page_btn.draw(screen)
    
    # check if the buttons are being clicked
    # if they are we want to switch sub_page
    # depending on which sub_page it is currently on
    # and which button is being pressed
    if next_page_btn.is_hover((mouse_x, mouse_y)) and sub_page < 4:
        if pygame.mouse.get_pressed()[0] == True:
            if sub_page == 1:
                sub_page = 2
                sleep(0.12)
            elif sub_page == 2:
                sub_page = 3
                sleep(0.12)
            elif sub_page == 3:
                sub_page = 4
                sleep(0.12)
    if back_page_btn.is_hover((mouse_x, mouse_y)) and sub_page > 1:
        if pygame.mouse.get_pressed()[0] == True:
            if sub_page == 2:
                sub_page = 1
                sleep(0.12)
            elif sub_page == 3:
                sub_page = 2
                sleep(0.12)
            elif sub_page == 4:
                sub_page = 3
                sleep(0.12)
    
    # om oss page
    # pygame.draw.polygon(screen, BLUE, ([150, aos_height + 830], 
    #                                    [950, aos_height + 830], 
    #                                    [950, aos_height + 1330], 
    #                                    [150, aos_height + 1330]
    #                                    ))
    screen.blit(picture_2, (150, aos_height + 830))

    # kontakta oss page
    pygame.draw.polygon(screen, BLUE, ([150, aos_height + 1760], 
                                       [350, aos_height + 1760], 
                                       [350, aos_height + 1540], 
                                       [150, aos_height + 1540]
                                       ))
    pygame.draw.polygon(screen, BLUE, ([450, aos_height + 1760], 
                                       [650, aos_height + 1760], 
                                       [650, aos_height + 1540], 
                                       [450, aos_height + 1540]
                                       ))
    pygame.draw.polygon(screen, BLUE, ([750, aos_height + 1760], 
                                       [950, aos_height + 1760], 
                                       [950, aos_height + 1540], 
                                       [750, aos_height + 1540]
                                       ))


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

# side slide animation for the product page
def aos_side_slide():
    global sub_page, page, aos_width, draw_sub_1, draw_sub_2, draw_sub_3, draw_sub_4
    if page == "Produkter":
        if sub_page == 1:
            draw_sub_1 = True
            aos_width += 30
            if aos_width >= 1280 and aos_width <= 1310:
                aos_width = 1280
                draw_sub_2 = False
                draw_sub_3 = False
                draw_sub_4 = False
        elif sub_page == 2:
            draw_sub_2 = True
            if draw_sub_3 == True:
                aos_width += 30
            else:
                aos_width -= 30
            if aos_width >= -30 and aos_width <= 0:
                aos_width = 0
                draw_sub_1 = False
                draw_sub_3 = False
                draw_sub_4 = False
        elif sub_page == 3:
            draw_sub_3 = True
            if draw_sub_4 == True:
                aos_width += 30
            else:
                aos_width -= 30
            if aos_width >= -1310 and aos_width <= -1280:
                aos_width = -1280
                draw_sub_1 = False
                draw_sub_2 = False
                draw_sub_4 = False
        elif sub_page == 4:
            draw_sub_4 = True
            aos_width -= 30
            if aos_width >= -2590 and aos_width <= -2560:
                aos_width = -2560
                draw_sub_1 = False
                draw_sub_2 = False
                draw_sub_3 = False

# very much like AOS in javascript (Animation on scroll)
# without the extra animation features when an object becomes visible
# just the infinite scroll feature that OG AOS is offering
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

# function for the age restriction page to allow / now allow
# users below the age of 18, saves a cookie like file that
# reads what option the chose and then instead of having to accept
# everytime they open the app it reads the "cookie" to proceed
def age_restriction(screen, font, large_font, mouse_x, mouse_y):
    global did_accept
    #f = open("meta-data.txt", 'w')
    pygame.draw.polygon(screen, BLUEISH, ([50, 50], 
                                          [1050, 50],
                                          [1050, 670], 
                                          [50, 670]
                                          ))
    age_restrict_txt1 = font.render("För att få tillgång till appen krävs det att du är 18+ enligt svensk lag.", 0, WHITE)
    age_restrict_txt2 = font.render("är du 18 år eller över?", 0, WHITE)
    # age_restrict_txt_yes = large_font.render("1 = JA!", 0, WHITE)
    # age_restrict_txt_no = large_font.render("| 2 = NEJ!", 0, WHITE)
    screen.blit(age_restrict_txt1, (120, 100))
    screen.blit(age_restrict_txt2, (400, 280))
    # screen.blit(age_restrict_txt_yes, (100, 350))
    # screen.blit(age_restrict_txt_no, (500, 350))

    yes_btn = fp.Button(GREEN, 290, 350, 200, 100, 'JA!')
    no_btn = fp.Button(RED, 580, 350, 200, 100, 'NEJ!')
    yes_btn.draw(screen)
    no_btn.draw(screen)
    if yes_btn.is_hover((mouse_x, mouse_y)) == True:
        yes_btn.color = DARK_GREEN
        yes_btn.draw(screen)
        if pygame.mouse.get_pressed()[0] == True:
            meta_file = open("meta-data.txt", 'w')
            meta_file.write("I accept")
            did_accept = "I accept"
            meta_file.close()
    elif no_btn.is_hover((mouse_x, mouse_y)) == True:
        no_btn.color = DARK_RED
        no_btn.draw(screen)
        if pygame.mouse.get_pressed()[0] == True:
            meta_file = open("meta-data.txt", 'w')
            meta_file.write("I reject")
            did_accept = "I reject"
            meta_file.close()

# define a main function
def main():
    global did_accept
    # initialize pygame modules
    pygame.init()
    pygame.font.init()

    # load and set the logo
    logo = pygame.image.load("hasse-800x700.png")
    pygame.display.set_icon(logo)

    # pictures used within the application
    home_picture = pygame.transform.scale(pygame.image.load("hasse-800x700.png"), (720, 680))
    back_picture = pygame.image.load("stars-background.jpg")
    bottle_picture = pygame.transform.scale(pygame.image.load("Hasseflarra.jpg"), (201, 241))
    om_oss_picture = pygame.image.load("om-oss.png")

    # set window title
    pygame.display.set_caption("Bryggeri Hemsida")

    # create fonts for text used in the program
    my_font = pygame.font.SysFont("comicsans", 30, 1)
    my_large_font = pygame.font.SysFont("comicsans", 100, 1)

    # create a main surface we can render objects on
    screen = pygame.display.set_mode((screen_width, screen_height))

    # get the size of our main surface and create a sub surface
    background = pygame.Surface(screen.get_size())

    # set previous sub surface to color black and fill the whole surface
    background = background.convert()

    # main variables for fullscreen / main app loop
    fullscreen = False
    running = True

    # used to limit FPS for the program
    clock = pygame.time.Clock()

    if os.path.exists("meta-data.txt"):
        f = open("meta-data.txt", "r+")
        did_accept = f.readline()
    else:
        f = open("meta-data.txt", 'w+')
        f.close()

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
        screen.blit(back_picture, (-290, aos_height - 720))

        # grab the mouse position for future use
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        # check if the cookie contains "I accept", "I reject"
        # if not run the age_restriction function
        if did_accept == 'I accept':
            input_system(screen, mouse_pos_x, mouse_pos_y)

            if draw_hem == True:
                screen.blit(home_picture, (190, aos_height - 690))
        
            draw_objects(screen, bottle_picture, om_oss_picture, mouse_pos_x, mouse_pos_y)
            draw_navbar(screen, my_font)

            # only run the hover animation on products
            # if no other page is being rendered (increased performance)
            if draw_produkter == True:
                if draw_om_oss == False:
                    if draw_kontakt == False:
                        if draw_hem == False:
                            hover_animation()
            
            # run the animation functions (AOS)
            aos()
            aos_side_slide()
        elif did_accept == 'I reject':
            quit()
        else:
            age_restriction(screen, my_font, my_large_font, mouse_pos_x, mouse_pos_y)

        # limit FPS (Frames per seconds)
        clock.tick(30)

        # update screen
        pygame.display.flip()
    

if __name__ == "__main__":
    main()