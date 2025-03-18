label infinite_loop_quiz:
    # Show the quiz background image (Your Canva design)
    scene bg_infinite_loop_quiz with fade

    # Display Harry to ask the question
    show harry at left
    harry "What do you think? Choose the correct answer below."

    # Call the custom screen to display buttons
    call screen infinite_loop_quiz_screen

    return  # Ends the quiz when an option is chosen

# Custom screen for button placement
screen infinite_loop_quiz_screen():
    vbox:
        xpos 0.5  # Center the buttons horizontally
        ypos 0.75  # Position the buttons lower on the screen
        anchor (0.5, 0.5)  # Ensure proper alignment
        spacing 20  # Adds space between buttons

        # Answer Buttons
        textbutton "It runs normally and stops after 5 iterations." action Jump("wrong_answer_infinite") style "quiz_button"
        textbutton "It will run forever." action Jump("correct_answer_infinite") style "quiz_button"
        textbutton "It won’t run at all." action Jump("wrong_answer_infinite") style "quiz_button"

# Correct Answer
label correct_answer_infinite:
    show harry at left
    harry "Good job! The condition never changes, so the loop runs forever."

    menu:
        "Continue to next quiz":
            jump next_quiz_or_maze  # Jump to the next quiz or challenge

# Wrong Answer
label wrong_answer_infinite:
    show harry at left
    harry "Not quite. Think about whether the loop condition is ever updated."

    menu:
        "Try again":
            jump infinite_loop_quiz
        "Re-read about Infinite Loops":
            jump infinite_loop_error  # Goes back to error explanation

