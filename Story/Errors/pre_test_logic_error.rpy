label pre_test_logic_error:
    # Explanation for Pre-Test Logic Error
    scene bg_maze_interior with dissolve
    
    # Harry starts the explanation
    show harry at left
    harry "A pre-test logic error happens when the condition of the loop is false from the very beginning. This means the loop doesn’t run at all."

    # Kendall asks for clarification
    hide harry
    show kendall at right
    kendall "So, even if the code is written correctly, the loop doesn’t run because of the starting condition?"

    # Harry elaborates
    hide kendall
    show harry at left
    harry "Exactly. Let me show you an example where we set up a loop, but the starting condition makes it skip everything."

    # Show the first code snippet (incorrect) as background
    scene bg_pre_test_logic_error_code1 with dissolve
    "Harry points to the screen where the incorrect code is displayed."

    # Harry explains the mistake
    harry "In this code, the loop’s condition is 'count < 1', but the starting value is 5. Since the condition is false from the start, the loop doesn’t run."

    # Kendall reacts
    hide harry
    show kendall at right
    kendall "Oh, I see! The loop doesn’t even get a chance to start because the condition fails right away."

    # Harry explains further
    hide kendall
    show harry at left
    harry "Exactly! Now let me show you how to fix it by adjusting the starting value and condition."

    # Show the fixed code as background
    scene bg_pre_test_logic_error_code2 with dissolve
    "Harry shows the corrected version of the code."

    # Harry explains the fix
    harry "Here’s the corrected version. By setting the starting value to 1 and the condition to 'count <= 5', the loop runs as expected and prints the numbers from 1 to 5."

    # Kendall reflects
    hide harry
    show kendall at right
    kendall "So, I need to make sure the starting value and condition are aligned to allow the loop to run properly. Got it."

    # Harry confirms
    hide kendall
    show harry at left
    harry "Exactly! Setting the right initial value and condition is key to avoiding pre-test logic errors."

    hide harry
    scene bg_maze_interior with dissolve

    jump choose_error

    return
