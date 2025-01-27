label infinite_loop_error:
    # Explanation for Infinite Loop
    scene bg_maze_interior with dissolve

    # Harry begins the explanation
    show harry at left
    harry "An infinite loop happens when the condition for the loop never becomes false. In simple terms, it just keeps going forever."

    # Kendall reacts with curiosity
    hide harry
    show kendall at right
    kendall "Forever? That sounds... bad. What would cause that to happen?"

    # Harry provides more detail
    hide kendall
    show harry at left
    harry "Let’s say you write a loop but forget to update the condition inside it."

    # Show the incorrect code snippet as background
    scene bg_infinite_loop_code1 with dissolve
    "Harry points to the screen where the incorrect code is displayed."

    # Harry elaborates
    harry "This kind of loop has no condition to stop, so it keeps running endlessly."

    # Kendall questions further
    hide harry
    show kendall at right
    kendall "So, the loop keeps asking the same question, but there’s no way to change the answer?"

    # Harry confirms
    hide kendall
    show harry at left
    harry "Exactly. Think of it like someone repeatedly asking, ‘Is it raining?’ when they’re inside and can’t check."
    harry "To fix it, you need to make sure the loop’s condition changes. For example, by updating a variable or checking a new value inside the loop."

    # Show the corrected code snippet as background
    scene bg_infinite_loop_code2 with dissolve
    "Harry shows the corrected version of the code."

    # Harry explains the fix
    harry "Here, we update the variable `count` in each iteration, so the condition eventually becomes false, and the loop stops."

    # Kendall reflects
    hide harry
    show kendall at right
    kendall "Got it! So, as long as we update the condition properly, the loop will end when it’s supposed to."

    return
