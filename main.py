import pygame, os
from screen_utils import *
# from process import Inputs

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption("Hello World")
pygame.init()

colors = {
    'black': [0, 0, 0],
    'white': [255, 255, 255],
    'dark_grey': [69, 72, 74],
    'light_gray': [108, 112, 117],
    'darkest_green': [61, 119, 123],
    'dark_green': [91, 167, 174],
    'green': [118, 183, 188],
    'light_green': [159, 205, 208],
}

ScreenWidth, ScreenHeight = 900, 600
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
screen.fill((69, 72, 74)) # dark_grey

buttons_background_border = 150
gameloop = True

button_width = 100
button_height = 40
button_font = "Arial"

pygame.draw.rect(screen, [0,0,0], [0, 0, ScreenWidth, buttons_background_border]) #buttons background
buttons_coords = draw_buttons(screen, button_width, button_height, button_font, 
                                colors['darkest_green'], colors['black'], 18)
button1_x, button1_y = buttons_coords[0][0], buttons_coords[0][1]
button2_x, button2_y = buttons_coords[1][0], buttons_coords[1][1]
# button3_x, button3_y = buttons_coords[2][0], buttons_coords[2][1]
# button4_x, button4_y = buttons_coords[3][0], buttons_coords[3][1]

base_starting_table_x = 100
base_starting_table_y = 200

base_solved_table_x = 500
base_solved_table_y = 200
board_config = None
current_file = None

pygame.display.flip()

while gameloop:
    events = pygame.event.get()

    # SOLVE BUTTON
    if is_button_pressed(events, button1_x, button1_y, button_width, button_height):
        if(board_config != None):
            solved_config = solve(screen, board_config, current_file)
            if(solved_config["table_dimmensions"] > 4):
                base_solved_table_x += (solved_config["table_dimmensions"] - 4) * 100
            draw_config_board(screen, board_config["table_dimmensions"], 
                        colors['light_gray'], colors['white'], 
                        solved_config, base_solved_table_x, base_solved_table_y)
            
            pygame.display.flip()
    # IMPORT BUTTON
    elif is_button_pressed(events, button2_x, button2_y, button_width, button_height):     
        #clear the screen
        pygame.draw.rect(screen, [69, 72, 74], [0, buttons_background_border, ScreenWidth, ScreenHeight-buttons_background_border]) #buttons background

        current_file = import_file()
        board_config = text_to_configuration(current_file)
        draw_config_board(screen, board_config["table_dimmensions"], 
                    colors['light_gray'], colors['white'], 
                    board_config, base_starting_table_x, base_starting_table_y)
   
        pygame.display.flip()
    # elif is_button_pressed(events, button3_x, button3_y, button_width, button_height):
    #     print("Button3 is pressed")
    # elif is_button_pressed(events, button4_x, button4_y, button_width, button_height):
    #     print("Button4 is pressed")
    # Inputs
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            gameloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                gameloop = False