label off_by_one_error:
    # Explanation for Off-By-One Error
    scene bg_maze_interior with dissolve
    
    # Harry starts the explanation
    show harry at left
    harry "An off-by-one error happens when the loop iterates one time too many or one time too few. It's one of the most common errors in coding."

    # Kendall asks for clarification
    hide harry
    show kendall at right
    kendall "So, the loop works, but it doesn’t cover all the cases? Like it skips something or stops too early?"

    # Harry elaborates
    hide kendall
    show harry at left
    harry "Exactly. Let me show you an example where we want to count up to 5, but the loop stops too early."

    # Show the first code snippet (incorrect) as background
    scene bg_off_by_one_code1 with dissolve
    "Harry points to the screen where the incorrect code is displayed."

    # Harry explains the mistake
    harry "In this code, the condition says 'count < 5', so the loop stops before reaching 5. The 'if' statement inside the loop checks if the number is 5, but it never prints 'True' because 5 isn’t included."

    # Kendall reacts
    hide harry
    show kendall at right
    kendall "Oh, I see! The loop condition makes it stop before 5, so it misses the chance to print 'True'."

    # Harry explains further
    hide kendall
    show harry at left
    harry "Exactly! Now let me show you how to fix it by updating the loop condition."

    # Show the fixed code as background
    scene bg_off_by_one_code2 with dissolve
    "Harry shows the corrected version of the code."

    # Harry explains the fix
    harry "Here’s the corrected version. By changing the condition to 'count <= 5', the loop includes 5. Now it prints 'True' when the count reaches 5."

    # Kendall reflects
    hide harry
    show kendall at right
    kendall "So, I just need to carefully check the loop conditions to make sure it does what I expect. Got it."

    # Harry confirms
    hide kendall
    show harry at left
    harry "Exactly! Paying attention to loop conditions will help you avoid off-by-one errors and other tricky mistakes."

    hide harry
    scene bg_maze_interior with dissolve

    jump choose_error

    return
