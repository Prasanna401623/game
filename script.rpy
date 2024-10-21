# Define Characters
define h = Character('Harry', color="#6FA8DC")
define k = Character('Kendall', color="#F4B183")

# Background Image for the Maze Entrance
image bg_maze = "maze_background_start.jpg"  # Replace with your maze image file

# Starting the game
label start:
    # Show the maze background
    scene bg_maze with fade
    
    # Dialogue for Scene 1
    k "Wow… This maze looks huge. How are we supposed to figure out which path is the right one?"
    h "We’ll solve it with code. We’re going to use something called a loop."
    k "A loop? How’s that going to help us get out of here?"
    h "A loop lets you repeat a set of actions until you find the solution."
    h "Specifically, a pre-test loop checks a condition first, and if it’s true, it keeps running."
    k "So, the loop will keep trying paths until one leads us to the exit?"
    h "Exactly! In our case, the loop will check if we’ve reached the exit after each path."

    # Jump to the next scene (writing the loop)
    jump writing_loop
