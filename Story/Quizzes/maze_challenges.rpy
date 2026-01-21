# ============================================================
# ENABLE PHASE - MAZE CODE CHALLENGES
# Students apply loop knowledge independently
# ============================================================

# ============================================================
# CHALLENGE 1: Navigate the Maze (Loop Condition)
# ============================================================
label maze_challenge_1:
    # Skip if already completed
    if "maze_challenge_1" in completed_quizzes:
        return

    # Show the challenge background image
    scene bg_maze_challenge_1 with fade

    # Display Harry to introduce the challenge
    show harry at left
    harry "Alright, we're at our first junction. I've got the basic navigation code here."
    harry "But I need you to tell me—what condition should keep us moving?"

    # Call the custom screen to display buttons
    call screen maze_challenge_1_screen

    # After returning from the screen, check if we need to continue
    if "maze_challenge_1" not in completed_quizzes:
        jump maze_challenge_1
    return

# Custom screen for maze challenge 1
screen maze_challenge_1_screen():
    $ challenge_number = 1  # First challenge
    use challenge_template(
        question="Challenge 1: Choose the correct loop condition",
        options=[
            ("while True", Jump("wrong_answer_challenge_1")),
            ("while at_exit", Jump("wrong_answer_challenge_1")),
            ("while not at_exit", Jump("correct_answer_challenge_1"))
        ],
        challenge_number=challenge_number
    )

# Correct Answer for Challenge 1
label correct_answer_challenge_1:
    if "maze_challenge_1" not in completed_quizzes:
        $ score += 1
        $ max_score += 1
        $ completed_quizzes.add("maze_challenge_1")
        show harry at left
        harry "Perfect! The loop should continue while we're NOT at the exit. Great job!"
        
        hide harry
        show kendall at right
        kendall "That makes sense! We keep going until we reach the exit."
        
        hide kendall
        show harry at left
        harry "Exactly! Let's move forward."
        hide harry
    return

# Wrong Answer for Challenge 1
label wrong_answer_challenge_1:
    if "maze_challenge_1" not in completed_quizzes:
        $ max_score += 1
        $ attempts += 1
        show harry at left
        harry "Not quite. Think about when the loop should keep running."

        if attempts >= 2:
            harry "Remember what we learned about loop conditions."
            $ attempts = 0
            menu:
                "Try again":
                    jump maze_challenge_1
                "Review concepts":
                    # Brief reminder without full error lesson
                    harry "We want the loop to continue WHILE we haven't reached the exit yet."
                    jump maze_challenge_1
        else:
            jump maze_challenge_1
    return


# ============================================================
# CHALLENGE 2: Prevent Infinite Loop (Add Safety Counter)
# ============================================================
label maze_challenge_2:
    # Skip if already completed
    if "maze_challenge_2" in completed_quizzes:
        return

    # Show the challenge background image
    scene bg_maze_challenge_2 with fade

    # Display Harry to introduce the challenge with story context
    show kendall at right
    kendall "Great! That worked! But... what if the maze has a glitch or something?"
    kendall "Couldn't we get stuck in an infinite loop?"
    
    hide kendall
    show harry at left
    harry "Good thinking! We should add a safety measure. What's the best way to write this loop condition?"

    # Call the custom screen to display buttons
    call screen maze_challenge_2_screen

    # After returning from the screen, check if we need to continue
    if "maze_challenge_2" not in completed_quizzes:
        jump maze_challenge_2
    return

# Custom screen for maze challenge 2
screen maze_challenge_2_screen():
    $ challenge_number = 2
    use challenge_template(
        question="Challenge 2: What's the safest loop condition?",
        options=[
            ("while not at_exit and steps < 100", Jump("correct_answer_challenge_2")),
            ("while steps < 100", Jump("wrong_answer_challenge_2")),
            ("while not at_exit", Jump("partial_answer_challenge_2"))
        ],
        challenge_number=challenge_number
    )

# Correct Answer for Challenge 2
label correct_answer_challenge_2:
    if "maze_challenge_2" not in completed_quizzes:
        $ score += 1
        $ max_score += 1
        $ completed_quizzes.add("maze_challenge_2")
        show harry at left
        harry "Excellent! Adding a step counter prevents infinite loops while still checking for the exit."
        
        hide harry
        show kendall at right
        kendall "So we check both conditions—not at exit AND haven't exceeded max steps!"
        
        hide kendall
        show harry at left
        harry "Exactly! This is a best practice in programming."
        hide harry
    return

# Partial Answer for Challenge 2
label partial_answer_challenge_2:
    if "maze_challenge_2" not in completed_quizzes:
        $ max_score += 1
        $ attempts += 1
        show harry at left
        harry "That works, but what if the maze has a bug? We might get stuck in an infinite loop!"
        harry "Think about what we learned about preventing infinite loops."
        
        if attempts >= 2:
            harry "Remember, we should add a safety counter to prevent infinite loops."
            $ attempts = 0
        jump maze_challenge_2
    return

# Wrong Answer for Challenge 2
label wrong_answer_challenge_2:
    if "maze_challenge_2" not in completed_quizzes:
        $ max_score += 1
        $ attempts += 1
        show harry at left
        harry "That's not quite right. We still need to check if we've reached the exit!"
        
        if attempts >= 2:
            harry "We need BOTH conditions: checking for the exit AND limiting the steps."
            $ attempts = 0
        jump maze_challenge_2
    return


# ============================================================
# CHALLENGE 3: Fix Off-By-One Error (Path Counting)
# ============================================================
label maze_challenge_3:
    # Skip if already completed
    if "maze_challenge_3" in completed_quizzes:
        return

    # Show the challenge background image
    scene bg_maze_challenge_3 with fade

    # Display with story context
    show harry at left
    harry "We're getting close! I can see the exit, but there are 5 different paths ahead."
    
    hide harry
    show kendall at right
    kendall "So we need to check all 5 paths, numbered 1 through 5?"
    
    hide kendall
    show harry at left
    harry "Exactly. Which loop condition will check all 5 without missing any?"

    # Call the custom screen to display buttons
    call screen maze_challenge_3_screen

    # After returning from the screen, check if we need to continue
    if "maze_challenge_3" not in completed_quizzes:
        jump maze_challenge_3
    return

# Custom screen for maze challenge 3
screen maze_challenge_3_screen():
    $ challenge_number = 3
    use challenge_template(
        question="Challenge 3: Check exactly 5 paths (1 to 5)",
        options=[
            ("while path < 6", Jump("correct_answer_challenge_3_alt")),
            ("while path < 5", Jump("wrong_answer_challenge_3")),
            ("while path <= 5", Jump("correct_answer_challenge_3"))
        ],
        challenge_number=challenge_number
    )

# Correct Answer for Challenge 3
label correct_answer_challenge_3:
    if "maze_challenge_3" not in completed_quizzes:
        $ score += 1
        $ max_score += 1
        $ completed_quizzes.add("maze_challenge_3")
        show harry at left
        harry "Perfect! Using <= 5 means we check paths 1, 2, 3, 4, and 5. That's exactly what we need!"
        
        hide harry
        show kendall at right
        kendall "I see! The <= includes 5, while < would stop before it."
        
        hide kendall
        show harry at left
        harry "Exactly! You've mastered off-by-one errors!"
        hide harry
    return

# Alternative Correct Answer for Challenge 3
label correct_answer_challenge_3_alt:
    if "maze_challenge_3" not in completed_quizzes:
        $ score += 1
        $ max_score += 1
        $ completed_quizzes.add("maze_challenge_3")
        show harry at left
        harry "Correct! Using < 6 also checks paths 1 through 5. Both this and <= 5 work!"
        
        hide harry
        show kendall at right
        kendall "So there can be multiple ways to write the same logic?"
        
        hide kendall
        show harry at left
        harry "Exactly! As long as the logic is correct, there are often multiple solutions."
        hide harry
    return

# Wrong Answer for Challenge 3
label wrong_answer_challenge_3:
    if "maze_challenge_3" not in completed_quizzes:
        $ max_score += 1
        $ attempts += 1
        show harry at left
        harry "Not quite. That would only check paths 1, 2, 3, and 4. We'd miss path 5!"
        harry "Remember what we learned about off-by-one errors."
        
        if attempts >= 2:
            harry "We need to include 5 in our check. Think about < versus <=."
            $ attempts = 0
        jump maze_challenge_3
    return
