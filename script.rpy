# Define Characters
define h = Character('Harry', color="#6FA8DC")
define k = Character('Kendall', color="#F4B183")

# Background Image for the Maze Entrance
image bg_maze = im.Scale("maze.webp", config.screen_width, config.screen_height)

# Character Images
image harry = "harry.png"
image kendall = "kendall.png"

# Starting the game
label start:
    # Show the maze background
    scene bg_maze with fade
    
    # Show Kendall on screen
    show kendall at left

    # Kendall's dialogue
    k "Wow… This maze looks huge. How are we supposed to figure out which path is the right one?"
    
    # Show Harry on screen and hide Kendall
    hide kendall
    show harry at right
    
    # Harry's dialogue
    h "We’ll solve it with code. We’re going to use something called a loop."
    
    # Switch back to Kendall
    hide harry
    show kendall at left
    
    # Kendall's dialogue
    k "A loop? How’s that going to help us get out of here?"

    # Switch back to Harry
    hide kendall
    show harry at right
    
    # Harry explaining more
    h "A loop lets you repeat a set of actions until you find the solution."
    h "Specifically, a pre-test loop checks a condition first, and if it’s true, it keeps running."

    # Switch back to Kendall
    hide harry
    show kendall at left

    k "So, the loop will keep trying paths until one leads us to the exit?"

    # Switch to Harry
    hide kendall
    show harry at right
    
    h "Exactly! In our case, the loop will check if we’ve reached the exit after each path."
    
    label writing_loop:
    # Background remains the same maze with arrows
    scene bg_maze with dissolve
    
    # Show Kendall on screen at the left
    show kendall at left
    
    # Kendall's dialogue as she starts thinking about the loop
    k "Alright, let me write a loop that keeps checking the paths. If a path is wrong, the loop should move to the next one."

    # Display the virtual tablet Kendall is using to type
    show text "Kendall is typing on her tablet..." at truecenter with dissolve

    # Hide the text after a moment
    pause 1
    hide text

    # Show Harry on screen and hide Kendall
    hide kendall
    show harry at right
    
    # Harry explains the loop Kendall is writing
    h "Good thinking! We can use a pre-test loop for this. Let’s check each path until we find the exit."

    # Display the code snippet on the screen
    show text "while (path != exit):\n    check_next_path()" at truecenter with dissolve

    # Wait for the player to read it
    pause 3

    # Show Kendall again, and hide Harry
    hide harry
    show kendall at left
    
    k "It’s working! The loop is checking each path, but we keep hitting dead ends."

    # Harry reappears
    hide kendall
    show harry at right

    h "That’s how loops work. They keep running until the condition is met."

    # Final dialogue to transition
    h "Keep going! We’re bound to find the right path."

