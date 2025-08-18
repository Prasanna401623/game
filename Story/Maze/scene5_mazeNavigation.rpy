# Screen for the maze navigation quiz
# screen maze_navigation_quiz():
#     modal True
    
#     # Code snippet image
#     # Question 1: Code shows a basic maze navigation sequence that needs completion
#     # Example:
#     # def navigate_maze():
#     #     move_forward()
#     #     ___
#     #     move_forward()
#     add "maze_navigation_image" xalign 0.5 yalign 0.3
    
#     $ current_question = 1  # This is the first question in the sequence
#     use quiz_template(
#         question="Question 1: What command should come next?",
#         options=[
#             ("turn_right()", Return("correct")),
#             ("turn_left()", Return("wrong")),
#             ("move_backward()", Return("wrong"))
#         ],
#         question_number=current_question
#     )

# Initialize score at the start of the maze section
label start_maze_section:
    $ score = 0
    $ max_score = 3  # Total number of questions across all maze challenges
    
    # Show the score display in the top-right corner
    show screen score_display
    
    jump maze_navigation_start

# Score display screen (persistent through maze challenges)
screen score_display():
    zorder 90  # High enough to be visible but below final score display
    add circle:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        xsize 100
        ysize 100
    
    vbox:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        xsize 100
        ysize 100
        spacing 5
        
        text "Score" size 20 xalign 0.5 color "#ffffff"
        hbox:
            xalign 0.5
            spacing 5
            text "[score]" size 25 color "#00ffff" outlines [(2, "#000000", 0, 0)]
            text "/" size 20 color "#ffffff"
            text "[max_score]" size 25 color "#00ffff" outlines [(2, "#000000", 0, 0)] 