#
# File: assign2_part2.py
# Author: Daniel Arbon
# SAIBT ID: arbdtd1502
# Description: Assignment 2 - Part 2 (Snake Game).
# This is my own work as defined by the University's Academic Misconduct Policy.

# LIBRARIES #
# Import the required libraries.
import graphics
import game
import random
import time
import math

# CONSTANTS #
# Width and height of the window
WIN_WIDTH = 600
WIN_HEIGHT = 600

# Size of the blocks.
BLOCK_SIZE = 25

# Distance for movement.
MOVE_DISTANCE = 25

# GLOBAL VARIABLES #
theSnake = [] # Store the elements of the snake.
direction = "" # Store the direction of snake's movement.
playing = False # Is the game in play or halted?

# FUNCTIONS #

# Function to contain the actual game.
def playSnakeGame():

    foodEaten = 0 # Count the food items eaten by the snake.
    # Bring in global variables.
    global theSnake # To store snake itself.
    global playing # To store game state.
       
    # Set up score displays at start of game. 
    gameScore = 0 # Set score at start of game.
    snakeLength = 2 # set length score at start of game.
    scoreText = "Score: " + str(gameScore) # How to display the score.
    scoreDisplay.setText(scoreText)
    lengthText = "Length: "+ str(snakeLength) # How to display the length.
    lengthDisplay.setText(lengthText)
    
    # Create the initial food block object.
    foodX = random.randint(BLOCK_SIZE,WIN_WIDTH-BLOCK_SIZE)
    foodY = random.randint(BLOCK_SIZE,WIN_HEIGHT-BLOCK_SIZE)
    food = game.GameBlock(foodX, foodY, BLOCK_SIZE, BLOCK_SIZE, "red", "apple.gif", None, 0)
    # Draw the initial food block to the screen.
    food.draw(win)

    # Create the head object for the snake.
    snakeHead = game.GameBlock(WIN_WIDTH/2, WIN_HEIGHT/2, BLOCK_SIZE, BLOCK_SIZE, "green", None, None, 0)
    snakeHead.draw(win)
    # Add snakeHead object to theSnake.
    theSnake.append(snakeHead)

    # Create the initial body object of the snake.
    snakeBody = game.GameBlock(WIN_WIDTH/2, WIN_HEIGHT/2, BLOCK_SIZE, BLOCK_SIZE, "blue", None, None, 0)
    snakeBody.draw(win)
    # Add the snakeBody object to theSnake.
    theSnake.append(snakeBody)

    # Set the initial speed for the snake's movement.
    speed = 0.2

    playing = True # Once set up, play the game until 'game over' condition met.

    # Loop the game while 'playing' is 'True'.
    while playing == True:

        # Move the body of the snake.
        for block in range(len(theSnake)-1,0,-1): # Move each part of the snake to the old position of the segment before.
            moveX = theSnake[block-1].getCentreX() - theSnake[block].getCentreX()
            moveY = theSnake[block-1].getCentreY() - theSnake[block].getCentreY()
            theSnake[block].move(moveX, moveY)

        # Move the snakeHead as directed by user.
        if direction == "Left": # LEFT
            theSnake[0].move(-MOVE_DISTANCE, 0)
        elif direction == "Right": # RIGHT
            theSnake[0].move(MOVE_DISTANCE, 0)
        elif direction == "Up": # UP
            theSnake[0].move(0,-MOVE_DISTANCE)
        elif direction == "Down": # DOWN
            theSnake[0].move(0, MOVE_DISTANCE)

        # Use collide() function to check if the snake has 'eaten' food.
        if collide(theSnake[0],food) == True:
            # Create a new body piece at the tail-end of the snake.
            newSnakeBody = game.GameBlock(theSnake[-1].getCentreX(), theSnake[-1].getCentreY(), BLOCK_SIZE, BLOCK_SIZE, "blue", None, None, 0)
            newSnakeBody.draw(win)
            theSnake.append(newSnakeBody) # Add the new segment to the snake.
            snakeLength = len(theSnake)
            lengthText = "Length: " + str(snakeLength)
            lengthDisplay.setText(lengthText) # Update the length score display.
            
            food.undraw() # Remove 'eaten' food object.
            foodEaten += 1 # Increment the 'Food Eaten' counter.

            gameScore = gameScore + 20 # Increment the score when snake eats food.
            scoreText = "Score: " + str(gameScore)
            scoreDisplay.setText(scoreText) # Update the score text display.
            
            # Create a new food object.
            foodX = random.randint(BLOCK_SIZE,WIN_WIDTH-BLOCK_SIZE)
            foodY = random.randint(BLOCK_SIZE,WIN_HEIGHT-BLOCK_SIZE)
            food = game.GameBlock(foodX, foodY, BLOCK_SIZE, BLOCK_SIZE, "red", "apple.gif", None, 0)
            food.draw(win)
            if foodEaten % 5 == 0 and speed > 0.05: # Every fifth food eaten (i.e. foodEaten is a multiple of 5), reduce the delay on the snake's speed to a lowest speed of 0.05.
                speed -= 0.03

        # Create game over message for fail conditions.
        gameoverText = "Game Over! Press 's' to start again" # Message to display if "Game Over" condition is met.

        # Check if the snake goes out of bounds.
        leftPos = theSnake[0].getCentreX() - (BLOCK_SIZE/2) # The left edge of the snake's head.
        rightPos = theSnake[0].getCentreX() + (BLOCK_SIZE/2) # The right edge of the snake's head.
        upPos = theSnake[0].getCentreY() - (BLOCK_SIZE/2) # The top edge of the snake's head.
        downPos = theSnake[0].getCentreY() + (BLOCK_SIZE/2) # The bottom edge of the snake's head.

        if (leftPos < 0) or (rightPos > WIN_WIDTH) or (upPos < 0) or (downPos > WIN_HEIGHT): # Is the snake's position outside the edges of the window?
            endGameMsg.setText(gameoverText) # IF yes: display 'Game Over'.
            food.undraw() # Remove food from play.
            for item in theSnake: # Remove the entire snake from play.
                item.undraw()
            playing = False # Halt the game.

        # Check if the head of the snake touches any part other than the first body piece.
        for bodypart in range(len(theSnake)-1,1,-1):
            hitSelf = collide(theSnake[0],theSnake[bodypart])
            if hitSelf:
                endGameMsg.setText(gameoverText) # IF yes: Display 'game over' message.
                food.undraw() # Remove food from play.
                for item in theSnake: # Remove the entire snake from play.
                    item.undraw()
                playing = False # Halt the game.

        # Use the 'speed' value to set a delay on the snake's speed.
        time.sleep(speed)

# Function to handle user's key input.
def handleKeys(event):
    # Set up variables.
    global direction
    global theSnake
    prevDirection = "" # Store current direction for comparison with new input.

    # Update snake direction.
    # Prevent movement in opposite directions.
    if event.keysym == "Left":
        prevDirection = direction
        if prevDirection != "Right": # Go left UNLESS already going right.
            direction = "Left"
    elif event.keysym == "Right":
        prevDirection = direction
        if prevDirection != "Left": # Go right UNLESS already going left.
            direction = "Right"
    elif event.keysym == "Up":
        prevDirection = direction
        if prevDirection != "Down": # Go up UNLESS already going down.
            direction = "Up"
    elif event.keysym == "Down":
        prevDirection = direction
        if prevDirection != "Up": # Go down UNLESS already going up.
            direction = "Down"
    # Set a keypress to reset game.
    elif event.keysym == "s" and playing == False: # Only works if game has been halted.
        endGameMsg.setText(" ") # Blank the GAME OVER message to make it go away.
        theSnake = [] # Reset the snake holder list to empty.
        direction = "" # Reset directional input to none.
        playSnakeGame() # Start a new game of Snake.
    #Set a keypress to quit game.
    elif event.keysym == "q":
        win.close() # Close the window.
        exit() # End the program entirely.

# Function to detect collision between blocks.
def collide(block1,block2):
    distance = math.sqrt(((block2.getCentreX() - block1.getCentreX())**2) + ((block2.getCentreY()-block1.getCentreY())**2))
    if distance < BLOCK_SIZE: # If the blocks overlap, there is a collision.
        return True
    else:
        return False

# MAIN PROGRAM #

# Create the graphics window for the snake game.
win = graphics.GraphWin("Snake", WIN_WIDTH, WIN_HEIGHT)

# Set the window background to black.
win.setBackground("black")

# Display the Score.
scoreDisplay = graphics.Text(graphics.Point(75,20), " ")
scoreDisplay.setTextColor("white")
scoreDisplay.setFace("arial")
scoreDisplay.setSize(16)
scoreDisplay.draw(win)

# Display the Snake Length.
lengthDisplay = graphics.Text(graphics.Point(515,20), " ")
lengthDisplay.setTextColor("white")
lengthDisplay.setFace("arial")
lengthDisplay.setSize(14)
lengthDisplay.draw(win)

# Display Game Over message.
endGameMsg = graphics.Text(graphics.Point(300,300), " ")
endGameMsg.setTextColor("green")
endGameMsg.setFace("arial")
endGameMsg.setSize(18)
endGameMsg.draw(win)

# Wait for Key Entry events.
win.bind_all("<Key>", handleKeys)

# Begin a game of Snake.
playSnakeGame()

# Wait for Main Loop events.
win.mainloop()

# Close the window.
win.getMouse()
win.close()
