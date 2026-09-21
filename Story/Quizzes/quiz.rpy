# ============================================================
# QUIZ ORCHESTRATOR - Runs all 4 quizzes in sequence
# ============================================================
label all_quizzes:
    # Reset attempts for fresh start
    $ attempts = 0
    
    # Introduction
    scene bg_maze_interior with fade
    show harry at left
    harry "Great work learning about all those errors! Now let's see how well you understood them."
    
    hide harry
    show kendall at right
    kendall "Quiz time? I think I'm ready!"
    
    hide kendall
    show harry at left
    harry "You'll answer 4 questions, one for each error type we covered. Let's begin!"
    hide harry
    
    # Run all 4 quizzes in sequence
    call infinite_loop_quiz from _call_infinite_loop_quiz
    call logic_error_quiz from _call_logic_error_quiz
    call off_by_one_quiz from _call_off_by_one_quiz
    call pre_test_logic_quiz from _call_pre_test_logic_quiz
    
    # All quizzes completed - show final score
    scene bg_maze_interior with fade
    show harry at left
    harry "You've completed all the quizzes! Let me show you your final score."
    hide harry
    
    # Show final score
    show screen final_score_display
    with dissolve
    pause 3.0
    hide screen final_score_display
    with dissolve
    
    return


# ============================================================
# QUIZ 1: INFINITE LOOP
# ============================================================
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
    missed_questions = set()  # Questions missed at least once; they score 0
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

# Final score display screen
screen final_score_display():
    zorder 100  # Ensure this appears above other elements
    frame:
        background Frame("gui/button/choice_idle_background.png", Borders(10, 10, 10, 10))
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 300
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text "Final Score" size 50 xalign 0.5 color "#ffffff"
            
            frame:
                background Frame("gui/button/choice_idle_background.png", Borders(10, 10, 10, 10))
                padding (20, 20)
                
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 10
                    
                    text "[score]" size 60 xalign 0.5 color "#00ffff" outlines [(2, "#000000", 0, 0)]
                    text "out of" size 25 xalign 0.5 color "#ffffff"
                    text "[max_score]" size 40 xalign 0.5 color "#00ffff" outlines [(2, "#000000", 0, 0)]
            
            $ percentage = (score * 100) // max_score if max_score > 0 else 0
            if percentage == 100:
                text "Perfect Score!" size 30 xalign 0.5 color "#00ffff"
            elif percentage >= 70:
                text "Great Job!" size 30 xalign 0.5 color "#00ffff"
            else:
                text "Keep Practicing!" size 30 xalign 0.5 color "#00ffff"

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

# Screen template for maze challenges (separate from quizzes)
screen challenge_template(question, options, challenge_number):
    zorder 100  # Ensure this appears above other elements
    
    # Challenge progress display in top right
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
            
            text "Challenge [challenge_number]" size 25 xalign 0.5 color "#00ff00"
            
            frame:
                background Frame("gui/button/choice_idle_background.png", Borders(10, 10, 10, 10))
                padding (10, 10)
                
                vbox:
                    spacing 5
                    xalign 0.5
                    
                    text "Quiz Score" size 20 xalign 0.5 color "#ffffff"
                    text "[score]/[max_score]" size 30 xalign 0.5 color "#00ffff"
    
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
        $ max_score += 1
        if "infinite_loop" not in missed_questions:
            $ score += 1
        $ completed_quizzes.add("infinite_loop")
        show harry at left
        harry "Good job! The condition never changes, so the loop runs forever."
        
        # Add short conversation
        hide harry
        show kendall at right
        kendall "That makes sense! So we need to be careful about our loop conditions."
        
        hide kendall
        show harry at left
        harry "That's the idea. Now you know how to spot infinite loops."
        
        hide harry
        show kendall at right
        kendall "I can't wait to learn more!"
    return

# Wrong Answer
label wrong_answer_infinite:
    if "infinite_loop" not in completed_quizzes:
        $ missed_questions.add("infinite_loop")
        $ attempts += 1
        show harry at left
        harry "Not quite. Think about whether the loop condition is ever updated."

        if attempts >= 2:
            harry "Let me explain this concept again."
            $ attempts = 0
            call infinite_loop_error from _call_infinite_loop_error_1
            jump infinite_loop_quiz
        else:
            menu:
                "Try again":
                    jump infinite_loop_quiz
                "Re-read about Infinite Loops":
                    call infinite_loop_error from _call_infinite_loop_error_2
                    jump infinite_loop_quiz
    return


# ============================================================
# QUIZ 2: LOGIC ERROR
# ============================================================
label logic_error_quiz:
    # Skip if already completed
    if "logic_error" in completed_quizzes:
        return

    # Show the quiz background image
    scene bg_logic_error_quiz with fade

    # Display Harry to ask the question
    show harry at left
    harry "Here's a tricky one about logic errors. What do you think will happen?"

    # Call the custom screen to display buttons
    call screen logic_error_quiz_screen

    # After returning from the screen, check if we need to continue
    if "logic_error" not in completed_quizzes:
        jump logic_error_quiz
    return

# Custom screen for logic error quiz
screen logic_error_quiz_screen():
    $ current_question = 2  # This is the second question
    use quiz_template(
        question="Question 2: What happens when you run this code?",
        options=[
            ("It never prints anything.", Jump("correct_answer_logic")),
            ("It prints 'Found it!' 5 times.", Jump("wrong_answer_logic")),
            ("It prints 'Found it!' once.", Jump("wrong_answer_logic"))
        ],
        question_number=current_question
    )

# Correct Answer for Logic Error
label correct_answer_logic:
    if "logic_error" not in completed_quizzes:
        $ max_score += 1
        if "logic_error" not in missed_questions:
            $ score += 1
        $ completed_quizzes.add("logic_error")
        show harry at left
        harry "Excellent! The condition 'count > 5' is never true because the loop stops at count < 5. That's a logic error."
        
        # Add short conversation
        hide harry
        show kendall at right
        kendall "Oh! So the logic is wrong, even though the code runs without crashing."
        
        hide kendall
        show harry at left
        harry "Exactly! Logic errors are tricky because the code runs, but it doesn't do what you want."
        
        hide harry
        show kendall at right
        kendall "I'll definitely watch out for those!"
    return

# Wrong Answer for Logic Error
label wrong_answer_logic:
    if "logic_error" not in completed_quizzes:
        $ missed_questions.add("logic_error")
        $ attempts += 1
        show harry at left
        harry "Not quite. Look carefully at the condition inside the if statement compared to the while loop condition."

        if attempts >= 2:
            harry "Let me explain logic errors again."
            $ attempts = 0
            call logic_error from _call_logic_error_1
            jump logic_error_quiz
        else:
            menu:
                "Try again":
                    jump logic_error_quiz
                "Re-read about Logic Errors":
                    call logic_error from _call_logic_error_2
                    jump logic_error_quiz
    return


# ============================================================
# QUIZ 3: OFF-BY-ONE ERROR
# ============================================================
label off_by_one_quiz:
    # Skip if already completed
    if "off_by_one" in completed_quizzes:
        return

    # Show the quiz background image
    scene bg_off_by_one_quiz with fade

    # Display Harry to ask the question
    show harry at left
    harry "Let's test your understanding of off-by-one errors!"

    # Call the custom screen to display buttons
    call screen off_by_one_quiz_screen

    # After returning from the screen, check if we need to continue
    if "off_by_one" not in completed_quizzes:
        jump off_by_one_quiz
    return

# Custom screen for off-by-one error quiz
screen off_by_one_quiz_screen():
    $ current_question = 3  # This is the third question
    use quiz_template(
        question="Question 3: How many times does this loop print 'Hello'?",
        options=[
            ("6 times", Jump("wrong_answer_off_by_one")),
            ("5 times", Jump("correct_answer_off_by_one")),
            ("4 times", Jump("wrong_answer_off_by_one"))
        ],
        question_number=current_question
    )

# Correct Answer for Off-By-One Error
label correct_answer_off_by_one:
    if "off_by_one" not in completed_quizzes:
        $ max_score += 1
        if "off_by_one" not in missed_questions:
            $ score += 1
        $ completed_quizzes.add("off_by_one")
        show harry at left
        harry "Perfect! Count starts at 0, so the loop runs for 0, 1, 2, 3, and 4. That's 'Hello' five times before the condition fails."

        # Add short conversation
        hide harry
        show kendall at right
        kendall "I almost said 4. I assumed it started counting at 1."

        hide kendall
        show harry at left
        harry "And that's the trap. Off-by-one errors come from the starting value just as often as from the condition."

        hide harry
        show kendall at right
        kendall "Got it! I'll check both ends before I trust a loop."
    return

# Wrong Answer for Off-By-One Error
label wrong_answer_off_by_one:
    if "off_by_one" not in completed_quizzes:
        $ missed_questions.add("off_by_one")
        $ attempts += 1
        show harry at left
        harry "Not quite. Trace it carefully: count starts at 0, and the loop runs while count < 5. That's 0, 1, 2, 3, and 4."

        if attempts >= 2:
            harry "Let me explain off-by-one errors again."
            $ attempts = 0
            call off_by_one_error from _call_off_by_one_error_1
            jump off_by_one_quiz
        else:
            menu:
                "Try again":
                    jump off_by_one_quiz
                "Re-read about Off-By-One Errors":
                    call off_by_one_error from _call_off_by_one_error_2
                    jump off_by_one_quiz
    return


# ============================================================
# QUIZ 4: PRE-TEST LOGIC ERROR
# ============================================================
label pre_test_logic_quiz:
    # Skip if already completed
    if "pre_test_logic" in completed_quizzes:
        return

    # Show the quiz background image
    scene bg_pre_test_logic_error_quiz with fade

    # Display Harry to ask the question
    show harry at left
    harry "One more! This is about pre-test logic errors."

    # Call the custom screen to display buttons
    call screen pre_test_logic_quiz_screen

    # After returning from the screen, check if we need to continue
    if "pre_test_logic" not in completed_quizzes:
        jump pre_test_logic_quiz
    return

# Custom screen for pre-test logic error quiz
screen pre_test_logic_quiz_screen():
    $ current_question = 4  # This is the fourth question
    use quiz_template(
        question="Question 4: What is the output of this code?",
        options=[
            ("It prints nothing", Jump("correct_answer_pre_test")),
            ("It runs forever", Jump("wrong_answer_pre_test")),
            ("It prints 10, 11, 12, 13, 14", Jump("wrong_answer_pre_test"))
        ],
        question_number=current_question
    )

# Correct Answer for Pre-Test Logic Error
label correct_answer_pre_test:
    if "pre_test_logic" not in completed_quizzes:
        $ max_score += 1
        if "pre_test_logic" not in missed_questions:
            $ score += 1
        $ completed_quizzes.add("pre_test_logic")
        show harry at left
        harry "Correct! Since count starts at 10 and the condition is 'count < 5', the condition is false from the very beginning. The loop never runs!"
        
        # Add short conversation
        hide harry
        show kendall at right
        kendall "So the pre-test checks the condition first, sees it's false, and skips the entire loop?"
        
        hide kendall
        show harry at left
        harry "Exactly! That's why they're called pre-test loops—they test the condition before running any code."
        
        hide harry
        show kendall at right
        kendall "I need to make sure my starting values make sense with my loop conditions!"
    return

# Wrong Answer for Pre-Test Logic Error
label wrong_answer_pre_test:
    if "pre_test_logic" not in completed_quizzes:
        $ missed_questions.add("pre_test_logic")
        $ attempts += 1
        show harry at left
        harry "Not quite. Remember, pre-test loops check the condition BEFORE running any code."

        if attempts >= 2:
            harry "Let me explain pre-test logic errors again."
            $ attempts = 0
            call pre_test_logic_error from _call_pre_test_logic_error_1
            jump pre_test_logic_quiz
        else:
            menu:
                "Try again":
                    jump pre_test_logic_quiz
                "Re-read about Pre-Test Logic Errors":
                    call pre_test_logic_error from _call_pre_test_logic_error_2
                    jump pre_test_logic_quiz
    return

