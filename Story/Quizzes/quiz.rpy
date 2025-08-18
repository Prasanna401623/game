label infinite_loop_quiz:
    # Skip if already completed
    if "infinite_loop" in completed_quizzes:
        return

    # Show the quiz background image (Your Canva design)
    scene bg_infinite_loop_quiz with fade

    # Display Harry to ask the question
    show harry at left
    harry "What do you think? Choose the correct answer below."

    # Call the custom screen to display buttons
    call screen infinite_loop_quiz_screen

    # After returning from the screen, check if we need to continue
    if "infinite_loop" not in completed_quizzes:
        jump infinite_loop_quiz
    return

init python:
    # Initialize score variables
    score = 0
    max_score = 0
    attempts = 0
    completed_quizzes = set()  # Track which quizzes have been completed
    current_question = 0  # Track question numbers across all branches

# Define styles for all quizzes
style quiz_frame:
    background Frame("gui/button/choice_idle_background.png", Borders(10, 10, 10, 10))
    xsize 300
    ysize 150
    padding (10, 10)

style quiz_text:
    size 24
    color "#00ffff"
    hover_color "#ffffff"
    text_align 0.5
    xalign 0.5
    yalign 0.5
    outlines [(2, "#000000", 0, 0)]

style quiz_question_text:
    size 40
    color "#00ffff"
    text_align 0.5
    xalign 0.5
    yalign 0.5
    outlines [(2, "#000000", 0, 0)]

style score_text:
    size 30
    color "#ffffff"
    text_align 1.0
    xalign 1.0
    yalign 0.0
    outlines [(2, "#000000", 0, 0)]

# Screen template for all quizzes
screen quiz_template(question, options, question_number):
    zorder 100  # Ensure this appears above other elements
    
    # Score display in top right
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -40
        yoffset 20
        background "gui/frame.png"
        padding (20, 20)
        
        vbox:
            spacing 10
            xsize 150
            
            text "Question [question_number]" size 25 xalign 0.5 color "#ffffff"
            
            frame:
                background Frame("gui/button/choice_idle_background.png", Borders(10, 10, 10, 10))
                padding (10, 10)
                
                vbox:
                    spacing 5
                    xalign 0.5
                    
                    text "Score" size 25 xalign 0.5 color "#ffffff"
                    text "[score]/[max_score]" size 35 xalign 0.5 color "#00ffff"
    
    # Question
    frame:
        background None
        xalign 0.5
        yalign 0.2
        text question style "quiz_question_text"
    
    # Options
    hbox:
        xalign 0.5
        yalign 0.7
        spacing 40
        
        for answer, action in options:
            frame style "quiz_frame":
                button:
                    action action
                    frame:
                        background None
                        padding (10, 10)
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            text answer style "quiz_text"

# Custom screen for infinite loop quiz
screen infinite_loop_quiz_screen():
    $ current_question = 1  # This is the first question
    use quiz_template(
        question="Question 1: What is the output of this code?",
        options=[
            ("It runs normally and stops after 5 iterations.", Jump("wrong_answer_infinite")),
            ("It will run forever.", Jump("correct_answer_infinite")),
            ("It won't run at all.", Jump("wrong_answer_infinite"))
        ],
        question_number=current_question
    )

# Correct Answer
label correct_answer_infinite:
    if "infinite_loop" not in completed_quizzes:
        $ score += 1
        $ max_score += 1
        $ completed_quizzes.add("infinite_loop")
        show harry at left
        harry "Good job! The condition never changes, so the loop runs forever."
        
        # Add short conversation
        hide harry
        show kendall at right
        kendall "That makes sense! So we need to be careful about our loop conditions."
        
        hide kendall
        show harry at left
        harry "Exactly! Now that you understand infinite loops, you're ready to tackle more complex programming challenges."
        
        hide harry
        show kendall at right
        kendall "I can't wait to learn more!"
    return

# Wrong Answer
label wrong_answer_infinite:
    if "infinite_loop" not in completed_quizzes:
        $ max_score += 1
        $ attempts += 1
        show harry at left
        harry "Not quite. Think about whether the loop condition is ever updated."

        if attempts >= 2:
            harry "Let me explain this concept again."
            $ attempts = 0
            jump infinite_loop_error
        else:
            menu:
                "Try again":
                    jump infinite_loop_quiz
                "Re-read about Infinite Loops":
                    jump infinite_loop_error
    return

