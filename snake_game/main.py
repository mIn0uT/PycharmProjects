from tkinter import *
import random

# constant variables
GAME_WIDTH = 1000
GAME_HEIGHT = 600
SPEED = 100  # the lower the faster
SPACE_SIZE = 50  # size of pixel (700/50 = 14 spaces)
BODY_PARTS = 3  # initial snake size
SNAKE_COLOR = "#00FFFF"  # blue green
FOOD_COLOR = "#FF0000"  # red
BACKGROUND_COLOR = "#000000"  # black

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        # nested lists for multiple boxes of snake body parts
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        # draw the snake and add a square for every coordinates
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        # set a random spawn points
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        # draw the food into the canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    # set the initial snake coordinate to 0
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    # change the snake coordinate based on direction
    snake.coordinates.insert(0, (x, y))
    # draw the snake into the canvas
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
    # add the squares of the snake
    snake.squares.insert(0, square)

    # alternate conditions: move the coordinates of the snake head to the other edge of the window
    # 16/09/2023: x<0 and y<0 only works as intended, other conditions has an offset 1
    if x < 0:
        snake.coordinates.insert(0, (GAME_WIDTH,y))
    elif x >= GAME_WIDTH:
        snake.coordinates.insert(0, (0,y))
    elif y < 0:
        snake.coordinates.insert(0, (x, GAME_HEIGHT))
    elif y >= GAME_HEIGHT:
        snake.coordinates.insert(0, (X, 0))
    # check if the head coordinate of snakes overlaps to last coordinates of the food
    # increment score and delete the food after
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        # delete the last coordinates of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    # check for collisions
    # if returned true the game is over
    if check_collisions(snake):
        game_over()
    else:
        # update the window every turn
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction  # old direction
    # set the new direction to old direction
    # disallow the new direction if it's the opposite of old direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]
    # check if the snake head overlaps the edges of the window then return true
    # if x < 0 or x >= GAME_WIDTH:
    #     return True
    # elif y < 0 or y >= GAME_HEIGHT:
    #     return True
    # check if the head index collides to any index of snake body parts
    for body_part in snake.coordinates[1:]:  # [1:] indicates any coordinates after the head index [0]
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")


""" Window Settings """
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'  # initial direction of snake object

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

"""Center the window every run"""
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# bind the arrow keys for change_direction function
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
