import pygame
import sys
from board import Board

pygame.init()

VALID_BOARD_SIZE = {4,9,16,25,36}

# Intro
print("")
while True:
    BOARD_SIZE = int(input("Give the size of the board: 4, 9, 16, 25, 36: "))
    if BOARD_SIZE not in VALID_BOARD_SIZE:
        print("This is not a valid size of the board!")
        print("")
    else:
        ans = input(f"You choose: {BOARD_SIZE}, is that correct? y/n:")
        print("")
        if ans == "y":
            break

print("You are ready to go now.")
print("You can fill positions by clicking on them and enter a number")
print("You can solve the board by pressing 's'")
print("You can clear the solved positions by pressing 'q'")
print("You can clear all position by pressing 'c'")
print("You can exit the program by pressing 'ESC'")
print("")

# Constants
MARGIN_TOP = 10
MARGIN_RIGHT = 10
MARGIN_BOT = 10
MARGIN_LEFT = 10
BOARD = Board(MARGIN_LEFT, MARGIN_TOP, BOARD_SIZE)
BOARD_WIDTH = BOARD.get_width()
WIDTH = MARGIN_LEFT + BOARD_WIDTH + MARGIN_RIGHT
HEIGHT = MARGIN_TOP + BOARD_WIDTH + MARGIN_BOT

# Pygame variables
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUDOKU SOLVER")
clock = pygame.time.Clock()

# Draw the window
def draw(win):
    win.fill((255,255,255))
    BOARD.draw(win)
    pygame.display.update()

# Mainloop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            if BOARD.sel_pos and not BOARD.solving:
                if event.key == pygame.K_KP0 or event.key == pygame.K_0:
                    BOARD.set_value_sel_block(0)
                if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                    BOARD.set_value_sel_block(1)
                if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                    BOARD.set_value_sel_block(2)
                if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                    BOARD.set_value_sel_block(3)
                if event.key == pygame.K_KP4 or event.key == pygame.K_4:
                    BOARD.set_value_sel_block(4)
                if event.key == pygame.K_KP5 or event.key == pygame.K_5:
                    BOARD.set_value_sel_block(5)
                if event.key == pygame.K_KP6 or event.key == pygame.K_6:
                    BOARD.set_value_sel_block(6)
                if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                    BOARD.set_value_sel_block(7)
                if event.key == pygame.K_KP8 or event.key == pygame.K_8:
                    BOARD.set_value_sel_block(8)
                if event.key == pygame.K_KP9 or event.key == pygame.K_9:
                    BOARD.set_value_sel_block(9)
            
            if event.key == pygame.K_s:
                BOARD.solving = not BOARD.solving
                if BOARD.solving:
                    BOARD.setup_solve()

            if event.key == pygame.K_a:
                BOARD.clear_solved()

            if event.key == pygame.K_c:
                BOARD.clear_all()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not BOARD.solving:
                BOARD.set_selected_position(pos)

    if BOARD.solving:
        BOARD.solve()

    draw(win)

# End program
pygame.quit()
quit()
sys.exit()