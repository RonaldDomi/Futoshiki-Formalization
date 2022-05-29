import pygame
import tkinter as tk
from tkinter import filedialog
import z3

root = tk.Tk()
root.withdraw()

cell_width = 90
cell_color_fill = cell_width - 20


def show_button(screen, x, y, button_width, button_height,  button_color, text_font, text, text_size, text_color):
    """
        just complete the arguments, it makes sense\n
        also blits the text to screen
    """
    font = pygame.font.SysFont(text_font, text_size)
    text = font.render(text, True, text_color)
    pygame.draw.rect(screen, button_color, [x, y, button_width, button_height])
    screen.blit(text, (x + 5, y + button_height/3))

def is_button_pressed(events, btn_x, btn_y, btn_width, btn_height):
    """
        if the user presses the button, return True
    """
    coords = pygame.mouse.get_pos()
    if coords[0] > btn_x and coords[0] < btn_x + btn_width \
            and coords[1] > btn_y and coords[1] < btn_y + btn_height:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
    return False

def draw_buttons(screen, button_width, button_height, button_font, button_color, text_color, button_size):
    """
        draws all the buttons at once\n
        returs the [[button1_x, button1_y], ...] for all the buttons we have created
    """
    # ----------- BUTTON 1
    button1_x = 20
    button1_y = 50
    show_button(screen, button1_x, button1_y, button_width,
                button_height, button_color, button_font, 'Solve', button_size, text_color)

    # ----------- BUTTON 2
    button2_x = 140
    button2_y = 50
    show_button(screen, button2_x, button2_y, button_width,
                button_height, button_color, button_font, 'Import', button_size, text_color)

    # ----------- BUTTON 3
    button3_x = 260
    button3_y = 50
    # show_button(screen, button3_x, button3_y, button_width,
    #             button_height, button_color, button_font, 'Button 3', button_size, text_color)

    # ----------- BUTTON 4
    button4_x = 380
    button4_y = 50
    # show_button(screen, button4_x, button4_y, button_width,
    #             button_height, button_color, button_font, 'Button4', button_size, text_color)

    return [[button1_x, button1_y], [button2_x, button2_y], [button3_x, button3_y], [button4_x, button4_y]]

def draw_config_board(screen, table_dimmensions, cell_color, cell_name_color, configuration, base_table_x, base_table_y):
    """
        draws the cells, with their respective colors\n
        adds the name of the bonus above, if it has one \n
        and blits the cells. configuration serves for the data
    """

    # draws the numbers of configuration and cell colors
    for rowIndex in range(table_dimmensions):
        for columnIndex in range(table_dimmensions):
            font = pygame.font.SysFont(None, 30)
            cell_name = ''
            for number in configuration["numbers"]:
                if(number["coords_x"] == columnIndex and number["coords_y"] == rowIndex):
                    cell_name = str(number['value'])


            cell = pygame.Rect(base_table_x + cell_width * columnIndex,
                               base_table_y + cell_width * rowIndex, 
                               cell_color_fill, cell_color_fill)

            pygame.draw.rect(screen, cell_color, cell)

            img = font.render(cell_name, True, cell_name_color)
            x = base_table_x + int(cell_width * columnIndex + cell_width / 5)
            y = base_table_y + int(cell_width * rowIndex + cell_width / 3)
            screen.blit(img, (x+11, y-3))

    # draws the arrows of configuration
    for arrow in configuration["arrows"]:
        coords = f"{arrow['coords_y']}-{arrow['coords_x']}"
        draw_single_arrow(screen, coords, arrow["direction"], base_table_x, base_table_y)

def draw_single_arrow(screen, start_cell, direction, base_table_x, base_table_y):
    """ 
        start_cell is row-column  as indexes\n
        direction is up/down/left/right
    """
    cell_row = int(start_cell.split("-")[0])
    cell_column = int(start_cell.split("-")[1])

    str_x = base_table_x + (cell_column)*cell_width
    str_y = base_table_y + (cell_row)*cell_width
    
    arrow = pygame.image.load("./pixil-frame-0.png")
    arrow_padding_x = 10
    arrow_padding_y = 15
    if direction == 'up':
        arrow_top_left = str_y - (cell_width - cell_color_fill)

        screen.blit(arrow, (str_x + arrow_padding_x, arrow_top_left+1))
    elif direction == 'down':
        arrow_top_left = str_y + cell_color_fill

        arrow = pygame.transform.rotate(arrow, 180)
        screen.blit(arrow, (str_x + arrow_padding_x, arrow_top_left+1))
    elif direction == 'left':
        arrow_top_left = str_x - (cell_width - cell_color_fill)
        arrow = pygame.transform.rotate(arrow, 90)
        screen.blit(arrow, (arrow_top_left+2, str_y + arrow_padding_y))
    else:
        # get end cell top left corner
        arrow_top_left = str_x + cell_color_fill
        arrow = pygame.transform.rotate(arrow, 270)
        screen.blit(arrow, (arrow_top_left+2, str_y + arrow_padding_y))

def text_to_configuration(file):
    f = open(file, "r")
    lines = f.read().split('\n')
    n = int(lines[0])
    lines = lines[2:]
    arrow_lines = []
    number_lines = []
    config_board = {
        "numbers": [],
        "arrows": [],
        "table_dimmensions": n
    }
    for i in range(len(lines)):
        if i%2==1:
            arrow_lines.append(lines[i])
        else:
            number_lines.append(lines[i])

    # adding arrows between lines
    for arrow_line_i in range(len(arrow_lines)):
        items = arrow_lines[arrow_line_i].split(' ')
        # clean empty spaces
        items = [x for x in items if x]
        
        for item_i in range(len(items)):
            item = items[item_i]
            if item == '^':
                arr_object = {
                    "coords_x": item_i, 
                    "coords_y": arrow_line_i+1, 
                    "direction": "up"
                }
                config_board["arrows"].append(arr_object)
            elif item == 'v':
                arr_object = {
                    "coords_x": item_i, 
                    "coords_y": arrow_line_i, 
                    "direction": "down"
                }
                config_board["arrows"].append(arr_object)

    # adding numbers and arrows between numbers
    for number_line_i in range(len(number_lines)):
        items = number_lines[number_line_i].split(' ')
        counter_number = -1
        for item_d in range(len(items)):
            item = items[item_d]
            if len(item) > 1 and item[0] == '-':
                item = '0'
            if item == '0' or item.isnumeric():
                if(int(item) > n): 
                    item = str(n)
                counter_number += 1
                # add number
                num_object = {
                    "coords_x": counter_number, 
                    "coords_y": number_line_i, 
                    "value": int(item) 
                }
                config_board["numbers"].append(num_object)
            else:
                if item == '<':
                    arr_object = {
                        "coords_x": counter_number+1, 
                        "coords_y": number_line_i, 
                        "direction": "left"
                    }
                    config_board["arrows"].append(arr_object)
                elif item == '>':
                    # add sign
                    arr_object = {
                        "coords_x": counter_number, 
                        "coords_y": number_line_i, 
                        "direction": "right"
                    }
                    config_board["arrows"].append(arr_object)
                
           
    return config_board

# def no_model(screen):
#     font = pygame.font.SysFont("Arial", 20)
#     text = font.render("No Model Found", True, [255, 255, 255])
#     screen.blit(text, (260, 50))

# def yes_model(screen):
#     font = pygame.font.SysFont("Arial", 20)
#     text = font.render("Model Found", True, [255, 255, 255])
#     screen.blit(text, (260, 50))

def solve(screen, board_config, input_file):
    # input_file with .txt 
    output_solved = input_file.replace(".txt", "_solved.txt")
    output_dimacs = 'conf_1.dimacs'
    create_dimacs(board_config, output_dimacs)
    solved_config = model_to_configuration("./Dimacs/" +output_dimacs)
    if solved_config == "Error":
        # no_model(screen)
        return board_config
    else:
        # yes_model(screen)
        solved_config["arrows"] = board_config["arrows"]
        solved_config["table_dimmensions"] = board_config["table_dimmensions"]
        export_file(output_solved, solved_config) 
        # save the solution file somewhere
    return solved_config

def export_file(file, conf):
    print("to open: ", file)
    f = open(file, 'w')
    f.write(str(conf["table_dimmensions"]) + '\n\n')
    y_index = 0
    for line_number in range(conf["table_dimmensions"]*2-1):
        if(line_number % 2 == 0):
            #numbers line 
            for x_index in range(conf["table_dimmensions"]):
                printed=False
                for conf_number in conf["numbers"]:
                    if(conf_number["coords_x"] == x_index and conf_number["coords_y"] == y_index):
                        # write a number
                        # print(conf_number)
                        f.write(str(conf_number['value']) + ' ')
                        printed=True
                if not printed:
                    f.write('0 ')
                if x_index != conf['table_dimmensions'] - 1:
                    printed=False
                    for conf_arrow in conf["arrows"]:
                        if(conf_arrow["coords_x"] == x_index and conf_arrow["coords_y"] == y_index and conf_arrow['direction']=="right"):
                            # write a number
                            # print(conf_arrow)
                            f.write('> ')
                            printed=True
                        elif(conf_arrow["coords_x"] == x_index+1 and conf_arrow["coords_y"] == y_index and conf_arrow['direction']=="left"):
                            # print('writing 0')
                            f.write('< ')
                            printed=True
                    if not printed:
                        f.write('| ')
        else:
            #arrows line
            for x_index in range(conf["table_dimmensions"]):
                printed=False
                for conf_arrow in conf['arrows']:
                    if conf_arrow['coords_x'] == x_index and conf_arrow['coords_y'] == y_index and conf_arrow['direction']=="down":
                        f.write("v") if  x_index==0 else f.write("   v")
                        printed=True
                    elif conf_arrow['coords_x'] == x_index and conf_arrow['coords_y'] == y_index+1 and conf_arrow['direction']=="up":
                        f.write("^") if  x_index==0 else f.write("   ^")
                        printed=True
                if not printed:
                    f.write("-") if  x_index==0 else f.write("   -")
                    
            y_index += 1
        f.write("\n")

def import_file():
    file_path = filedialog.askopenfilename()
    return file_path

def create_dimacs(board_config, output_file):

    f = open('./Dimacs/' + output_file, 'w')
    n = board_config["table_dimmensions"]
    
    # each number at least once per ligne
    print("c each number at least once per lingne", file=f)
    for number in range(n):
        for line in range(n):
            for column in range(n):
                var_name = create_name(number+1, line, column)
                print(var_name, end=' ', file=f)
            print(" 0", file = f)
    
    # each number at least once per column
    print("c each number at least once per column", file=f)
    for number in range(n):
        for line in range(n):
            for column in range(n):
                var_name = create_name(number+1, column, line)
                print(var_name, end=' ', file=f)
            print(" 0", file = f)
    
    # not more than same number once in each line
    print("c not more than same number in each line", file=f)
    for number in range(n):
        for line in range(n):
            for column in range(n-1):
                for col2 in range(column+1, n):
                    var_name1 = '-' + create_name(number+1, line, column)
                    var_name2 = '-' + create_name(number+1, line, col2)
                    print(var_name1, ' ', var_name2, end=' ', file=f)   
                    print(" 0", file=f)

    # not more than same number in each column
    print("c not more than same number in each column", file=f)
    for number in range(n):
        for line in range(n-1):
            for column in range(n):
                for line2 in range(line+1, n):
                    var_name1 = '-' + create_name(number+1, line, column)
                    var_name2 = '-' + create_name(number+1, line2, column)
                    print(var_name1, ' ', var_name2, end=' ', file=f)   
                    print(" 0", file=f)

   
    # not more than one number per cell
    print("c not more than one number per cell", file=f)
    for number1 in range(n):
        for line in range(n):
            for column in range(n):
                for number2 in range(number1+1, n):
                    var1_name = '-' + create_name(number1+1, line, column)
                    var2_name = '-' + create_name(number2+1, line, column)
                    print(var1_name, ' ', var2_name, end=' ', file=f)   
                    print(" 0", file=f)
    
    # adding data numbers
    print("c numbers", file=f)
    for number_object in board_config["numbers"]:
        name = str(number_object['value']) + \
                str(number_object['coords_y']) + str(number_object['coords_x'])
        if(number_object['value'] != 0):
            print(name + ' 0', file=f)
    
    # adding data arrows
    print("c arrows", file=f)
    for arrow_object in board_config["arrows"]:
        for sup_number in range(2, board_config["table_dimmensions"]+1): 
            for inf_number in range(1, sup_number):
                name_low = str(inf_number) + str(arrow_object["coords_y"]) + str(arrow_object["coords_x"])
                # print("-" + name_low)
                name_high = ""

                if(arrow_object["direction"] == 'up'):
                    name_high = str(sup_number) + str(arrow_object['coords_y']-1) + str(arrow_object['coords_x'])
                elif(arrow_object["direction"] == 'down'):
                    name_high = str(sup_number) + str(arrow_object['coords_y']+1) + str(arrow_object['coords_x'])
                elif(arrow_object["direction"] == 'right'):
                    name_high = str(sup_number) + str(arrow_object['coords_y']) + str(arrow_object['coords_x']+1)
                elif(arrow_object["direction"] == 'left'):
                    name_high = str(sup_number) + str(arrow_object['coords_y']) + str(arrow_object['coords_x']-1)
                print('-' + name_high, ' -' + name_low, ' 0', file=f)



def create_name(number, line, column):
    str_created = str(number) + str(line) + str(column)
    return str_created

def model_to_configuration(file):
    # print(file)
    s = z3.Solver()
    s.from_file(file)
    # print(s.check())
    if (str(s.check()) == "sat"):
        model=s.model()
        solList=[]
        for i in model:
            solList.append(model[i])

        for i in range(0,len(solList)):
            solList[i]=((int(str(model[i]).replace('k','').replace('!',''))),solList[i])
    else:
        print('no model')
        return "Error"

    config_board = {
        "numbers": [],
        "arrows": [],
        "table_dimmensions": 0
    }
    for variable, value in solList:
        if value:
            config_board["numbers"].append({
                    "coords_x": int(str(variable)[2]), 
                    "coords_y": int(str(variable)[1]), 
                    "value": int(str(variable)[0]) 
            })

    # print(config_board)
    return config_board

# solved_config = model_to_configuration("./Dimacs/conf_1.dimacs")

# model_to_configuration("./Dimacs/conf_1.dimacs")
# board_config = text_to_configuration("./configurations/conf_1.txt")
# create_dimacs(board_config, ".conf_2_output.txt")

# model_to_configuration('./Dimacs/conf_1.dimacs')