label enable_phase:
    # Show the maze interior background
    scene bg_maze_interior with fade

    # Add ambient maze sounds
    play sound "maze_interior_ambience.ogg" fadein 2.0

    # Skip first challenge if already completed
    if "first_maze_challenge" not in completed_quizzes:
        # Harry introduces the interactive part
        show harry at left
        harry "Now that you understand how loops work and what can go wrong, it's time to put your knowledge to the test!"
        harry "I'll show you a code snippet, and you'll need to choose the correct condition to make the loop work properly."

        # First code challenge
        $ attempts = 0
        label .first_challenge:
            call screen code_challenge_1
            $ result = _return

            if result == "correct":
                $ score += 1
                $ max_score += 1
                $ completed_quizzes.add("first_maze_challenge")
                show harry at left
                harry "Perfect! You got it right! The loop should continue while we're not at the exit."
                harry "Let's try something a bit more challenging now."
            else:
                $ max_score += 1
                $ attempts += 1
                show harry at left
                if attempts >= 2:
                    harry "Let me explain this concept again..."
                    $ attempts = 0
                    jump infinite_loop_error
                else:
                    harry "Not quite right. Remember, we want to keep going while we haven't reached the exit."
                    harry "Try again with the same example."
                    jump .first_challenge

    # Skip final challenge if already completed
    if "final_maze_challenge" not in completed_quizzes:
        # Final maze challenge
        $ attempts = 0
        label .final_challenge:
            call screen final_maze_challenge
            $ result = _return

            if result == "correct":
                $ score += 1
                $ max_score += 1
                $ completed_quizzes.add("final_maze_challenge")
                show harry at left
                harry "Excellent! You've mastered the basics of pre-test loops!"
                harry "The step counter is a great addition to prevent infinite loops."
                "The maze walls begin to glow brighter, and a path forward becomes clear."
            elif result == "partial":
                $ max_score += 1
                $ attempts += 1
                show harry at left
                if attempts >= 2:
                    harry "Let me explain about infinite loops again..."
                    $ attempts = 0
                    jump infinite_loop_error
                else:
                    harry "Good try! You got the main condition right, but remember what we learned about infinite loops?"
                    harry "We should add a step counter to make sure we don't get stuck."
                    jump .final_challenge
            else:
                $ max_score += 1
                $ attempts += 1
                show harry at left
                if attempts >= 2:
                    harry "Let's review the concepts again..."
                    $ attempts = 0
                    jump infinite_loop_error
                else:
                    harry "Let's think about this again. Remember, we need to keep going while we haven't reached the exit."
                    harry "We should also count our steps to avoid getting stuck."
                    jump .final_challenge

    # Success ending (only shown when all challenges are completed)
    if len(completed_quizzes) >= 3:  # infinite_loop, first_maze_challenge, and final_maze_challenge
        show kendall at right
        kendall "Wow! The maze is actually responding to our code!"
        hide kendall
        show harry at left
        harry "That's the power of programming! Let's get out of here and continue our adventure!"
        
        # Show final score with visual feedback
        show screen final_score_display
        with dissolve
        pause 2.0
        hide screen final_score_display
        with dissolve
        
        # Return to main game flow
        return
    else:
        # If we somehow got here without completing everything, go back to appropriate section
        if "infinite_loop" not in completed_quizzes:
            jump infinite_loop_quiz
        elif "first_maze_challenge" not in completed_quizzes:
            jump enable_phase
        else:
            jump enable_phase

# Screen for the first code challenge
screen code_challenge_1():
    modal True
    
    # Code snippet image
    # Question 2: Code shows a maze navigation loop that needs a condition
    # Example:
    # while ___:
    #     move_forward()
    #     if at_wall():
    #         turn_right()
    add "code_challenge_1_image" xalign 0.5 yalign 0.3
    
    $ current_question = 2  # This is the second question in the sequence
    use quiz_template(
        question="Question 2: Choose the correct condition for the loop:",
        options=[
            ("while not at_exit()", Return("correct")),
            ("while at_exit()", Return("wrong")),
            ("while True", Return("wrong"))
        ],
        question_number=current_question
    )

# Screen for the final maze challenge
screen final_maze_challenge():
    modal True
    
    # Code snippet image
    # Question 3: Code shows a maze navigation loop that needs protection against infinite loops
    # Example:
    # steps = 0
    # while ___:
    #     move_forward()
    #     if at_wall():
    #         turn_right()
    #     steps += 1
    add "code_challenge_2_image" xalign 0.5 yalign 0.3
    
    $ current_question = 3  # This is the third question in the sequence
    use quiz_template(
        question="Question 3: Select the best loop condition:",
        options=[
            ("while not at_exit() and steps < 100", Return("correct")),
            ("while not at_exit()", Return("partial")),
            ("while True", Return("wrong"))
        ],
        question_number=current_question
    )

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